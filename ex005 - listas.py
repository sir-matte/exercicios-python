# Desenvolva um programa que armazene quatro notas em uma lista e que apresente:
# a média final, a maior nota e a menor nota

notas = []
print('ARMAZENANDO 4 NOTAS')
for c in range(1, 5):
    notas.append(float(input(f'Informe a {c}ª nota: ')))

print('-' * 20)
média = sum(notas) / len(notas)
print(f'{notas}\nMédia = {média}\nMaior nota = {max(notas)}\nMenor nota = {min(notas)}')
