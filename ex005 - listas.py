# Desenvolva um programa que armazene quatro notas em uma lista e que apresente:
# a média final, a maior nota e a menor nota

lista = []
soma = 0
print('ARMAZENANDO 4 NOTAS')
for c in range(1, 5):
    nota = (float(input(f'Informe a {c}ª nota: ')))
    soma += nota
    lista.append(nota)
print('-' * 20)
média = soma / c
print(f'{lista}\nMédia = {média}\nMaior nota = {max(lista)}\nMenor nota = {min(lista)}')
