# coding: utf-8
# Letras Alternadas
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def letras_alternadas(nome):
	nova_palavra = ''
	for i in range(len(nome)):
		if i % 2 == 0:
			nova_palavra += nome[i]
	return nova_palavra

assert letras_alternadas("casa") == 'cs'
assert letras_alternadas("exemplo") == "eepo" 

