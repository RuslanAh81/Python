
from aiogram import types
max_total =150
total = max_total
game = False

bot_level ='Light'

def set_total_to_max():
    global total
    global max_total
    total = max_total

def set_max_total(value: int):
    global max_total
    max_total=value

def get_total():
    global total
    return total



def take_candies(take: int):
    global total
    total-=take


def new_game():
    global game
    global total
    if game:
        total = max_total
        game = False
    else:
        game = True


def check_game():
    global game
    return game


# def check_win(massage: types.Message, player: str, take: int):
#     pass


def change_level():
    global bot_level
    if bot_level == 'Light':
        bot_level = 'Hard'
    else:
        bot_level = 'Light'


def get_bot_lvl():
    global bot_level
    return bot_level



