secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guessed_number = int(input('Guess: '))
    guess_count += 1
    if guessed_number == secret_number:
        print('You have won')
        break
else:
    print('sorry you have failed')




