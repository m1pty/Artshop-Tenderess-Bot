import constPrices, mGetter
import asyncio

menu = """
Tenderness Catcher - Главное меню
Наш канал - (гиперссылка)

Присоединяйся, чтобы влиться в наше коммьюнити и не пропускать обновления бота!

🧑‍💻Создатель и поддержка бота: @jellyw00n
"""

artist_banner_main = "⭐️ БАННЕР ХУДОЖНИКОВ\n\n"
artist_banner_second = "В этом баннере падают только товары художников Тесс\n\n"

tess_banner_main = "⭐️ БАННЕР УСЛУГ ТЕНДЕРНЕСС\n\n"
tess_banner_second = "В этом баннере падают только услуги, которые предоставляет Тендернесс Шоп\n\n"

for_banner_one = f"💸 Цена одной крутки - {constPrices.allprices['twist']} тенд., выбери количество круток\n\n"

shop_up = "💸 МАГАЗИН УСЛУГ ТЕСС\n\nВ этом разделе Вы можете приобрести услуги Тендернесс\n\nДля пользователей:\n" 
shop_second = f"Пиар на 12 часов – {constPrices.allprices['piar_12_p']} тенд.\nПиар на 24 часа – {constPrices.allprices['piar_24_p']} тенд.\nВыставление вашего конкурса | лотереи – {constPrices.allprices['contest_p']} тенд.\nВыставление вашего товара: адопта | юч | оты | коммишен поиска – {constPrices.allprices['product']} тенд.\n\n" 
shop_third = f"Для шопов:\nПиар на 12 часов – {constPrices.allprices['piar_12_s']} тенд.\nПиар на 24 часа – {constPrices.allprices['piar_24_s']} тенд.\nВыставление вашего конкурса | лотереи – {constPrices.allprices['contest_s']} тенд.\nРепост набора – {constPrices.allprices['repost']} тенд. "
artist_banner = artist_banner_main + artist_banner_second + for_banner_one
tess_banner = tess_banner_main + tess_banner_second + for_banner_one

shop = shop_up + shop_second + shop_third
balance = "💸 Ваш баланс: "
inventory = "🎒 Ваш инвентарь: "
donate = "💸 Вы можете приобрести тендеры за реальную валюту!"
faq = "❓ Тут будут ответы на частые вопросы"
piar = "Вы хотите приобрести эту услугу для себя или для шопа?"
product = f"Вы уверены, что хотите приобрести \"выставление товара\" за {constPrices.allprices['product']} тенд.?"
repost = f"Вы уверены, что хотите приобрести \"репост набора\" за {constPrices.allprices['repost']} тенд.?"

example1 = 'Вы уверены, что хотите приобрести '
piar12p =  example1 + f"пиар на 12 часов за {constPrices.allprices['piar_12_p']} тенд.?"
piar12s =  example1 + f"пиар на 12 часов для шопа за {constPrices.allprices['piar_12_s']} тенд.?"
piar24p =  example1 + f"пиар на 24 часа за {constPrices.allprices['piar_24_p']} тенд.?"
piar24s =  example1 + f"пиар на 24 часа для шопа за {constPrices.allprices['piar_24_s']} тенд.?"
contestp = example1 + f"выставление конкурса за {constPrices.allprices['contest_p']} тенд.?"
contests = example1 + f"выставление конкурса для шопа за {constPrices.allprices['contest_s']} тенд.?"

#ПРИОБРЕТЕНИЕ

buying =  "Поздравляем с приобретением!\n\n"
buying1 = "Поздравляем! Выбитые предметы:\n\n"
buying2 = "⭐️ *Для получения товара свяжитесь с нашим администратором* с подтверждением в виде скрина или пересланного сообщения.\n\n"
admin =   "👤 *Администратор:* <...>"

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

❓ *Что делать?*: В конце данного сообщения указан Ваш уникальный идентификатор. Для пополнения баланса обратитесь к администратору и совершите платёж на высланные реквезиты, в комментариях к нему укажите идентификатор.

⏳ *Платёж обрабатывается* в течение часа в ближайший к дате платежа рабочий день с 10:00 до 20:00 по МСК.
"""

buying_failure = "Для совершения этой покупки у Вас недостаточно средств!"