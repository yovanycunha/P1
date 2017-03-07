# coding: utf-8
# Imprime Sequencias de Números Inteiros
# (C) 2016, Yovany Cunha / UFCG, Programação 1

num = int(raw_input(''))
entrada = raw_input('')
sequencias = []
lista_seq = []
seq = 1
while entrada != 'fim':
	cont = 0
	entr = entrada.split(" ")
	for i in range(len(entr)):
		entr[i] = int(entr[i])
		if entr[i] > num:
			cont += 1
	if cont > (len(entr)/2):
		sequencias.append(entrada)
		lista_seq.append(seq)
	entrada = raw_input('')
	seq += 1


for i in range(len(sequencias)):
	print 'sequencia %d: %s' % (lista_seq[i],sequencias[i])
