#coding: utf-8
# Mais Ocorrências de um Caractere
# (C) 2016, Yovany Cunha/UFCG, Programaçao I


palavra = raw_input('')
palavras = []

while palavra != 'fim':
	palavras.append(palavra)
	palavra = raw_input('')

letra = raw_input('')
num = int(raw_input(''))

for i in range(len(palavras)):
	cont = 0
	l = 0
	while cont < num or l != len(palavras[i]):
		if palavras[i][l] == letra:
			cont += 1
		l += 1
	if cont == num:
		print palavras[i]
	else:
		print 'Nenhuma palavra encontrada.'
