import random
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from create_bot import dp
from aiogram import types
from keyboards import kb_new, kb_stop
import text
import game
from datetime import datetime

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer('Привет, добро пожаловать в игру Конфетки ', reply_markup=kb_new)

    user = []
    user.append(datetime.now())
    user.append(message.from_user.full_name)
    user = list(map(str, user))
    with open('log.txt', 'a', encoding='utf-8') as data:
        data.write(' | '.join(user)+'\n')


@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer(f'{text.rules}',reply_markup=kb_stop)

@dp.message_handler(commands=['set_total'])
async def mes_set(message: types.Message):
    await message.answer(f'{text.set}')


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):

    if not game.check_game():
        max_total = message.text.split()
        if len(max_total)>1 and max_total[1].isdigit():
            game.set_max_total(int(message.text.split()[1]))
            print(max_total)
            await message.reply(text=f'Максимальное количество конфет установлено {max_total}'
                                     f'\n Нажмите на /start_game', reply_markup=kb_new)
        else:
            await message.reply(text='Данную настройку можно изменить только после окончания партии')



@dp.message_handler(commands=['level'])
async def set_bot_level(message: types.Message):
    await message.answer('Введите уровень сложности:')
    if not game.check_game():
        game.change_level()
        await message.reply(f'Уровень сложности установлен на:{game.get_bot_lvl()}')
    else:
        await message.reply(text='Данную настройку можно изменить только после окончания игры')


@dp.message_handler(commands=['exit_game'])
async def exit_game(message: Message):
    # print("game")
    game.new_game()
    await message.answer('Игра окончена', reply_markup=kb_new)


@dp.message_handler(commands=['start_game'])
async def start_new_game(message: Message):
    if not game.check_game():
        game.set_total_to_max()
        game.new_game()

    if game.check_game():
        toss = random.choice([True, False])
        # print(toss)
        if toss:
            await player_turn(message)
            print(message)
        else:
            await message.answer('Первый ходит бот')
            await bot_turn(message)




@dp.message_handler()
async def take(message: Message):
    name = message.from_user.first_name
    if game.check_game():
        if message.text.isdigit():
            take = int(message.text)
            if (0<take<29) and take <= game.get_total():
                game.take_candies(take)
                if await check_win(message, take, 'player'):
                    return
                await message.answer(f'{name} взял {take} конфет и на столе осталось'
                                     f'{game.get_total()}. Ходит Бот')
                await bot_turn(message)
            else:
                # num = random.randint(1,3)
                await message.answer('Много берешь, возьми от 1 до 28-ми')
        else:
            pass




async def player_turn(message: Message):
    await message.answer(f'{message.from_user.first_name}, твой ход. Сколько возьмешь конфет?', reply_markup=kb_stop)
    # print('Ходи')

async def bot_turn(message: Message):
    total = game.get_total()
    take = 0
    if game.get_bot_lvl()=='Light':
        if total <= 28:
            take = total
        else:
            var = (game.get_total()-29)%28
            take = var if var>0 else random.randint(1,28)
    game.take_candies(take)
    await message.answer(f'Бот взял {take} конфет и их осталось {game.get_total()}', reply_markup=kb_stop)
    # print(game.get_total)
    if await check_win(message, take,'Бот'):
        return
    await player_turn(message)


async def check_win(message, take: int, player: str):
    if game.get_total()<=0:
        if player =='player':
            await message.ansswer(f'{message.from_user.first_name} взял {take} и'
                                  f'оделжал победу')
        else:
            await message.answer(f'Ты проиграл. Бот взял {take} и одержал победу')
        game.new_game()
        return True
    else:
        return False


