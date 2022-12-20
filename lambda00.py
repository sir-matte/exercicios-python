# Desenvolva um programa que leia o seu nome completo e que apresente somente o seu primeiro e último nomes

nome = str(input('Nome: '))
pn = lambda n: nome.split()[0]
un = lambda n: nome.split()[-1]
print(f'Primeiro nome é {pn(nome)}, último nome é {un(nome)}')
