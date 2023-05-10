import random

import Message

def letter2num(letter):
    return ord(letter.lower()) - 96

def num2letter(num):
    return chr(num + 96)

def trainer():
    global correct, incorrect, max_combo
    test_n = Message.test_n
    correct = 0
    incorrect = 0
    combo = 0
    max_combo = 0

    Message.print_green(f'\nstarting...')
    if Message.test_type == 'matchNumber':
        for n in range(test_n):
            randInt = random.randint(1, 26)
            user_answer = input(f'{randInt}= ').lower()
            test_answer = num2letter(randInt)

            if test_answer == user_answer:
                correct += 1
                combo += 1
                max_combo = combo if combo > max_combo else max_combo
                if combo % 5 == 0:
                    Message.print_green(f'{combo} combo!')
            else:
                Message.print_red(f'correct answer is: {test_answer.upper()}')
                incorrect += 1
                combo = 0

    elif Message.test_type == 'matchAlphabet':
        for n in range(test_n):
            randAlp = num2letter(random.randint(1, 26))
            user_answer = int(input(f'{randAlp.upper()}= '))
            test_answer = letter2num(randAlp)

            if test_answer == user_answer:
                correct += 1
                combo += 1
                max_combo = combo if combo > max_combo else max_combo
                if combo % 5 == 0:
                    Message.print_green(f'{combo} combo!')
            else:
                Message.print_red(f'correct answer is: {test_answer}')
                incorrect += 1
                combo = 0
    
    elif Message.test_type == 'math':
        for n in range(test_n):
            randInt = random.randint(1, 26) #8
            randSign = random.choice([0, 1]) #0
            randSign = '+' if randSign == 0 else '-' #'+'
            randAlp = num2letter(random.randint(1, 26)) #S
            user_answer = input(f'{randAlp.upper()}{randSign}{randInt}= ').lower()
            if randSign == '+':
                test_answer = letter2num(randAlp) + randInt
                if test_answer > 26:
                    test_answer = test_answer - 26
            elif randSign == '-':
                test_answer = letter2num(randAlp) - randInt
                if test_answer < 1:
                    test_answer = test_answer + 26
            test_answer = num2letter(test_answer)
            
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

    return correct, incorrect, max_combo

    