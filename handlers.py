from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode #настройки разметки сообщений
import os

import constConfig, constKeyboards, constText, constPrices, constIds
import mGetter, mSetter, mChecker, roulette

router = Router()
bot = Bot(token = constConfig.BOT_TOKEN)

# создание персонального каталога пользователя
@router.message(F.text == "/start")
async def newUser(msg: types.Message):
    user_id = str(msg.chat.id)

    # инициализация нулевого баланса, если нужно
    if (not await mChecker.checkAccountExistance(user_id)):
        await mSetter.setNewUserBalance(user_id)
        await mSetter.setNewUserDrop(user_id)
        print(f"[SYSTEM]: mChecker.checkAccountExistance ({user_id}) -> False")
        print(f"[SYSTEM]: mSetter.setNewUserBalance ({user_id})")
    else:
        print(f"[SYSTEM]: mChecker.checkAccountExistance ({user_id}) -> True")

    await bot.send_photo(
        chat_id = msg.chat.id,
        photo = "https://drive.google.com/uc?export=view&id=17QJp24TenAD19ozJBGG4nUd14VavdpVQ",
        caption = constText.menu, reply_markup = constKeyboards.menu_kb, parse_mode = "HTML"
    )

# возвращение в меню
@router.message(F.text == "Вернуться в меню")
async def menu(msg: types.Message):
    await bot.send_photo(
        chat_id = msg.chat.id, 
        photo = "https://drive.google.com/uc?export=view&id=17QJp24TenAD19ozJBGG4nUd14VavdpVQ", 
        caption = constText.menu, reply_markup = constKeyboards.menu_kb, parse_mode = "HTML"
    )

# донат
@router.message(F.text == "Донат")
async def donation(msg: types.Message):
    message = constText.donation + f"\n{msg.chat.id}"
    await msg.answer(
        text = message,
        reply_markup = constKeyboards.menu_kb,
        parse_mode = "Markdown"
    )

# баннеры
banner_commands = {
    "Баннер художников": {
        "photo":        "https://drive.google.com/uc?export=view&id=17QJp24TenAD19ozJBGG4nUd14VavdpVQ",
        "caption":      constText.artist_banner,
        "reply_markup": constKeyboards.banner_kb_artists
    },
    "Баннер Тесс":       {
        "photo":        "https://drive.google.com/uc?export=view&id=17QJp24TenAD19ozJBGG4nUd14VavdpVQ",
        "caption":      constText.tess_banner,
        "reply_markup": constKeyboards.banner_kb_tess
    },
}

commands = {
    "Вернуться в магазин":  {"text": constText.shop,    "reply_markup": constKeyboards.shop_kb},
    "Магазин":              {"text": constText.shop,    "reply_markup": constKeyboards.shop_kb},
    "Донат":                {"text": constText.donate,  "reply_markup": constKeyboards.donate },
    "FAQ":                  {"text": constText.faq,     "reply_markup": constKeyboards.faq    },
    "Пиар на 12 часов":     {"text": constText.piar,    "reply_markup": constKeyboards.piar_12},
    "Пиар на 24 часа" :     {"text": constText.piar,    "reply_markup": constKeyboards.piar_24},
    "Выставление конкурса": {"text": constText.piar,    "reply_markup": constKeyboards.contest},
    "Выставление товара":   {"text": constText.product, "reply_markup": constKeyboards.letsgo_product},
    "Репост набора":        {"text": constText.repost,  "reply_markup": constKeyboards.letsgo_repost },
    
    # выбор пиара
    "Приобрести пиар на 12 часов для себя":     {"text": constText.piar12p, "reply_markup": constKeyboards.letsgo_piar_12_p},
    "Приобрести пиар на 12 часов для шопа":     {"text": constText.piar12s, "reply_markup": constKeyboards.letsgo_piar_12_s},
    "Приобрести пиар на 24 часа для себя" :     {"text": constText.piar24p, "reply_markup": constKeyboards.letsgo_piar_24_p},
    "Приобрести пиар на 24 часа для шопа" :     {"text": constText.piar24s, "reply_markup": constKeyboards.letsgo_piar_24_s},
    "Приобрести выставление конкурса для себя": {"text": constText.contestp, "reply_markup": constKeyboards.letsgo_contest_p}, # конкурс для пользователя
    "Приобрести выставление конкурса для шопа": {"text": constText.contests, "reply_markup": constKeyboards.letsgo_contest_s}, # конкурс для шопа
}

# пиар 12 часов для пользователя
@router.message(F.text == "Потратить тендеры")
async def buyPiar12P(msg: types.Message):
    balance = await mGetter.getBalance(msg.chat.id)
    price = constPrices.allprices["piar_12_p"]
    if (balance >= price):
        await mSetter.setBalance(msg.chat.id, balance - price)
        await mSetter.setUserArtistDropById(msg.chat.id, constIds.ids["piar_12_p"])
        await msg.answer(
            text = constText.piar_12_p,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 
    else:
        await msg.answer(
            text = constText.buying_failure,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 

# пиар 12 часов для шопа
@router.message(F.text == "Пoтратить тендеры")
async def buyPiar12S(msg: types.Message):
    balance = await mGetter.getBalance(msg.chat.id)
    price = constPrices.allprices["piar_12_s"]
    if (balance >= price):
        await mSetter.setBalance(msg.chat.id, balance - price)
        await mSetter.setUserArtistDropById(msg.chat.id, constIds.ids["piar_12_s"])
        await msg.answer(
            text = constText.piar_12_s,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 
    else:
        await msg.answer(
            text = constText.buying_failure,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 

# пиар 24 часа для пользователя
@router.message(F.text == "Потратить тeндеры")
async def buyPiar24P(msg: types.Message):
    balance = await mGetter.getBalance(msg.chat.id)
    price = constPrices.allprices["piar_24_p"]
    if (balance >= price):
        await mSetter.setBalance(msg.chat.id, balance - price)
        await mSetter.setUserArtistDropById(msg.chat.id, constIds.ids["piar_24_p"])
        await msg.answer(
            text = constText.piar_24_p,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 
    else:
        await msg.answer(
            text = constText.buying_failure,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 

# пиар 24 часа для шопа
@router.message(F.text == "Потратить тендeры")
async def buyPiar24S(msg: types.Message):
    balance = await mGetter.getBalance(msg.chat.id)
    price = constPrices.allprices["piar_24_s"]
    if (balance >= price):
        await mSetter.setBalance(msg.chat.id, balance - price)
        await mSetter.setUserArtistDropById(msg.chat.id, constIds.ids["piar_24_s"])
        await msg.answer(
            text = constText.piar_24_s,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 
    else:
        await msg.answer(
            text = constText.buying_failure,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 

# конкурс для пользователя
@router.message(F.text == "Потратить тeндeры")
async def buyConP(msg: types.Message):
    balance = await mGetter.getBalance(msg.chat.id)
    price = constPrices.allprices["contest_p"]
    if (balance >= price):
        await mSetter.setBalance(msg.chat.id, balance - price)
        await mSetter.setUserArtistDropById(msg.chat.id, constIds.ids["contest_p"])
        await msg.answer(
            text = constText.con_p,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 
    else:
        await msg.answer(
            text = constText.buying_failure,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 

# конкурс для шопа
@router.message(F.text == "Пoтратить тeндeры")
async def buyConS(msg: types.Message):
    balance = await mGetter.getBalance(msg.chat.id)
    price = constPrices.allprices["contest_s"]
    if (balance >= price):
        await mSetter.setBalance(msg.chat.id, balance - price)
        await mSetter.setUserArtistDropById(msg.chat.id, constIds.ids["contest_s"])
        await msg.answer(
            text = constText.con_s,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 
    else:
        await msg.answer(
            text = constText.buying_failure,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 

# продукт
@router.message(F.text == "Пoтратить тeндеры")
async def buyProduct(msg: types.Message):
    balance = await mGetter.getBalance(msg.chat.id)
    price = constPrices.allprices["product"]
    if (balance >= price):
        await mSetter.setBalance(msg.chat.id, balance - price)
        await mSetter.setUserArtistDropById(msg.chat.id, constIds.ids["product"])
        await msg.answer(
            text = constText.prod,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 
    else:
        await msg.answer(
            text = constText.buying_failure,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 

# репост
@router.message(F.text == "Пoтратить тендeры")
async def buyRepost(msg: types.Message):
    balance = await mGetter.getBalance(msg.chat.id)
    price = constPrices.allprices["repost"]
    if (balance >= price):
        await mSetter.setBalance(msg.chat.id, balance - price)
        await mSetter.setUserArtistDropById(msg.chat.id, constIds.ids["repost"])
        await msg.answer(
            text = constText.rep,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 
    else:
        await msg.answer(
            text = constText.buying_failure,
            reply_markup = constKeyboards.done,
            parse_mode = "Markdown"
        ) 

# предметы баннера художников
@router.message(F.text == "Предметы баннера")
async def handleArtBannerItems(msg: types.Message):
    possible = await mGetter.getArtBannerDrop()
    reply = constText.art_banner_items
    for element in possible:
        reply += f"\n📎 {element[1]} (x{element[2]})"

    await msg.answer(
        text = reply,
        reply_markup = constKeyboards.artist_kb, 
        parse_mode = "Markdown"
    )

# предметы баннера Тесс
@router.message(F.text == "Пpедметы баннера")
async def handleTessBannerItems(msg: types.Message):
    possible = await mGetter.getTessBannerDrop()
    reply = constText.tess_banner_items
    for element in possible:
        reply += f"\n📎 {element[1]}"

    await msg.answer(
        text = reply,
        reply_markup = constKeyboards.tess_kb,
        parse_mode = "Markdown"
    )

# обработчик любых команд баннера
@router.message(F.text.in_(banner_commands.keys()))
async def AnyBannerHandler(msg: types.Message):
    msg_text = msg.text
    await bot.send_photo(
        chat_id = msg.chat.id,
        photo = banner_commands[msg_text]["photo"],
        caption = banner_commands[msg_text]["caption"],
        reply_markup = banner_commands[msg_text]["reply_markup"], 
        parse_mode = "HTML"
    )

# вывод баланса
@router.message(F.text == "Баланс")
async def handleBalance(msg: types.Message):
    balance   = await mGetter.getBalance(msg.chat.id)
    inventory = await mGetter.getUserInventory(msg.chat.id)
    inventory_reply = constText.inventory
    for element in inventory:
        inventory_reply += f"\n- {element[1]} (x{element[2]})"

    text_reply = constText.balance + str(balance) + f"\n{inventory_reply}"
    await msg.answer(
        text = text_reply,
        reply_markup = constKeyboards.balance, 
        parse_mode = "Markdown"
    )

# обработка команд
@router.message(F.text.in_(list(commands.keys())))
async def handleAnyCommand(msg: types.Message):
    msg_text = msg.text
    await msg.answer(
        text = commands[msg_text]["text"],
        reply_markup = commands[msg_text]["reply_markup"],
        parse_mode = "HTML"
    )

# попытка крутить баннер
# ДОБАВИТЬ ЗВУКИ ПАДАЮАЩИХ ЗВЕЗДОЧЕК
spend_spins = [
    "Потратить круток: 1", "Потратить круток: 3", "Потратить круток: 5", 
    "Потратить крутoк: 1", "Потратить крутoк: 3", "Потратить крутoк: 5"
]
@router.message(F.text.in_(spend_spins))
async def RollBanner(msg: types.Message):
    text = msg.text.lower()
    await msg.answer(
        text = "Загружаем результат...",
        parse_mode = "HTML"
    )
    await roulette.getRouletteDrop(bot, msg)

@router.message(F.text == "Меню разработчика")
async def handleTessBannerItems(msg: types.Message):
    await msg.answer(
        text = constText.admin_menu,
        reply_markup = constKeyboards.tess_kb,
        parse_mode = "Markdown"
    )