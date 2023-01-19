
# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом


board = [' 'for x in range(10)]
def insert_letter(letter, pos):
    board[pos] = letter

def spaceis_free(pos):
    return board[pos]==' '


def print_board(board):
    print("."*13)
    for i in range(3):
        print('|', board[1+i*3], '|', board[2+i*3], '|', board[3+i*3], '|')
        print('-'*13)

def is_winner(bo,le):
    return (bo[7]==le and bo[8]==le and bo[9]==le) or(bo[4]==le and bo[5]==le and
bo[6]==le) or(bo[1]==le and bo[2]==le and bo[3]==le) or(bo[1]==le and bo[4]==le and
bo[7]==le) or(bo[2]==le and bo[5]==le and bo[8]==le) or(bo[3]==le and bo[6]==le and
bo[9]==le) or(bo[1]==le and bo[5]==le and bo[9]==le) or(bo[3]==le and bo[5]==le and
bo[7]==le)

def player_move():
    run= True
    while run:
        move = input('Введите позицию Х: ')
        try:
            move = int(move)
        except:
            print('Число давай!!')
            continue
        if move > 0 and move < 10:
            if spaceis_free(move):
                run = False
                insert_letter('X', move)
            else:
                print('Место занято')
        else:
            print('Введите число от 1 до 9')


def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x !=0]
    move= 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corners_open=[]
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners_open.append(i)

    if len(corners_open)>0:
        move= select_random(corners_open)
        return move

    if 5 in possible_moves:
        move =5

    edges_open =[]
    for i in possible_moves:
        if i in [2,4,6,8]:
            edges_open.append(i)

    if len(edges_open)>0:
        move =select_random(edges_open)

    return move

def select_random(Ii):
    import random
    ln =len(Ii)
    r= random.randrange(0, ln)
    return Ii[r]

def is_boardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def main():
    print('Добро пожаловать в игру')
    print_board(board)

    while not(is_boardFull(board)):
        if not(is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('O выиграл')
            break

        if not(is_winner(board,'X')):
            move=comp_move()
            if move==0:
                print('Ничья')
            else:
                insert_letter('O', move)
                print('Бот пошел на', move, ':')
                print_board(board)
        else:
            print('X победил!')
            break

    if is_boardFull(board):
        print('Ничья')

while True:
    answer = input('Хотите еще?(Да/Нет)')
    if answer.lower()=='да'or answer.lower == 'да':
        board = [' 'for x in range(10)]
        print(' --------------')
        main()
    else:
        break
