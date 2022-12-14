# Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar

def PouI(num):
    try:
        n = int(input(num))
        if n % 2 == 0:
            return f'O número {n} é par'
        else:
            return f'O número {n} é ímpar'
    except ValueError:
        print('\033[31mDigite um número inteiro válido\033[m')
        return PouI(num)


num = PouI('Informe um número inteiro: ')
print(num)
