# Desenvolva um programa que leia um número qualquer e informe se ele é par ou ímpar

n = int(input('Informe o número: '))
par = lambda x: x % 2 == 0
print(f'O número {n} é ', end='')
if par(n):
    print('par')
else:
    print('ímpar')
