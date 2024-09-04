from datetime import datetime
print('Insira sua data de nascimento:')
dia = int(input('Dia:  '))
mes = input('Mês:  ')
ano = int(input('Ano:  '))
months = 0
eita = False
for meses in ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']:
	months += 1
	if mes == meses:
		eita = True
if eita == True:
    mes = months
else:
    mes = int(mes)       
atual = (int(datetime.now().day)) + (int(datetime.now().month)*30) + (int(datetime.now().year)*365)
resultado = atual - (dia + mes*30 + ano*365)

print("Você tem "+str(resultado)+" dias de vida!!!")
input()