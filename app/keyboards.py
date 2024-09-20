from config import files, menu, first_menu, contacts



from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from app.database.requests import get_appointments_str



main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Main Menu  🔠")],
    [KeyboardButton(text="Connect me with councilor  👀")],
],
resize_keyboard=True
)

mainAI2 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Quit AI")],
],
resize_keyboard=True
)

# buttonUnder = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4")],
#     [InlineKeyboardButton(text="Not YT", url="https://www.youtube.com/watch?v=LusIE2r-5to")]
# ])




async def inline_first_menu():
    keyboard = InlineKeyboardBuilder()
    for firstMenuOptions in first_menu:
        keyboard.add(InlineKeyboardButton(text=firstMenuOptions["option"], callback_data=firstMenuOptions["callback"]))
    return keyboard.adjust(2).as_markup()


async def inline_files():
    keyboard = InlineKeyboardBuilder()
    for file in files:
        keyboard.add(InlineKeyboardButton(text=file["fileName"], callback_data=file["fileBtnCallback"]))
    return keyboard.adjust(1).as_markup()

async def inline_menu():
    keyboard = InlineKeyboardBuilder()
    for menuOptions in menu:
        keyboard.add(InlineKeyboardButton(text=menuOptions["option"], callback_data=menuOptions["callback"]))
    return keyboard.adjust(2,1,1).as_markup()

async def inline_contacts():
    keyboard = InlineKeyboardBuilder()
    for contact in contacts:
        keyboard.add(InlineKeyboardButton(text=contact["contact"], url=contact["url"]))
    return keyboard.adjust(1).as_markup()

async def inline_booking():
  all_appointments = await get_appointments_str()
  keyboard = InlineKeyboardBuilder()
  for appointments in all_appointments:
    if(appointments.booked == 0):
        keyboard.add(InlineKeyboardButton(text=appointments.date, callback_data=f"appointment_{appointments.id}"))
  return keyboard.adjust(2).as_markup()