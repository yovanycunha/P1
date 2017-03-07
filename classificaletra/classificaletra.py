#coding: utf-8
# Classifica Letra
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

palavra = raw_input('')

for i in range(len(palavra)):
	if palavra[i] == 'A' or palavra[i] == 'a' or palavra[i] == 'E' or palavra[i] == 'e' or palavra[i] == 'I' or palavra[i] == 'i' or palavra[i] == 'O' or palavra[i] == 'o' or palavra[i] == 'U' or palavra[i] == 'u':
		print '<%s> sim' % palavra[i]
	else:
		print '<%s> nao' % palavra[i]

