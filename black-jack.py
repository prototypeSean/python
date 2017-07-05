# blackjack:
 # 第一章棄掉
#     dealer and player 各發一張明牌。
#     dealer 發一張暗牌, plary 發一張明牌。
#     dealer先看自己是不是blackjack組合，如果是就結束這局。 dealer wins
#     if dealer明牌是Ace, 詢問player要不要insurance,就是賭另一張是不是blackjack。
#     如果是，這局結束，insurance double送。若不是，收走Insurance。
#     玩家有blackjack->3:2! get pay 15 if bet 10
#     loop
#         詢問玩家的動作。
#         hit:繼續家牌
#         stand:不加牌 (1 player的時候 = 掀牌push)
#         dealer翻底牌，不夠17要再加抽一張，看看結果。
#
#         反正都不能 少於 17! 超過21就bustted!
import random
from functools import reduce
dealedCards = [] #已發出去的牌
cardDisplay = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
class Player(object):
    def __init__(self):
        self.hand = []
        self.total = 0
        self.money = 100
        self.bustted = False
        self.point = 0

    def get_card(self, card):
        self.hand.append(card)

    def cal_points(self):
        total_point = 0
        has_ace = 0
        for card in self.hand:
            if card == 'J' or card == 'Q' or card == 'K':
                total_point += 10
            elif card == 'A':
                has_ace += 1
            else:
                total_point += int(card)

        if total_point <= 11 and has_ace > 0:
            total_point += 11 + (has_ace - 1)
        elif total_point > 11 and has_ace > 0:
            total_point += has_ace

        return total_point


# 抽牌
# return 牌額
def draw():
    while True:
        suit = random.randint(1,4)
        number = random.randint(1,13)
        card = str(suit) + str(number)
        if card not in cardDisplay:
            cardDisplay.append(card)
            break
    return cardDisplay[number-1]

# def print_card(card):
#     for c in card:
#         print('+------+')
#         print('| %s    |' % c)
#         print('|      |' )
#         print('|    %s |' % c)
#         print('+------+')

def playGame():
    dealer = Player()
    you = Player()

    while True: #遊戲開始的 while
        print('--- new game ---')
        while True:
            bet = int(input('Enter your bet (you have $%d):' % you.money))
            if bet > you.money:
                print('Wake up, your money is not enough.')
                continue
            elif bet <= 0 :
                print('Not accepted.')
            else:
                break
        #發牌
        dealer.get_card(draw())
        you.get_card(draw())
        dealer.get_card(draw())
        you.get_card(draw())
        # you.hand = ['A','J']
        # dealer.hand = ['5','A']
        #dealer.check_status()
        #you.check_status()

        #print 牌
        # print_card(dealer.hand[0])
        print('dealer: ' ,dealer.hand[0])
        # print_card(you.hand)
        print('you: ', you.hand)
        if dealer.cal_points() > 21 :
            print('Dealer bustted ! You win')
            you.money += bet
            break
            #bustted
            #break
        elif you.cal_points() > 21 :
            print('Sorry ... You bustted !')
            you.money -= bet

        elif you.cal_points() == 21:
            print('Blackjack ! You win !')
            you.money += bet * 3/2

        else:
            ask = True

            #dealer有沒有ace
            if dealer.hand[0] == 'A':
                #insurance
                print('Dealer got an Ace !')
                while True:
                    insurance = int(input('Enter your insurance: (you have $%d): ' % (you.money-bet)))
                    if insurance > you.money-bet:
                        print('Wake up, your money is not enough.')
                        continue
                    elif insurance < 0 :
                        print('Not accepted.')
                    else:
                        break

                if dealer.cal_points() == 21:
                    print('-----------')
                    print('dealer: ' ,dealer.hand)
                    print('you: ', you.hand)
                    print('It is blackjack!')
                    you.money = you.money - bet + insurance
                    ask = False
                    #insurance * 5/3
                    #bet gone
                else:
                    print('-----------')
                    print('dealer: ' ,dealer.hand)
                    print('you: ', you.hand)
                    print('Not blackjack, let\'s continue..')
                    you.money = you.money - insurance
                    #insurance gone

            while ask: #發牌的 while
                print(' ')
                choice = input('Now you want hit or stand?(h/s) ').lower()
                #ask hit or stand
                if choice == 'h':
                    #hit
                    you.get_card(draw())
                    #發牌
                    print('-----------')
                    print('dealer: ' ,dealer.hand)
                    print('you: ', you.hand)
                    #print 牌
                    if you.cal_points() > 21:
                        print('Sorry ... You bustted !')
                        you.money -= bet
                        break

                    elif you.cal_points() == 21:
                        print('You win !')
                        you.money += bet
                        break
                        #bustted
                        #break
                elif choice == 's': #stand
                    if you.cal_points() < 17:
                        print('You must hit!')
                        continue

                    while dealer.cal_points() < 17:
                        dealer.get_card(draw())

                    print('-----------')
                    print('dealer: ' ,dealer.hand)
                    print('you: ', you.hand)

                    #print 牌
                    #看結果
                    if dealer.cal_points() > 21 :
                        print('Dealer bustted ! You win')
                        you.money += bet
                        # break
                        #bustted
                        #break
                    else:
                        if you.cal_points() > dealer.cal_points():
                            print('Your point is greater, you win.')
                            you.money += bet
                        elif you.cal_points() < dealer.cal_points():
                            print('Dealer\'s point is greater, you lose.')
                            you.money -= bet
                        else :
                            print('Tie!')
                    break


                    #宣布贏家
                    #計算獲利
                    #break
        print('-----------')
        print('Your money : $%d' % you.money)
        ans = input('Wanna play again? (y/n)').lower()
        #ask game again?
        if ans == 'y':
            dealer.hand = []
            you.hand = []
            continue
        elif ans == 'n':
            break
        else:
            print('welcome to endless ...')

# game start!

playGame()
