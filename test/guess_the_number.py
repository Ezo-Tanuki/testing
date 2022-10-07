import random
#Init.
rdm_num = random.randint(1, 100)

while True:
    guess = int(input('Guess the number: '))
    if guess > rdm_num:
        print('The number is too high\n\n')
        continue

    if guess < rdm_num:
        print('The number is too low\n\n')
        continue


    print('The number is correct!')
    break 