def collatz(number):
    if number % 2 == 0:
        return  number // 2


    else:
       return  3 * number + 1

try:
    number = int(input("digite um numero inteiro"))
    number = collatz(number)
except ValueError:
    print('Numero nao letras')
    number = int(input("digite um numero inteiro"))
    number = collatz(number)


while number != 1:
    print(number)
    number = collatz(number)

if number == 1:
    print(number)


#Em Construcao !!!!