a1 = int(input(Insira a nota da 1a:  ))
a2 = int(input(Insira a nota da 2a:  ))
media = (a1 + a2)/2
if media >= 6:
	print('O aluno foi aprovado!!!! Média: ' + media)
else:
	print('O aluno foi reprovado! D: Média: ' + media)
input()