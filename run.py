import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

from config import TOKEN, COUNSELOR_TG_ID
from app.handlers import router, data, dataBook

from app.database.models import async_main
from app.database.requests import get_appointment_name


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

async def main():
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)

# @dp.message(F.text == "Booked successfully!")
# async def process_start_command(message: Message):
#     await bot.send_message(chat_id=COUNSELOR_TG_ID, text=f'{data["name"]} booked for {get_appointment_name(int(dataBook))}') #like this
#     #await message.answer("test message") 
#     #or like this

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print('Exitted')