# -*- coding: utf-8 -*-
from telegram import Update, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7727497397:AAErCfm3BM4zV8aAbkNnmFJ9CUFZvibaAUQ'
IMG_PATH = "sno_bot_images"

async def send_album(update: Update, image_filenames: list, caption: str = None):
    media = []
    for i, filename in enumerate(image_filenames):
        with open(f"{IMG_PATH}/{filename}", "rb") as img:
            if i == 0 and caption:
                media.append(InputMediaPhoto(img.read(), caption=caption, parse_mode="Markdown"))
            else:
                media.append(InputMediaPhoto(img.read()))
    await update.message.reply_media_group(media)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_album(update, ["start.png"],
        "👋 *Привет! Я бот проекта СНО Московского Политеха.*\n\n"
        "Вот что я умею:\n"
        "/about — О проекте\n"
        "/team — Команда\n"
        "/rubrics — Рубрики\n"
        "/contentplan — Контент-план\n"
        "/results — Результаты\n"
        "/mascot — Маскот\n"
        "/future — Планы на будущее\n"
        "/contact — Контакты"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_album(update, ["about.png"],
        "🧪 *О проекте СНО*\n\n"
        "Проект направлен на популяризацию науки среди студентов. "
        "Мы создаем научно-популярный контент и рассказываем о студенческой науке доступно и интересно."
    )

async def team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_album(
        update,
        ["team.png"],
        """👥 *Команда Telegram-подгруппы:*

*Руководители подгруппы Telegram:*
1) Пшеничникова Арина  
2) Загирьянов Азат  

*Участники подгруппы Telegram:*  
1) Логвиненко Анастасия  
2) Карапецкий Александр  
3) Чарычанский Даниил  
4) Подлатова Мария  
5) Лебедев Арсений  
6) Курепин Владислав  
7) Кудрявцев Владислав  
8) Деменков Никита  
9) Володина Виктория  
10) Бондарь Тимофей  
11) Агеева Софья  

*Куратор проекта:*  
Осьминова Марианна Борисовна
"""
    )


async def rubrics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_album(update, [
        "rubric.jpeg",
        "rubric.png",
        "rubric (1).jpeg",
        "rubric (2).png",
        "rubric (3).png",
        "rubric (4).png",
        "rubric (5).png",
        "rubric (6).png",
        "rubric (7).png"
    ],
    "📚 *Рубрики Telegram-канала:*\n"
    "• Наука в быту\n"
    "• Научный фейл\n"
    "• Мемы\n"
    "• Школьный блиц\n"
    "• Рубрики с конкурсами и рилсами"
    )

async def contentplan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_album(
        update,
        ["contentplan.png", "contentplan (1).png"],
        """🗓 *Контент-план:*

• 10 марта: “Наука в быту” — очки  
• 12 марта: “Научный фейл” — NASA  
• 15 марта: Рилс №1 и реклама группы VK  
• 17 марта: “Наука в быту” — зубная паста  
• 19 марта: “Научный фейл” — 150$ миллионов  
• 21 марта: Рилс №2 и реклама группы VK  
• 23 марта: Мем  
• 24 марта: Кружок с розыгрышем  
• 26 марта: “Школьный блиц” — радуга  
• 30 марта: Маскот СНО  
• 6 апреля: “Школьный блиц” — брожение теста  

*Разработали контент-план:*  
Пшеничникова Арина  
Загирьянов Азат
"""
    )


async def results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_album(update, [
        "result (1).png",
        "result (2).png",
        "result (3).png"
    ],
    "📈 *Результаты:*\n"
    "Динамика подписчиков, вовлечённости, активности и охватов канала за всё время проекта."
    )

async def mascot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_album(update, ["mascot.png"],
        "🧪 *Маскот СНО* — это пробирка по имени Колберт, вызывающая улыбку и ассоциации с научным подходом и креативом."
    )

async def future(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_album(update, ["future.png"],
        "🚀 *Будущие планы:*\n"
        "• Развитие новых форматов\n"
        "• Расширение аудитории\n"
        "• Вовлечение студентов\n"
        "• Рост медиаприсутствия"
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_album(update, ["contacts.png"],
        "📬 *Контакты:*\n"
        "По всем вопросам можно обращаться в Telegram или к кураторам и руководителям.\n"
        "🌐 Сайт проекта: —"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("team", team))
    app.add_handler(CommandHandler("rubrics", rubrics))
    app.add_handler(CommandHandler("contentplan", contentplan))
    app.add_handler(CommandHandler("results", results))
    app.add_handler(CommandHandler("mascot", mascot))
    app.add_handler(CommandHandler("future", future))
    app.add_handler(CommandHandler("contact", contact))
    print("✅ Бот запущен!")
    app.run_polling()

if __name__ == '__main__':
    main()
