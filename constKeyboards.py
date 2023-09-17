from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

# menu:
kb_m = [
    [KeyboardButton(text = "Баннер художников")],
    [KeyboardButton(text = "Баннер Тесс")],
    [KeyboardButton(text = "Магазин"), KeyboardButton(text = "Баланс")],
    [KeyboardButton(text = "Донат")],
    [KeyboardButton(text = "FAQ")]
]
menu_kb = ReplyKeyboardMarkup(keyboard = kb_m, resize_keyboard = True)

#banners:

# banner artists
kb_banner_artists = [
    [KeyboardButton(text = "Потратить круток: 1")], [KeyboardButton(text = "Потратить круток: 3")], [KeyboardButton(text = "Потратить круток: 5")], [KeyboardButton(text = "Предметы баннера")], [KeyboardButton(text = "Вернуться в меню")]
]
banner_kb_artists = ReplyKeyboardMarkup(keyboard = kb_banner_artists, resize_keyboard = True)

# banner tess 
# заменены о на английские в слове круток и р на английскую в слове предметы
kb_banner_tess = [
    [KeyboardButton(text = "Потратить крутoк: 1")], [KeyboardButton(text = "Потратить крутoк: 3")], [KeyboardButton(text = "Потратить крутoк: 5")], [KeyboardButton(text = "Пpедметы баннера")], [KeyboardButton(text = "Вернуться в меню")]
]
banner_kb_tess = ReplyKeyboardMarkup(keyboard = kb_banner_tess, resize_keyboard = True)

# shop:
kb_s = [
    [KeyboardButton(text = "Пиар на 12 часов"), KeyboardButton(text = "Пиар на 24 часа")],
    [KeyboardButton(text = "Выставление конкурса")],
    [KeyboardButton(text = "Выставление товара")],
    [KeyboardButton(text = "Репост набора")],
    [KeyboardButton(text = "Вернуться в меню")]
]
shop_kb = ReplyKeyboardMarkup(keyboard = kb_s, resize_keyboard = True)

#balance:
kb_b = [
    [KeyboardButton(text = "Донат")],
    [KeyboardButton(text = "Вернуться в меню")]
]
balance = ReplyKeyboardMarkup(keyboard = kb_b, resize_keyboard = True)

#donation:
kb_d = [
    [KeyboardButton(text = "Приобрести тендеры")],
    [KeyboardButton(text = "Вернуться в меню")]
]
donate = ReplyKeyboardMarkup(keyboard = kb_d, resize_keyboard = True)

#faq:
kb_faq = [
    [KeyboardButton(text = "Вернуться в меню")]
]
faq = ReplyKeyboardMarkup(keyboard = kb_faq, resize_keyboard = True)

#piar 12:
kb_12 = [
    [KeyboardButton(text = "Приобрести пиар на 12 часов для себя")],
    [KeyboardButton(text = "Приобрести пиар на 12 часов для шопа")],
    [KeyboardButton(text = "Вернуться в магазин")]
]
piar_12 = ReplyKeyboardMarkup(keyboard = kb_12, resize_keyboard = True)

#piar 24:
kb_24 = [
    [KeyboardButton(text = "Приобрести пиар на 24 часа для себя")],
    [KeyboardButton(text = "Приобрести пиар на 24 часа для шопа")],
    [KeyboardButton(text = "Вернуться в магазин")]
]
piar_24 = ReplyKeyboardMarkup(keyboard = kb_24, resize_keyboard = True)

#contest:
kb_contest = [
    [KeyboardButton(text = "Приобрести выставление конкурса для себя")],
    [KeyboardButton(text = "Приобрести выставление конкурса для шопа")],
    [KeyboardButton(text = "Вернуться в магазин")]
]
contest = ReplyKeyboardMarkup(keyboard = kb_contest, resize_keyboard = True)


# acception for shop:
kb_letsgo_piar_12_p = [
    [KeyboardButton(text = "Потратить тендеры")], # нет изменений
    [KeyboardButton(text = "Вернуться в меню")]
]

letsgo_piar_12_p = ReplyKeyboardMarkup(keyboard = kb_letsgo_piar_12_p, resize_keyboard = True)
kb_letsgo_piar_12_s = [
    [KeyboardButton(text = "Пoтратить тендеры")], # буква о заменена на английскую
    [KeyboardButton(text = "Вернуться в меню")]
]
letsgo_piar_12_s = ReplyKeyboardMarkup(keyboard = kb_letsgo_piar_12_s, resize_keyboard = True)

kb_letsgo_piar_24_p = [
    [KeyboardButton(text = "Потратить тeндеры")], # первая буква е заменена на английскую
    [KeyboardButton(text = "Вернуться в меню")]
]
letsgo_piar_24_p = ReplyKeyboardMarkup(keyboard = kb_letsgo_piar_24_p, resize_keyboard = True)

kb_letsgo_piar_24_s = [
    [KeyboardButton(text = "Потратить тендeры")], # вторая буква е заменена на английскую
    [KeyboardButton(text = "Вернуться в меню")]
]
letsgo_piar_24_s = ReplyKeyboardMarkup(keyboard = kb_letsgo_piar_24_s, resize_keyboard = True)

kb_letsgo_contest_p = [
    [KeyboardButton(text = "Потратить тeндeры")], # две буквы е заменены на английскую
    [KeyboardButton(text = "Вернуться в меню")]
]
letsgo_contest_p = ReplyKeyboardMarkup(keyboard = kb_letsgo_contest_p, resize_keyboard = True)

kb_letsgo_contest_s = [
    [KeyboardButton(text = "Пoтратить тeндeры")], # две буквы е заменены на английскую и о тоже
    [KeyboardButton(text = "Вернуться в меню")]
]
letsgo_contest_s = ReplyKeyboardMarkup(keyboard = kb_letsgo_contest_s, resize_keyboard = True)

kb_letsgo_product = [
    [KeyboardButton(text = "Пoтратить тeндеры")], # первая буква е заменена на английскую и о тоже
    [KeyboardButton(text = "Вернуться в меню")]
]
letsgo_product = ReplyKeyboardMarkup(keyboard = kb_letsgo_product, resize_keyboard = True)

kb_letsgo_repost = [
    [KeyboardButton(text = "Пoтратить тендeры")], # вторая буква е заменена на английскую и о тоже
    [KeyboardButton(text = "Вернуться в меню")]
]
letsgo_repost = ReplyKeyboardMarkup(keyboard = kb_letsgo_repost, resize_keyboard = True)

# покупка совершена
kb_done = [
    [KeyboardButton(text = "Вернуться в меню")]
]
done = ReplyKeyboardMarkup(keyboard = kb_done, resize_keyboard = True)

kb_tess = [
    [KeyboardButton(text = "Баннер Тесс")],
    [KeyboardButton(text = "Вернуться в меню")]
]
tess_kb = ReplyKeyboardMarkup(keyboard = kb_tess, resize_keyboard = True)

kb_artist = [
    [KeyboardButton(text = "Баннер художников")],
    [KeyboardButton(text = "Вернуться в меню")]
]
artist_kb = ReplyKeyboardMarkup(keyboard = kb_artist, resize_keyboard = True)