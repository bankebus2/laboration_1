import os
import random

def print_menu():
    os.system('cls')
    print('1 --> Sten')
    print('2 --> Sax')
    print('3 --> Påse')
    print('9 --> Ge upp')

def compare(weapon1, weapon2):
    result = None
    if weapon1 == '1' and weapon2 == '2':       #Sten vs. sax
        result = 1
    elif weapon1 == '1' and weapon2 == '3':     #Sten vs. påse
        result = 2
    elif weapon1 == '2' and weapon2 == '1':     #Sax vs. sten
        result = 2
    elif weapon1 == '2' and weapon2 == '3':     # Sax vs. påse
        result = 1
    elif weapon1 == '3' and weapon2 == '1':     # Påse vs. sten
        result = 1
    elif weapon1 == '3' and weapon2 == '2':     # Påse vs. sax
        result = 2

    #print(f'Result={result}')
    return result

weapons = {
    1: 'Sten',
    2: 'Sax',
    3: 'Påse'
}


while True:
    print_menu()
    player_weapon_of_choice = input("Välj ditt öde: ")
    if player_weapon_of_choice in('1','2','3'):
        computer_weapon_of_choice = random.randint(1,3)
        #print(f'Datorns val: {computer_weapon_of_choice}')
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
        print('\nAvslutar, tack för visat intresse!\n')
        break