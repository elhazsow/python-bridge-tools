import time
import os


def program_welcome():
    print('Bridge Tools\n')


def main_loop():
    try:
        user_input = ''
        while user_input.lower() != 'q':
            program_welcome()
            print()
            print('1. Calculate Bridge Grades')
            print('2. Retrieve Design Response Spectra')
            print()
            print('Type \'q\' to exit the program')
            user_input = input('>> ')
            handle_user_input(user_input)
    except ValueError as e:
        print('n' + e.args[0])
        time.sleep(2)  # keep window open long enough to see error message


def handle_user_input(user_input):
    if user_input == '1':
        clear_console()
        pass
    elif user_input == '2':
        clear_console()
        pass
    elif user_input == 'q':
        pass
    else:
        print('\nPlease select a valid option or type \'q\' to exit\n')


def clear_console():
    if os.name == 'nt':  # windows
        os.system('cls')
    else:  # mac or linux
        os.system('clear')


if __name__ == '__main__':
    main_loop()
