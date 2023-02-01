
from create import dp
from aiogram import types

from random import randint

total =200

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}\n Задай количество конфет (/set..)')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('/rules - правила игры\n/set - изменить количество конфет \n/help-помощь')


@dp.message_handler(commands=['rules'])
async def mes_rul(message: types.Message):
    global total
    await message.answer(f'На столе лежит {total} конфет. Играют два игрока,делая ход друг после друга. За один ход можно взять не более 28-ми конфет.'
                         f'Все конфеты оппонента достаются сделавшему последний ход')


@dp.message_handler(commands=['rules'])
async def mes_start(message: types.Message):
    await message.answer('Hello')


@dp.message_handler(commands=['set'])
async def mes_settings(message: types.Message):
    global total
    count = int(message.text.split()[1])
    if count > 29:
        total = count
        await message.answer(f'Количество конфет установлено {total}.\n Сколько возмешь?')
    else:
        await message.answer('Слишком мало конфет')


@dp.message_handler()
async def take(message: types.Message):
    global total
    if message.text.isdigit():
        take = int(message.text)
        if take>28:
            await message.answer('Что так много берешь? Бери меньше 29')
        if take<0:
            await message.answer('Ну... это не серьезно, возьми хотябы одну')
        else:
            temp_total = total-take
        if temp_total == 0:
            await message.answer('Для Бота не осталось конфет.Ты выиграл')
        elif temp_total>28:
            bot_step= randint(1, 28)
            total = temp_total-bot_step
            await message.answer(f'Осталось{temp_total} конфет.Бот берет {bot_step} конфет. На столе осталось {total} конфет')
        else:
            bot_step= randint(1,temp_total+1)
            total = temp_total - bot_step
            if total == 0:
                await message.answer(f'Осталось {temp_total} конфет. Бот берет {bot_step}. Бот выиграл')
            else:
                await message.answer(f'Осталось {temp_total} конфет. Бот берет {bot_step}.На столе осталось{total} конфет')
    else:
        await message.answer('Чтобы вызвать помощь, введите /help')



