fenstring = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


slashcount = 0
j = 8


for i in range(9):
    if i == 0:
        print('+',end='')
    else:
        print('---+',end='')
print()
print("|", end=' ')    
for ch in fenstring:
    if ch == ' ':
        print(j)
        break
    if ch == '/':
        print(j)
        j -= 1
        for i in range(9):
            if i == 0:
                print('+',end='')
            else:
                print('---+',end='')
        print()
        print("|", end=' ')
    else:
        if ch.isdigit():
            for l in range(int(ch)):
                print('  | ', end = '')
        else:
            print(ch + ' | ', end='')

for i in range(9):
    if i == 0:
        print('+',end='')
    else:
        print('---+',end='')
print()
print('  ',end='')
for i in range(8):
    ch = 'a'
    ch = chr(ord(ch)+i)
    print(ch, end ='   ')
print()

#fucntion to get turn and castling rights
info_flag = 0
side = -1
KC = QC = kc = qc = 0
for ch in fenstring:
    if info_flag == 1:
        if ch == 'w':
            side = 0
        if ch == 'b':
            side = 1
        if ch == 'K':
            KC=1
        if ch == 'Q':
            QC=1
        if ch == 'k':
            kc=1
        if ch == 'q':
            qc=1
    
    if ch == ' ' and info_flag == 0:
        info_flag = 1
    
print(side, KC,QC,kc,qc)