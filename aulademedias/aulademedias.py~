#coding: utf-8
# Aula de Medias
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

num = float(raw_input(''))
soma = num
numero = []
numero.append(num)
while soma < 100:
	num = float(raw_input(''))
	numero.append(num)
	soma += num

media = soma/len(numero)

maior = []
menor = []
pos_maior = []
pos_menor = []

for i in range(len(numero)):
	if numero[i] > media:
		maior.append(numero[i])
		pos_maior.append(i + 1)
	elif numero[i] < media:
		menor.append(numero[i])
		pos_menor.append(i + 1)

print 'Quantidade de números lidos: %d' % len(numero)
print 'Soma dos números lidos: %.2f' % soma
print 'Média = %.2f\n' % media

print 'Abaixo da média'
for i in range(len(menor)):
	print '%.2f (%do)' % (menor[i],pos_menor[i])
print 
print 'Acima da média'
for i in range(len(maior)):
	print '%.2f (%do)' % (maior[i],pos_maior[i])
