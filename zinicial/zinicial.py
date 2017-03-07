# coding: utf-8
# Z Inicial
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def z_inicial(lista):
	z_cont = 0
	for i in range(len(lista)):
		if lista[i][0] == 'Z' or lista[i][0] == 'z':
			z_cont += 1
	return z_cont

lista1 = ["zumbi","Zeca","Recife"]
lista2 = ["livro", "cd", "software"]
assert z_inicial(lista1) == 2
assert z_inicial(lista2) == 0

if __name__ == '__main__':
	lista_palavras = raw_input('').split()
	print z_inicial(lista_palavras)
