# coding: utf-8
# No Limite
# (C) 2016, Yovany Cunha / UFCG, Programação 1




medias = []
contador = 1
cont = 0
soma = 0.0
media = 0.0

valor = raw_input('')

while valor != '-':
	valor = float(valor)
	soma += valor
	media = soma / contador
	medias.append(media)
	contador += 1
	valor = raw_input('')
	
	
limite = float(raw_input(''))

while cont != len(medias):
	if medias[cont] > limite:
		break
	cont += 1

if cont == len(medias):
	print 'limite não alcançado'
else:
	print 'media = %.1f' % medias[cont]
	print 'num = %d' % (cont + 1)
