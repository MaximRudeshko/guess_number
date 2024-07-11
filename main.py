from random import randint

number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True: 
    guess = int(input('введите число'))

    if guess > number:
        print('Загаданное число меньше')

    if guess < number:
        print('Загаданное число больше')

    if guess == number:
        break

print('Отличная новость вы угадали')