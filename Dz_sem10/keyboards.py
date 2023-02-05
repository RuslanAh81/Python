from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_new = ReplyKeyboardMarkup(resize_keyboard=True)
kb_stop = ReplyKeyboardMarkup(resize_keyboard=True)

btn_new_game = KeyboardButton(text='/start_game')
btn_help = KeyboardButton(text='/help')
btn_exit_game = KeyboardButton('/exit_Game')
btn_level = KeyboardButton('/level')
btn_set = KeyboardButton('/set_total')


kb_new.add(btn_set, btn_new_game, btn_help)
kb_stop.add(btn_exit_game, btn_level)