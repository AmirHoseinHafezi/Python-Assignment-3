import random
counter  = 0
while True:
    num = random.randint(1,6)
    counter += num
    if num == 6:
        continue
    else:
        break
print('Total :', counter)