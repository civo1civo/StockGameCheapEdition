# Stock game made by Civo, idea from HumbleCaktus, based on Boerderijspel from Robbe Vercammen

import random

#variables
money = 15
maximumStocks = 50
ownedStocks = 0
amountStocks = 0
year = 2021
priceStocks = random.randint(1, 5)
game = True
Firewall = 'no'
info = 'show'

#loop of the game
print('Stock Game''\n')
while game == True:
    while info == 'show':
        info = 'gone'
        ownedStocks = int(amountStocks)
        print('Year:' + str(year) + ' /// Money:€' + str(money) + ' /// Owned Stocks:' + str(ownedStocks) + '/' +
              str(maximumStocks) + ' /// Price Stocks: €' + str(priceStocks) + ' /// Amount Stocks:' +
              str(amountStocks) +'\n')
        while info == 'gone':
            print('Commands: buyStocks, sellStocks, buyFirewall, coinflip, showInfo')
            x = input()
            if x == str('sellStocks'):
                sellPrice = random.randint(1, 8)
                theft = random.randint(1, 7)
                if Firewall == 'yes':
                    theft = 0
                if int(theft) == 1:
                    money = int(money) / 2
                    print('You have been hacked, half of your money is gone.')
                if int(theft) == 2:
                    print('The stocks plummeted, you lost all the money.')
                    sellPrice = 0
                profit = int(sellPrice) * int(amountStocks)
                if year < 2031 :
                    print('\nThe sell price this year is €' + str(sellPrice) + '. You had ' + str(amountStocks) +
                      ' stocks, so you get €' + str(profit) + '. Your yearly tax is €5.')
                    money = int(money) + int(profit) - 5
                if year >= 2031:
                    print('\nThe sell price this year is €' + str(sellPrice) + '. You had ' + str(amountStocks) +
                      ' stocks, so you get €' + str(profit) + '. Your yearly tax is €10.')
                    money = int(money) + int(profit) - 10
                print('You now have €' + str(money) + '.')
                if int(money) < 0:
                    print('You lost all your money.')
                    info = 0
                    game = False
                else:
                    amountStocks = 0
                    year += 1
                    priceStocks = random.randint(1, 5)
                    info = 'show'
            elif x == str('buyStocks'):
                print('How many stocks do you want to buy? (number)')
                x = input()
                if int(x) < 0:
                    print('The minimum amount is 0.')
                elif int(x) + int(ownedStocks) > int(maximumStocks):
                    print('The maximum amount of stocks you can own is 50. ' + 'You own ' + str(ownedStocks) + ' stocks.')
                elif int(x) * int(priceStocks) <= int(money):
                    print('You bought ' + str(x) + ' stocks.')
                    money = int(money) - int(priceStocks) * int(x)
                    amountStocks = int(amountStocks) + int(x)
                    info = 'show'
                else:
                    print('You do not have enough money to buy ' + str(x) +' stocks.')
            elif x == str('buyFirewall'):
                print('Do you want to buy a firewall for €150? Type yes or no')
                x = input()
                if x == 'yes':
                    if 150 <= int(money):
                        money = int(money) - 150
                        Firewall = 'yes'
                        print('You are now secured against hackers.')
                        info = 'show'
                    else:
                        print('You do not have enough money.')
                        info = 'show'
                else:
                    info = 'show'
            elif x == str('showInfo'):
                print('\nInfo:'+'\nbuyStocks = By typing this command you can buy stocks.Fill in a number, if you fill in somthing that is not a number, the game will crash.'+
      '\nsellStocks = By typing this command, you will go to a new year and sell your stocks at a random price.'
      '\nbuyFirewall = By typing this command, you will have the option to buy a firewall that protects you from getting hacked.'+'\n')
            elif x == str('coinflip'):
                print('Do you want to go all in and see if you can double your money? Type yes or no'+'\nNote: You can lose all of it.')
                x = input()
                if x == 'yes':
                    print('Heads or Tails?')
                    x = input()
                    if x == 'Heads':
                        Heads = random.randint(1 , 2)
                        print('\n' + str(Heads) + '\n')
                        if Heads == 1:
                            money = int(money) * 2
                            info = 'show'
                        elif Heads == 2:
                            money = 0
                            print('You lost all your money.')
                            if money == '0' and ownedStocks == '0' :
                                info = 0
                                game = False
                            else:
                                info = 'show'
                    elif x == 'Tails':
                        Tails = random.randint(1 , 2)
                        print('\n' + str(Tails) + '\n')
                        if Tails == 2:
                            money = int(money) * 2
                            info = 'show'
                        elif Tails == 1:
                            money = 0
                            print('You lost all your money.')
                            if money == '0' and ownedStocks == '0' :
                                info = 0
                                game = False
                            else:
                                info = 'show'
                        
                            
                            
                        