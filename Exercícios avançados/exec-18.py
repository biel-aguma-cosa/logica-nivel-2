from datetime import datetime
niver = int(input('Insira seu ano de nascimento:  '))
idade = datetime.now().year - niver
if idade >= 16:
	print('Você pode/poderá votar este ano')
else:
	print('Você não pode votar este ano')

input()