from aiogram import Bot, Dispatcher, types
import random, os, sqlite3

import constText, constKeyboards, constPaths, constIds
import mGetter, mChecker, mSetter, constPrices

# английские буквы
tess_banner_drop = [
    {"name": "Пиар на 12ч", "probability": 30},
    {"name": "Пиар на 24ч", "probability": 16},
    {"name": "Рисунок от artist1", "probability": 18},
    {"name": "Рисунок от artist2", "probability": 18},
    {"name": "Рисунок от artist3", "probability": 18}
]

# рулетка (художников / Тесс)
async def getRouletteDrop(bot: Bot, message: types.Message):
    # парсер числа круток
    spins = int(message.text[message.text.find(": ") + 2 :])

    # выбор предметов баннера
    # banner_drop = artist_banner_drop if ('круток' in message.text.lower()) else tess_banner_drop

    # проверка баланса
    balance = await mGetter.getBalance(message.chat.id)

    # если хватает денег на крутку
    if (balance >= spins * constPrices.allprices["twist"]):
        
        # выбитые предметы
        collected_drop = []
        for spin in range(spins):
            current_drop = await mGetter.getBannerResult()
            if (current_drop == 0):
                break
            
            balance -= constPrices.allprices["twist"]
            await mSetter.setBalance(message.chat.id, balance) # уменьшение баланса пользователя
            await mSetter.setBannerDropQuantity(current_drop)  # уменьшение числа оставшихся предметов
            collected_drop.append(current_drop)
        
        # переводим дроп из id в названия
        conn = sqlite3.connect(constPaths.db_paths["banner_prizes"], check_same_thread = False)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM possible_prizes")
        exists = cursor.fetchall()
        cursor.close(); conn.close()

        # выводим полученный дроп
        reply = f"{message.chat.id}" + constText.buying1
        for drop in collected_drop:
            for result in exists:
                if (result[0] == drop):
                    reply += f"- {result[1]}\n"
                    break
        reply += f"\n{constText.buying2}"
        reply += constText.admin
        
        # заполняем дроп пользователю
        for drop in collected_drop:
            await mSetter.setUserArtistDropById(message.chat.id, drop)
                        
        # отправляем сообщение в ответ
        await message.answer(
            text = reply,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        )
    
    else:
        # если не хватило денег
        await message.answer(
            text = constText.buying_failure,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        )
