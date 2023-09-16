from aiogram import Bot, Dispatcher, types
import random, os, sqlite3
import constText, constKeyboards, constPaths

# английские буквы
tess_banner_drop = [
    {"name": "Пиар на 12ч", "probability": 30},
    {"name": "Пиар на 24ч", "probability": 16},
    {"name": "Рисунок от artist1", "probability": 18},
    {"name": "Рисунок от artist2", "probability": 18},
    {"name": "Рисунок от artist3", "probability": 18}
]

artist_banner_drop = [
    {"name": "Пиар на 12ч", "probability": 30},
    {"name": "Пиар на 24ч", "probability": 16},
    {"name": "Рисунок от artist1", "probability": 18},
    {"name": "Рисунок от artist2", "probability": 18},
    {"name": "Рисунок от artist3", "probability": 18}
]

# 1/3/5 круток
async def GetRouletteDrop(bot: Bot, message: types.Message):
    # парсер числа круток
    spins = int(message.text[message.text.find(": ") + 2 :])

    # баннер художников
    if ('круток' in message.text.lower()):
        banner_drop = artist_banner_drop
    else:
        banner_drop = tess_banner_drop

    # проверка баланса
    user_id = str(message.chat.id)
    user_path = os.path.join(os.getcwd(), "database", user_id)
    if (os.path.exists(user_path)):
        with open(os.path.join(user_path, "balance.txt"), "r") as file:
            balance = int(file.read().replace("\n", ""))

    # если хватает денег на крутку
    if (balance >= spins):
        # изменяем баланс в связи с покупкой
        with open(os.path.join(user_path, "balance.txt"), "w") as file:
            file.write(str(balance - spins))

        collected_drop = []       # выбитые штуки
        for spin in range(spins):
            # выбор произвольного варианта
            options = [x for x in range(1, 101)]
            chosen_option = random.choice(options)

            # идёт по всем возможным опциям, и складывает их вероятности, чтобы
            # выбитый процент <chosen_option> указывал на нужную опцию
            current_percentage = 0
            for drop_item in banner_drop:
                if (current_percentage + drop_item["probability"] >= chosen_option):
                    collected_drop.append(drop_item["name"])
                    break
                
                else:
                    current_percentage += drop_item["probability"]
            
        # выводим полученный дроп
        reply = "Поздравляем! Выбитые предметы:\n"
        for drop in collected_drop:
            reply += f"- {drop}\n\n"
            reply += constText.buying2
            reply += constText.admin
        
        #
        #
        # записывает результат для пользователя
        #
        #
                        
        # отправляем сообщение в ответ
        await message.answer(
            text = reply,
            reply_markup = constKeyboards.done,
            parse_mode = "HTML"
        )
    
    else:
        await message.answer(
            text = "Ваш баланс недостаточен для выполнения данной операции!",
            reply_markup = constKeyboards.kb_d,
            parse_mode = "HTML"
        )
