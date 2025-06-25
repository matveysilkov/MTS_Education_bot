from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dotenv import load_dotenv  # Импортируем функцию для загрузки переменных из .env
import os  # Модуль для работы с операционной системой

# Загружаем переменные из файла .env
load_dotenv()

# Создаём бота, получая токен из переменной окружения
bot = Bot(token="8174711542:AAFQXVG0FoO07Wo6kR_f5D7FWkpXMuiP84Y")
dp = Dispatcher()

a="10"
b="6"
c="2"
s=""
u=""
j=""
d=0


class Form(StatesGroup):
    name = State()
    age = State()
    city = State()
    obr = State()
    opyt = State()
    leng = State()
    dost = State()
    what = State()
    nav = State()
    zad1 = State()
    zad2 = State()
    zad3 = State()
    kon = State()


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(
        "🚀 Привет, будущий IT-специалист!\nМеня зовут MTS Education Bot, и я помогу тебе пройти отбор на стажировку в МТС — такую же, после которой другие ребята выходят на зарплату 250 000 ₽!")
    await message.answer("Ответьте на вопросы о себе, рзбитых на 3 раздела, и решите 3 задачи")
    await message.answer("Раздел 1: Личные данные")
    await message.answer("Как вас зовут? (ФИО)")

@dp.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer("Введите дату вашего рождения, в виде(**.**.****):")

@dp.message(Form.age)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Form.city)
    await message.answer("Введите город вашего проживания:")

@dp.message(Form.city)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Form.obr)
    await message.answer("Раздел 2: Образование и опыт")
    await message.answer("Какое у вас образование (школа, колледж, вуз)?")

@dp.message(Form.obr)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(obr=message.text)
    await state.set_state(Form.opyt)
    await message.answer("Есть ли у вас опыт в IT или смежных областях? Опишите кратко.")

@dp.message(Form.opyt)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(opyt=message.text)
    await state.set_state(Form.leng)
    await message.answer("Какие языки программирования вы знаете?")

@dp.message(Form.leng)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(leng=message.text)
    await state.set_state(Form.dost)
    await message.answer("Участвовали ли вы в олимпиадах, хакатонах или других конкурсах?")

@dp.message(Form.dost)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(dost=message.text)
    await state.set_state(Form.what)
    await message.answer("Раздел 3: Мотивация")
    await message.answer("Почему вы хотите участвовать в программе от МТС?")

@dp.message(Form.what)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(what=message.text)
    await state.set_state(Form.nav)
    await message.answer("Какие навыки вы хотите развить во время обучения?")

@dp.message(Form.nav)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(nav=message.text)
    await state.set_state(Form.zad1)
    await message.answer("1 задача\nНайдите количество чисел-палиндромов** от 100 до 200.\nОтвет вводить числом")
    await message.answer("Число-палиндром** — это натуральное число, которое одинаково читается как справа налево, так и слева направо. ")

@dp.message(Form.zad1)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(Form.zad2)
    data = await state.get_data()
    print(data)
    await state.update_data(zad1=message.text)

    await message.answer("2 задача\nДан массив [-2, 1, -3, 4, -1, 2, 1, -5, 4]. Найдите максимальную сумму непрерывного подмассива.\nОтвет вводить числом  ")

@dp.message(Form.zad2)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(zad2=message.text)
    data = await state.get_data()
    print(data)
    await state.set_state(Form.zad3)
    await message.answer("3 задача\nДан массив [2, 3, 1, 1, 4]. Каждый элемент показывает максимальную длину прыжка. Найдите минимальное количество прыжков для достижения конца.\nОтвет вводить числом")


@dp.message(Form.zad3)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(zad3=message.text)
    await state.set_state(Form.kon)
    data = await state.get_data()
    print(data)
    kek = 0
    if a == data['zad1']:
        s="Правильно✅"
        print(s)
        kek+=1
    else:
        s = "Неправильно❌"
        print(s)
    if b == data['zad2']:
        u="Правильно✅"
        print(u)
        kek += 1
    else:
        u = "Неправильно❌"
        print(u)
    if c == data['zad3']:
        j="Правильно✅"
        print(j)
        kek += 1
    else:
        j = "Неправильно❌"
        print(j)

    await message.answer(f"Результаты:\n1 задача: {s}\n2 задача: {u}\n3 задача: {j}")

    if kek == 3:
        await message.answer("✅Вы приняты и приглашены на собседование")
    else:
        await message.answer("❌Вы нам не подходите")

@dp.message(Form.kon)
async def process_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    await state.update_data(kon=message.text)

dp.run_polling(bot)
