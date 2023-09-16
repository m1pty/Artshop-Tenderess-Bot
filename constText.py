import constPrices, mGetter
import asyncio

menu_1 = "Tenderness Catcher - Главное меню\n"
channel = "Наш канал - (гиперссылка)\n"
fun = "\nПрисоединяйся, чтобы влиться в наше коммьюнити и не пропускать обновления бота!\n"
author = "\n🧑‍💻Создатель и поддержка бота: @jellyw00n"

artist_banner_main = "⭐️ БАННЕР ХУДОЖНИКОВ\n\n"
artist_banner_second = "В этом баннере падают только товары художников Тесс\n\n"

tess_banner_main = "⭐️ БАННЕР УСЛУГ ТЕНДЕРНЕСС\n\n"
tess_banner_second = "В этом баннере падают только услуги, которые предоставляет Тендернесс Шоп\n\n"

for_banner_one = "💸 Цена одной крутки - " + constPrices.twist + ", выбери количество круток\n\n"
for_banner_second = "У тебя есть: "

shop_up = "💸 МАГАЗИН УСЛУГ ТЕСС\n\nВ этом разделе Вы можете приобрести услуги Тендернесс\n\nДля пользователей:\n" 
shop_second = "Пиар на 12 часов – " + constPrices.piar_12_p + "\nПиар на 24 часа – " + constPrices.piar_24_p + "\nВыставление вашего конкурса | лотереи – "+ constPrices.contest_p + "\nВыставление вашего товара: адопта | юч | оты | коммишен поиска – "+ constPrices.product + "\n\n" 
shop_third = "Для шопов:\nПиар на 12 часов – " + constPrices.piar_12_s + "\nПиар на 24 часа – " + constPrices.piar_24_s + "\nВыставление вашего конкурса | лотереи – "+ constPrices.contest_s + "\nРепост набора – " + constPrices.repost

artist_banner = artist_banner_main + artist_banner_second + for_banner_one + for_banner_second
tess_banner = tess_banner_main + tess_banner_second + for_banner_one + for_banner_second

menu = menu_1 + channel + fun + author

shop = shop_up + shop_second + shop_third
balance = "💸 Твой баланс: "
donate = "💸 Вы можете приобрести тендеры за реальную валюту!"
faq = "❓ Тут будут ответы на частые вопросы"
piar = "Вы хотите приобрести эту услугу для себя или для шопа?"
product = 'Вы уверены, что хотите приобрести "выставление товара" за ' + constPrices.product + "?"
repost = 'Вы уверены, что хотите приобрести "репост набора" за ' + constPrices.repost + "?"

example1 = 'Вы уверены, что хотите приобрести '
piar12p = example1 + "пиар на 12 часов " + 'за ' + constPrices.piar_12_p + "?"
piar12s = example1 + "пиар на 12 часов для шопа " + 'за ' + constPrices.piar_12_s + "?"
piar24p = example1 + "пиар на 24 часа " + 'за ' + constPrices.piar_24_p + "?"
piar24s = example1 + "пиар на 24 часа для шопа " + 'за ' + constPrices.piar_24_s + "?"
contestp = example1 + "выставление конкурса " + 'за ' + constPrices.contest_p + "?"
contests = example1 + "выставление конкурса для шопа "  + 'за ' + constPrices.contest_s + "?"

#ПРИОБРЕТЕНИЕ

buying = "Поздравляем с приобретением!\n"
buying2 = "Для получения товара свяжитесь с нашим администратором с подтверждением в виде скрина или пересланного сообщения.\n\n"
admin = "Администратор - гиперссылка"

# ПИАР 12 ЧАСОВ для пользователя

p12p = "Вы приобрели: рекламу на 12 часов\n\n"
piar_12_p = buying + p12p + buying2 + admin

# ПИАР НА 24 ЧАСА для пользователя

p24p = "Вы приобрели: рекламу на 24 часа\n\n"
piar_24_p = buying + p24p + buying2 + admin

# ПИАР 12 ЧАСОВ для шопа

p12s = "Вы приобрели: рекламу на 12 часов для шопа\n\n"
piar_12_s = buying + p12s + buying2 + admin

# ПИАР НА 24 ЧАСА для шопа

p24s = "Вы приобрели: рекламу на 24 часа для шопа\n\n"
piar_24_s = buying + p24s + buying2 + admin

# КОНКУРС

cp = "Вы приобрели: выставление Вашего конкурса\n\n"
con_p = buying + cp + buying2 + admin

# КОНКУРС ДЛЯ ШОПА

cs = "Вы приобрели: выставление конкурса для шопа\n\n"
con_s = buying + cs + buying2 + admin

# ВЫСТАВЛЕНИЕ ТОВАРА

pr = "Вы приобрели: выставление Вашего товара\n\n"
prod = buying + pr + buying2 + admin

# РЕПОСТ НАБОР

rr = "Вы приобрели: репост набора\n\n"
rep = buying + rr + buying2 + admin

items = ""
# suka_blyat = await mGetter.getTable()
# for element in suka_blyat:
#     items += element[1]

donation = """
⭐️ Для пополнения баланса обратитесь к администратору!
👤 *Контакты администратора:* <...>
❓ *Что делать?*: В конце данного сообщения указан Ваш уникальный идентификатор. Для пополнения баланса обратитесь к администратору и совершите платёж на высланные реквезиты, в комментариях к нему укажите идентификатор. \n ⏳ *Платёж обрабатывается* в течение часа в ближайший к дате платежа рабочий день с 10:00 до 20:00 по МСК.
"""