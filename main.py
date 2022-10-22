import random

num_digits = 3
max_guess = 10

def get_secret_num():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i]) 
    return str(secret_num)

def get_clues(guess, secret_num):
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')    
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

def main():
    print(''' 
Bagels is a simple logical game. You need to guess a {} - digit.
I will give you a clue:
Pico - one digit is correct, but in the wrong position.
Fermi - one digit is correct and in the right position.
Bagels - no difit is correct. 
For example, if a secret number is 248 and your guess was 843, the clues would be Fermi Pico.
'''.format(num_digits))
    print(f'I have thought up a number. Try to guess it. You have {max_guess} attempts.')
    num_guesses = 1
    secret_num = get_secret_num()
    guess = str(input('type your guess >'))
    result = f'You ran out of guesses. The answer  was {secret_num}'
    result = 'You got it' if guess == secret_num else result
    while num_guesses != max_guess and guess != secret_num:
        clues = get_clues(guess, secret_num)
        print(clues)
        # print(guess, secret_num)
        guess = str(input('type your guess >'))
        result = 'You got it' if guess == secret_num else result
        num_guesses += 1     
    return result

    
if __name__=='__main__':
    answer = 'y'
    while answer != 'n':
        print(main())
        answer = input('Do you want to try it one more time? y/n >')
    print('Thank you! Good luck!')       