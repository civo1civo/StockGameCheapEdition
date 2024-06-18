# Stock game made by Civo, idea from HumbleCaktus, based on Boerderijspel from Robbe Vercammen
# updated in 2024 AI was used to clean it up

import random


def display_info(year, money, owned_stocks, maximum_stocks, price_stocks, amount_stocks):
    print(
        f'Year: {year} /// Money: €{money} /// Owned Stocks: {owned_stocks}/{maximum_stocks} /// Price Stocks: €{price_stocks} /// Amount Stocks: {amount_stocks}\n')


def sell_stocks(year, amount_stocks, money, firewall):
    sell_price = random.randint(1, 8)
    theft = random.randint(1, 7)

    if firewall:
        theft = 0
    if theft == 1:
        money /= 2
        print('\nYou have been hacked, half of your money is gone.')
    elif theft == 2:
        print('\nThe stocks plummeted, you lost all the money.')
        sell_price = 0

    profit = sell_price * amount_stocks
    tax = 5 if year < 2031 else 10

    print(
        f'\nThe sell price this year is €{sell_price}. You had {amount_stocks} stocks, so you get €{profit}. Your yearly tax is €{tax}.')
    money += profit - tax
    print(f'You now have €{money}.\n')

    if money < 0:
        print('You lost all your money.\nThank you for playing!')
        return money, 0, False

    return money, 0, True


def buy_stocks(price_stocks, money, amount_stocks, maximum_stocks):
    print('How many stocks do you want to buy? (number or "max" to buy maximum stocks)')
    x = input().strip().lower()
    if x == 'max':
        x = (money // price_stocks)
        if x + amount_stocks > maximum_stocks:
            x = maximum_stocks - amount_stocks
    elif not x.isdigit():
        print('Please enter a valid number.')
        return money, amount_stocks, True

    x = int(x)
    if x < 0:
        print('The minimum amount is 0.\n')
    elif x + amount_stocks > maximum_stocks:
        print(f'The maximum amount of stocks you can own is {maximum_stocks}. You own {amount_stocks} stocks.')
    elif x * price_stocks <= money:
        print(f'You bought {x} stocks.\n')
        money -= price_stocks * x
        amount_stocks += x
    else:
        print(f'You do not have enough money to buy {x} stocks.')

    return money, amount_stocks, True


def buy_firewall(money):
    print('\nDo you want to buy a firewall for €150? Type yes or no.')
    x = input().lower()
    if x == 'yes':
        if money >= 150:
            money -= 150
            print('You are now secured against hackers.')
            return money, True, True
        else:
            print('You do not have enough money.')

    return money, False, True


def show_commands():
    print('Commands: buyStocks, sellStocks, buyFirewall, coinFlip, showInfo')


def show_info():
    print(
        '\nInfo:\nbuyStocks = Buy stocks.\nsellStocks = Sell your stocks at a random price and advance to the next year.\nbuyFirewall = Buy a firewall to protect against hackers.\ncoinFlip = Double or lose all your money with a coin flip.')


def coin_flip(money, amount_stocks):
    print(
        'Do you want to go all in and see if you can double your money? Type yes or no\nNote: You can lose all of it.')
    x = input().lower()
    if x == 'yes':
        print('\nHeads or Tails?')
        x = input().capitalize()
        if x in ['Heads', 'Tails']:
            result = random.choice(['Heads', 'Tails'])
            print(f'\n{result}\n')
            if result == x:
                money *= 2
                print(f'You won, you now have €{money}.\n')
            else:
                money = 0
                print('You lost all your money.\n')
                if amount_stocks == 0:
                    print('\nThank you for playing!')
                    return money, amount_stocks, False
        else:
            print('Invalid choice. Please enter Heads or Tails.')
    return money, amount_stocks, True


def handle_command(command, game_state):
    command_functions = {
        'sellstocks': lambda: sell_stocks(game_state['year'], game_state['amount_stocks'], game_state['money'],
                                          game_state['firewall']),
        'buystocks': lambda: buy_stocks(game_state['price_stocks'], game_state['money'], game_state['amount_stocks'],
                                        game_state['maximum_stocks']),
        'buyfirewall': lambda: buy_firewall(game_state['money']),
        'coinflip': lambda: coin_flip(game_state['money'], game_state['amount_stocks']),
        'showinfo': lambda: (show_info(), game_state['money'], game_state['amount_stocks'], game_state['game']),
    }

    if command in command_functions:
        return command_functions[command]()
    else:
        print('Invalid command. Please try again.')
        return game_state['money'], game_state['amount_stocks'], game_state['game']


# Main game loop
def main():
    game_state = {
        'money': 15,
        'maximum_stocks': 50,
        'amount_stocks': 0,
        'year': 2021,
        'price_stocks': random.randint(1, 5),
        'game': True,
        'firewall': False
    }

    print('Stock Game\n')

    while game_state['game']:
        display_info(game_state['year'], game_state['money'], game_state['amount_stocks'], game_state['maximum_stocks'],
                     game_state['price_stocks'], game_state['amount_stocks'])
        show_commands()
        command = input().lower()

        game_state['money'], game_state['amount_stocks'], game_state['game'] = handle_command(command, game_state)

        if command == 'sellstocks' and game_state['game']:
            game_state['year'] += 1
            game_state['price_stocks'] = random.randint(1, 5)


if __name__ == "__main__":
    main()

                        
