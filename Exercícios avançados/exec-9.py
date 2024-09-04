salario = int(input('Salário inicial:  '))
percent = input('Percentual de reajusteuste:  ')
if ' ' in percent:
	reajuste = percent.replace(" ", "")
if '%' in percent:
	reajuste = percent.replace("%", "")
reajuste = int(percent)
meio = (salario*reajuste)/100
salario += meio
print('')
print('Novo valor:  '+str(salario))
input()