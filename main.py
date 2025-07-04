import asyncio
import aiohttp
import csv
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import TOKEN, GOOGLE_API_KEY, CSV_URL
from handlers.cash import register_cash_handlers
from handlers.crypto import register_crypto_handlers
from handlers.start import register_start_handlers

bot = Bot(token=TOKEN)
dp = Dispatcher()
google = GOOGLE_API_KEY



# 👇 Регистрация всех хендлеров
def register_all_handlers(dp: Dispatcher):
    register_cash_handlers(dp)
    register_crypto_handlers(dp)
    register_start_handlers(dp)

# 🚀 Запуск бота
async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        register_all_handlers(dp)
        print("🤖 Бот запущен...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Ошибка запуска бота: {e}")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('👋 Бот остановлен')
    except Exception as e:
        print(f'❌ Критическая ошибка: {e}')
