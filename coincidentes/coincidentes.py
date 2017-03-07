# coding: utf-8
# Coincidentes
# (C) 2016, Yovany Cunha / UFCG, Programação 1

nome1 = raw_input('')
nome2 = raw_input('')
letras = []
posicao = []
percent_letras = 0

if len(nome1) > len(nome2):
	for l in range(0,len(nome2)):
		if nome1[l] == nome2[l]:
			letras.append(nome1[l])
			posicao.append(l)
	percent_letra = (100*len(posicao))/len(nome2)
	print 'Letras coincidentes'
	for i in range(len(letras)-1):
		print "'%s' na posição %d" % (letras[i],posicao[i])
	percent_letras = 100*len(letras)/(len(nome1) + len(nome2))
	print 'Total de letras coincidentes: %d' % percent_letras
else:
	for l in range(0,len(nome1)):
		if nome1[l] == nome2[l]:
			letras.append(nome1[l])
			posicao.append(l)
	percent_letra = (100*len(posicao))/len(nome2)
	print 'Letras coincidentes'
	for i in range(len(letras)-1):
		print "'%s' na posição %d" % (letras[i],posicao[i])
	percent_letras = 100*len(letras)/(len(nome1) + len(nome2))
	print 'Total de letras coincidentes: %d' % percent_letras
