import os
import random

def print_menu():
    print()
    print('1 --> Sten')
    print('2 --> Sax')
    print('3 --> Påse')
    print('9 --> Ge upp')
    print()

def compare(weapon1, weapon2):
    result = 0
    if weapon1 == '1' and weapon2 == '2':       # Rock vs. scissors
        result = 1
    elif weapon1 == '1' and weapon2 == '3':     # Rock vs. paper
        result = 2
    elif weapon1 == '2' and weapon2 == '1':     # Scissors vs. rock
        result = 2
    elif weapon1 == '2' and weapon2 == '3':     # Scissors vs. paper
        result = 1
    elif weapon1 == '3' and weapon2 == '1':     # Paper vs. rock
        result = 1
    elif weapon1 == '3' and weapon2 == '2':     # Paper vs. scissors
        result = 2

    return result

weapons = {
    1: 'Sten',
    2: 'Sax',
    3: 'Påse'
}


while True:
    os.system('cls')
    print_menu()
    player_weapon_of_choice = input("Välj ditt öde: ")
    os.system('cls')
    if player_weapon_of_choice in('1','2','3'):
        computer_weapon_of_choice = random.randint(1,3)
        result = compare(player_weapon_of_choice, str(computer_weapon_of_choice))
        if result == 1:
            print('\nDu vann!')
        elif result == 2:
            print('\nDu förlorade...')
        else:
            print('\nOavgjort')

        print(f'\nDitt vapen: {weapons[int(player_weapon_of_choice)]}\nDatorns vapen: {weapons[int(computer_weapon_of_choice)]}')
        input('\nTryck Enter för en ny runda')

    elif player_weapon_of_choice == '9':
        print('\nAvslutar...\n')
        break