# Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final.
# Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário,
# armazenar a nota da prova final e recalcular a média. Caso a nova média seja igual superior a 5,
# apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"

notas = []
recuperacao = []
for c in range(1, 5):
    notas.append(float(input(f'Informe a {c}ª nota: ')))
media = sum(notas) / len(notas)
print(f'\t{notas}\n\tMédia final = {media:.1f}')
if media >= 7:
    print('\t\033[32mAPROVADO!\033[m')
else:
    print('\t\033[31mREPROVADO! Faça a prova final.\033[m')
    media = 0
    for c in range(1, 5):
        recuperacao.append(float(input(f'Informe a {c}ª nota da prova final: ')))
    media = sum(recuperacao) / len(recuperacao)
    print(f'\t{recuperacao}\n\tMédia da prova final = {media:.1f}')
    print('\t\033[32mAPROVADO!\033[m' if media >= 5 else '\t\033[31mREPROVADO!!!\033[m')
