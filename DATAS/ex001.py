# Carregue a data atual do computador e, com base na data atual, apresente a data de dois dias no futuro

from datetime import date

dia = date.today().day + 2
df = date.today().replace(day=dia)
print(f'Em dois dias a data será: {df}')
