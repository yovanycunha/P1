#coding: utf-8
# Remove Consecutivas
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def remove_consecutivas(palavras):
	for i in range(len(palavras)-1,-1,-1):
		for l in range(len(palavras[i])-1,0,-1):
			if palavras[i][l].lower() == palavras[i][(l-1)].lower():
				palavras.pop(i)
				break

#lista1 = ['arara', 'tv',   'bacia']
#assert remove_consecutivas(lista1) == None
#assert lista1 == ['arara', 'tv',  'bacia']

#lista1 = ['arara', 'arroba',   'bacia']
#assert remove_consecutivas(lista1) == None
#assert lista1 == ['arara', 'bacia']

#lista1 = ['', 'arroba',   'bacia']
#assert remove_consecutivas(lista1) == None
#assert lista1 == ['', 'bacia']

#lista1 = ['', 'arroba',   'bacia']
#assert remove_consecutivas(lista1) == None
#assert lista1 == ['', 'bacia']

lista1 = ['bBb', "arr"]
remove_consecutivas(lista1)# == None
print lista1# == ['', 'bacia']


