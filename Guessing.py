import random

guessestaken=0
print('What is your name?')
myName=input()
number=random.randint(1,20)
print('Well, '+ myName + ', am thinking of a number between 1 to 20. but yo have up to 6 tries before you fail')

while guessestaken <= 6:
    print('Take a guess:')
    guess = int(input())
    guessestaken = guessestaken + 1

    if guess < number:
        print('Number too low')
    if guess > number:
        print('Number  too high')

    if guess == number:
        print('Weldone ' +myName+ ' you have guessed right in ', guessestaken, ' times')
        break
    #if guess == number:
            # print('Weldone you have guessed right in ', guessestaken, ' times')
while guessestaken > 6:
    if guess != number:
            print('Sorry ' +myName+ ' the number I was thinking of was', number)
            break

