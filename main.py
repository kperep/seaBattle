import random
import os

clear = lambda: os.system('cls')
# Формируем поле для демонстрации пользователю
a = []
for i in range(6):
    a1 = []
    for j in range(6):
        a1.append('O')
    a.append(a1)
a[0][0] = '@'
for i in range(5):
    a[i + 1][0] = i + 1
a[0][1] = 'A'
a[0][2] = 'B'
a[0][3] = 'C'
a[0][4] = 'D'
a[0][5] = 'E'
for i in range(6):
    for j in range(6):
        print(a[i][j], ' ', end='')
    print()

# Формируем поле для компьютера
b = []
for i in range(6):
    b1 = []
    for j in range(6):
        b1.append('O')
    b.append(b1)
b[0][0] = '@'
for i in range(5):
    b[i + 1][0] = i + 1
b[0][1] = 'A'
b[0][2] = 'B'
b[0][3] = 'C'
b[0][4] = 'D'
b[0][5] = 'E'
ships = 0
while ships < 7:
    x = random.randrange(5) + 1
    y = random.randrange(5) + 1
    if b[x][y] != '#':
        b[x][y] = '#'
        ships += 1
dead = 0
ans = input('Стреляй!(А если не хочешь, напиши "Exit")')
while dead < 6 or ans.upper() == 'EXIT':
    y = int(ans[1])
    if ans[0] == 'A':
        x = 1
    elif ans[0] == 'B':
        x = 2
    elif ans[0] == 'C':
        x = 3
    elif ans[0] == 'D':
        x = 4
    elif ans[0] == 'E':
        x = 5
    else:
        print('Ты втираешь мне какую-то дичь!')
    if b[y][x] == '#' or b[y][x] == '$':
        if b[y][x] == '#':
            dead += 1
        a[y][x] = '$'
    else:
        a[y][x] = 'X'
    clear()
    for i in range(6):
        for j in range(6):
            print(a[i][j], ' ', end='')
        print()
    ans = input('Стреляй!(А если не хочешь, напиши "Exit")')
