#coding: utf-8
# Troca Chave
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def ausentes(estoque):
	zerados = 0
	for i in range(len(estoque)):
		if estoque.values()[i] == 0:
			zerados += 1
	return zerados
	
	
livros = { "Metamorfose": 30, "O Principe": 0, "Vigiar e Punir": 0, "Dumbo": 22}
assert ausentes(livros) == 2

