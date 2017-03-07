# coding: utf-8
# Filta e Altera Lista
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def filtra_altera_lista(num,lista):
	for i in range(len(lista)-1,-1,-1):
		if i % num != 0 :
			lista.pop(i)


seq = [0,1,2,3,4,5,6]
filtra_altera_lista(2, seq)
print seq #== [0, 2, 4 ,6]
