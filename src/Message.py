from colorama import Fore, Style

import Trainer

def print_red(message):
    print(Fore.LIGHTRED_EX + message + Style.RESET_ALL)

def print_green(message):
    print(Fore.LIGHTGREEN_EX + message + Style.RESET_ALL)

def print_blue(message):
    print(Fore.LIGHTBLUE_EX + message + Style.RESET_ALL)


def user_input():
    global test_n, test_type
    while True:
        print_blue("\nEnter test type, enter 'exit' to exit:")
        test_type = input()
        if str(test_type).lower() == 'exit':
            exit()
        elif test_type not in ['math', 'matchNumber', 'matchAlphabet']:
            print_red("Invalid test type. Enter 'math', 'matchNumber' or 'matchAlphabet'")
            continue
        break

    print_blue("\nEnter number of tests:")
    test_n = int(input())

def result():
    print_blue('\nResults:')
    print_green(f'correct: {Trainer.correct}')
    print_green(f'incorrect: {Trainer.incorrect}')
    print_green(f'max combo: {Trainer.max_combo}')

