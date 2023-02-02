
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
    name = message.from_user.first_name
    global total
    if message.text.isdigit():
        take = int(message.text)

        temp_total = total - take
        if (0 < take < 29) and take <= total:
            await message.answer(f'{name} Взял {take} конфет и на столе осталось {temp_total} конфет. Ходит Бот')
            if temp_total <= 0:
                await message.answer(f'Боту не осталось конфет {name} выиграл')
            elif temp_total > 28:
                bot_turn = randint(1, 28)
                total = temp_total - bot_turn
                await message.answer(f'Бот взял {bot_turn} конфет осталось {total} конфет\n Сколько возьмешь?')
            else:
                bot_turn = randint(1, temp_total)
                total = temp_total - bot_turn
                await message.answer(f'Бот взял {bot_turn} конфет осталось {total} конфет\n Сколько возьмешь?')
                if total <= 0:
                    await message.answer('Бот победил')
        else:
            await message.answer('Что то ты много взял!!')




