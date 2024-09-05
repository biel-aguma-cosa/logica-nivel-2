inicio = input('Insira a hora de início no formato 24h:  ')
if 'h' in inicio:
	inicio.replace('h','')
inicio = int(inicio)
fim = input('Insira a hora de fim no formato 24h:  ')
if 'h' in fim:
	fim.replace('h','')
fim = int(fim)
if fim > inicio:
	duracao = fim - inicio
if fim <= inicio:
	duracao = 24 - (inicio - fim)
if (duracao > 24) or (duracao < 0):
	print(str(duracao) + 'h é uma duração inválida')
else:
	print('A partida de xadrez durou ' + str(duracao) + ' horas')
input()