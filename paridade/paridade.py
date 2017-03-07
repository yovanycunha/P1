# coding: utf-8
# Paridade
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def paridade(valor):
	par = 0
	for i in range(len(valor)-1):
		if valor[i] == '1':
			par += 1
	if par % 2 == 0 and valor[-1] == '0':
		return True
	else:
		return False

valor = raw_input('')
while paridade(valor) == True:
	valor = raw_input('')
print "ERRO"
