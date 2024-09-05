m = int(input('Quantas maçãs deseja comprar?  '))
if m < 12:
	pi = 1.30
else:
	pi = 1
pt = m * pi
print('')
print('Preço total:   R$ ' + str(pt))
input()