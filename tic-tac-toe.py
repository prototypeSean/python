def drawBoard(place_list):
    print(' ')
    print(' %s | %s | %s ' %(place_list[7], place_list[8], place_list[9]))
    print('---+---+---')
    print(' %s | %s | %s ' %(place_list[4], place_list[5], place_list[6]))
    print('---+---+---')
    print(' %s | %s | %s ' %(place_list[1], place_list[2], place_list[3]))

def init():
    global k, rounds, place_list
    #k = True
    rounds = 0
    #place_list = ['','1','2','3','4','5','6','7','8','9']
    place_list = [' ']*10
    drawBoard(place_list)


def check_winner(play_list):
    tmp = play_list[5]
    if tmp != ' ':
        if play_list[2] == tmp and play_list[8] == tmp:
            return tmp
        if play_list[4] == tmp and play_list[6] == tmp:
            return tmp
        if play_list[3] == tmp and play_list[7] == tmp:
            return tmp
        if play_list[1] == tmp and play_list[9] == tmp:
            return tmp
    tmp = play_list[7]
    if tmp!=' ':
        if play_list[8] == tmp and play_list[9] == tmp:
            return tmp
        if play_list[1] == tmp and play_list[4] == tmp:
            return tmp
    tmp = play_list[3]
    if tmp!= ' ':
        if play_list[6] == tmp and play_list[9] == tmp:
            return tmp
        if play_list[1] == tmp and play_list[2] == tmp:
            return tmp
    return False

print('Before we start, we need 2 players.')
print('Press the number to place your O or X.')
key = input('press any to start ... ')
if key != '':
    o = True;
while(o):
    init()
    print(' ')
    print('****************')
    print('New game start!')
    while True:
        print(' ')
        print('player %d , please press the number...' %(rounds%2 + 1))
        number = int(input())
        if rounds%2 == 1:
            ch = 'o'
        else:
            ch = 'x'
        if place_list[number] == 'o' or place_list[number] == 'x':
            print('Can not place here!')
        else:
            place_list[number] = ch
            drawBoard(place_list)
            if rounds > 3 :
                end = check_winner(place_list)
                if end!=False :
                    print('------------')
                    print(' player%d won!' %(rounds%2 + 1))
                    print('------------')
                    d = input('Restart?')
                    if d == 'y':
                        break
                    else:
                        o=False
                        break
                if len(set(place_list[1::]))==2:
                    print('------------')
                    print(' A draw!')
                    print('------------')
                    d = input('Restart?')
                    if d == 'y':
                        break
                    else:
                        o=False
                        break
            rounds += 1
