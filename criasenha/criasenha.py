# coding: utf-8
# Cria Senha
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def criaSenhaFraca(palavra):
	senha = palavra
	return senha

def criaSenhaForte(palavra):
	senha = ''
	for i in range(len(palavra)):
		if palavra[i] == 'o' or palavra[i] == 'O':
			senha += '0'
		elif palavra[i] == 'i' or palavra[i] == 'I' or palavra[i] == 'l' or palavra[i] == 'L':
			senha += '1'
		elif palavra[i] == 'e' or palavra[i] == 'E':
			senha += '3'
		elif palavra[i] == 'a' or palavra[i] == 'A':
			senha += '4'
		elif palavra[i] == 'b' or palavra[i] == 'B':
			senha += '6'
		elif palavra[i] == 't' or palavra[i] == 'T':
			senha += '7'
		else:
			senha += palavra[i]
	return senha

palavra,senha = raw_input('').split()

while palavra != '***':
	if senha == 'fraca':
		print criaSenhaFraca(palavra)
	elif senha == 'forte':
		print criaSenhaForte(palavra)
	palavra,senha = raw_input('').split()
