from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

from config import allQA, files, OURAI_SK, menuText, careerDeterminationLinks

from app.database.requests import get_appointment_name, get_appointments_str

router = Router()

class Reg(StatesGroup):
    name = State()
    surname = State()
    number = State()

#### OPENA AI ####

from openai import OpenAI

client = OpenAI(
  organization='org-AnVqaQuoMHqbQQJZlhIbtAYB',
  project='proj_7IGoDPzM2sVNHiSNsEhElmr2',
  api_key=OURAI_SK,
)


def getAiResponse(userPropmpt: str):
    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": userPropmpt,
        }],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content

##################

#### FUNCTIONS ####

dataBook = ""

def qaPrint():
    strr = ""
    for i in range(len(allQA)):
        strr += f'{i+1}. Q: ' + allQA[i]["Q"] + "\n"
        strr += 'A: ' + allQA[i]["A"] + "\n\n"
    return strr

def careerPrint():
    strr = ""
    for i in range(len(careerDeterminationLinks)):
        strr += f'{i+1}. ' + careerDeterminationLinks[i]["careerTestName"] + "\n"
        strr += 'URL: ' + careerDeterminationLinks[i]["careerTestLink"] + "\n\n"
    return strr

def changeDataBook(strr):
    global dataBook
    dataBook = strr

globalBool = False

def globalBoolChageToTrue():
    global globalBool
    globalBool = True
    return "Now you're talking with our AI  👀. Ask any questions about apllience to universities 📑."

def globalBoolChageToFalse():
    global globalBool
    globalBool = False
    return "The session with AI has ended ❗. Now you can use the main menu."

###################

#### REGISTER ####

data = {}


@router.callback_query(F.data == "reg_in")
async def reg_in(cb: CallbackQuery, state: FSMContext):
    await cb.answer('')
    await state.set_state(Reg.name)
    await cb.message.answer("Write your name: ")

@router.message(Reg.name)
async def reg_catch_name(msg: Message, state: FSMContext):
    await state.update_data(name = msg.text)
    await state.set_state(Reg.surname)
    await msg.answer("Write your surname: ")

@router.message(Reg.surname)
async def reg_catch_surname(msg: Message, state: FSMContext):
    await state.update_data(surname = msg.text)
    await state.set_state(Reg.number)
    await msg.answer("Write your number: ")

@router.message(Reg.number)
async def reg_catch_surname(msg: Message, state: FSMContext):
    await state.update_data(number = msg.text)
    global data
    data = await state.get_data()
    await msg.answer(f'{data["name"]} \n {data["number"]}')
###################

@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer("A", reply_markup=kb.main)
    await msg.answer('Hello!!! I am your School Councilor! Choose the option below to interact with me!', reply_markup=await kb.inline_first_menu())

@router.message(F.text.contains("Main Menu"))
async def main_menu_show(msg: Message):
    await msg.answer(menuText, reply_markup=await kb.inline_menu())

@router.message(F.text.contains("Connect me with"))
async def main_menu_show(msg: Message):
    await msg.reply("Here are councilor`s contacts:", reply_markup=await kb.inline_contacts())

#### FIRST MENU OPTIONS ####
@router.callback_query(F.data == "fm_start")
async def fm_start(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.answer(menuText, reply_markup=await kb.inline_menu())

@router.callback_query(F.data == "fm_wcyd")
async def fm_wcyd(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.answer("I am a school councilor bot that makes it easy for you to book an appointment and to get some basic information from the councilor!")

@router.callback_query(F.data == "fm_contacts")
async def fm_contacts(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.answer("Here are councilor`s contacts:", reply_markup=await kb.inline_contacts())

#### MAIN MENU OPTIONS ####
@router.callback_query(F.data == "menuBtnFiles")
async def menuBtnFiles(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.answer("Here are all the files:", reply_markup=await kb.inline_files())

@router.callback_query(F.data == "menuBtnQA")
async def menuBtnQA(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.answer(qaPrint())

@router.callback_query(F.data == "menuCareer")
async def menuBtnCareer(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.answer(careerPrint())

@router.callback_query(F.data == "appBook")
async def menuBtnAppBook(cb: CallbackQuery):
    await cb.answer('')
    await cb.message.answer("Look for available Appointments", reply_markup=await kb.inline_booking())

@router.callback_query(F.data.startswith("appointment_"))
async def menuBtnAppBookYes(cb: CallbackQuery):
    await cb.answer('')
    changeDataBook(cb.data)
    await cb.message.answer("Booked successfully!", reply_markup=await kb.inline_menu())

#### FILES ####
@router.callback_query(F.data == "f_bragSheet")
async def f_bragSheet(cb: CallbackQuery):
    filePath = files[0]["filePath"]
    await cb.answer('')
    await cb.message.reply_document(
        document=FSInputFile(
            path=filePath
        )
    )

@router.callback_query(F.data == "f_commonAppGuide")
async def f_commonAppGuide(cb: CallbackQuery):
    filePath = files[1]["filePath"]
    await cb.answer('')
    await cb.message.reply_document(
        document=FSInputFile(
            path=filePath
        )
    )

#################





@router.callback_query(F.data == "menuAI")
async def giveAIstream(cb: CallbackQuery):
    await cb.message.answer(globalBoolChageToTrue(), reply_markup=kb.mainAI2)

@router.message(F.text == "Quit AI")
async def quitAI(msg: Message):
    await msg.answer(globalBoolChageToFalse(),reply_markup=kb.main)
    await msg.answer(menuText,reply_markup=await kb.inline_menu())


@router.message(F.text)
async def takeUsersPrompt(msg: Message):
    if(globalBool == False):
        await msg.reply("Please write to our bot or contact the school counselor if you have any questions.")
    else:
        await msg.reply(getAiResponse(msg.text))
