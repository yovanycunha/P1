#coding: utf-8
# Converte Senha
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

senha = raw_input('')
trocas = 0
new = ''
new += senha[0]

for i in range(1,len(senha)):
	if senha[i] == 'A' or  senha[i] == 'a':
		trocas += 1
		new += '4'
	elif senha[i] == 'E' or senha[i] == 'e':
		trocas += 1
		new += '3'
	elif senha[i] == 'I' or senha[i] == 'i':
		trocas += 1
		new += '1'
	elif senha[i] == 'O' or senha[i] == 'o':
		trocas += 1
		new += '0'
	else:
		new += senha[i]

print '%s (%d troca(s))' % (new,trocas)
