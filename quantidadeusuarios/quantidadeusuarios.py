#coding: utf-8
# Quantidade de Usuários
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def quantidade_usuarios(cadastro):
	qnt_usuarios = 0
	for i,j in cadastro.iteritems():
		if i != 9999:
			qnt_usuarios += len(j)
	return qnt_usuarios

lsd = {1234:['Andrey'], 1226:['Nazareno', 'Livia'], 9999:['administrador'] }
deq = {1114:['Ana'] }

assert quantidade_usuarios(lsd) == 3
assert quantidade_usuarios(deq) == 1

