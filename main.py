
from telegram.ext import ApplicationBuilder
from handlers.commands import register_command_handlers
from handlers.messages import register_message_handlers
from handlers.callbacks import register_callback_handlers
from services.database import init_db
from config import TELEGRAM_BOT_TOKEN

def main():
    init_db()  # Инициализация базы данных

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    register_command_handlers(application)
    register_message_handlers(application)
    register_callback_handlers(application)

    print("✅ Бот запущен")
    application.run_polling()

if __name__ == "__main__":
    main()
