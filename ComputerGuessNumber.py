import random

small_number = 0

big_number = 99

num = random.randint(small_number, big_number)

while True:
    print('is it', num, '? (Yes/No)')

    ans = input()
    if ans == 'Yes' :
        print('yay i won')
        break
    elif ans == 'No' :
        pos = input('is it bigger or smaller: ')

        if pos == 'bigger':
            small_number = num + 1
            num = random.randint(small_number, big_number)
        elif pos == 'smaller':
            b_num = num - 1
            num = random.randint(small_number, big_number)
        else:
            print('answer should bigger or smaller')
            continue

    else:
        print('answer should be between yes or no')
        continue