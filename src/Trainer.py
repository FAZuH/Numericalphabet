import random

import Message

def letter2num(letter):
    return ord(letter.lower()) - 96

def num2letter(num):
    return chr(num + 96)

def check_answer(user_answer, test_answer):
    global correct, incorrect, max_combo
    if user_answer == test_answer:
        correct += 1
        combo += 1
        max_combo = combo if combo > max_combo else max_combo
        if combo % 5 == 0:
            Message.print_green(f'{combo} combo!')
    else:
        Message.print_red(f'correct answer is: {test_answer}')
        incorrect += 1
        combo = 0

def trainer():
    global correct, incorrect, max_combo
    test_n = Message.test_n
    correct = 0
    incorrect = 0
    combo = 0
    max_combo = 0

    Message.print_green(f'\nstarting...')
    match Message.test_type:
        case 'matchNumber':
            for n in range(test_n):
                randInt = random.randint(1, 26)
                user_answer = input(f'{randInt}= ').upper()
                test_answer = num2letter(randInt).upper()
                check_answer(user_answer, test_answer)

        case 'matchAlphabet':
            for n in range(test_n):
                randAlp = num2letter(random.randint(1, 26))
                user_answer = int(input(f'{randAlp.upper()}= '))
                test_answer = letter2num(randAlp)
                check_answer(user_answer, test_answer)
    
        case 'math':
            for n in range(test_n):
                randInt = random.randint(1, 26)
                randSign = random.choice([0, 1])
                randSign = '+' if randSign == 0 else '-'
                randAlp = num2letter(random.randint(1, 26))
                user_answer = input(f'{randAlp.upper()}{randSign}{randInt}= ').lower()
                match randSign:
                    case '+':
                        test_answer = letter2num(randAlp) + randInt
                        if test_answer > 26:
                            test_answer = test_answer - 26
                    case '-':
                        test_answer = letter2num(randAlp) - randInt
                        if test_answer < 1:
                            test_answer = test_answer + 26
                test_answer = num2letter(test_answer) 
                check_answer(user_answer, test_answer)

    return correct, incorrect, max_combo
