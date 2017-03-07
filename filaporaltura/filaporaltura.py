# coding: utf-8
# Fila por Altura
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def insere_na_fila(fila,nome,altura):
	indice = 0
	altura = float(altura)
	minha_tupla = (nome,altura)
	for i in range(len(fila)):
		if fila[i][1] >= altura:
			fila.insert(i,minha_tupla)
			return
	fila.append(minha_tupla)

fila = [("maria", 1.05), ("joao", 1.09), ("ana", 1.16)]
insere_na_fila(fila, "jose", 1.12)
assert fila == [("maria", 1.05), ("joao", 1.09), ("jose", 1.12), ("ana", 1.16)]

fila = [("maria", 1.05), ("joao", 1.09), ("ana", 1.16)]
insere_na_fila(fila, "jose", 1.22)
assert fila == [("maria", 1.05), ("joao", 1.09), ("ana", 1.16), ("jose", 1.22)]
