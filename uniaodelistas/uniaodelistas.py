#coding: utf-8
# União de Listas
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def uniao_listas(lista1,lista2):
		
	for i in range(len(lista2)):
		tem_na_lista = False
		for j in range(len(lista1)):
			if lista2[i] == lista1[j]:
				tem_na_lista = True
		if tem_na_lista == False:
			lista1.append(lista2[i])
	print lista1
	for m in range(len(lista1)-1,0,-1):
		#unico = lista1[len(lista1)-1]
		for p in range(m-1,-1,-1):
			print 'a'
			if lista1[m] == lista1[p]:
				lista1.pop(p)
	print lista1



#l1 = [2,1,3,4]
#l2 = [2]
#assert uniao_listas(l1,l2) == None
#assert l1 == [2,1,3,4]
#assert l2 == [2]
#
#l1 = [1,3,4]
#l2 = [4]
#assert uniao_listas(l1,l2) == None
#assert l1 == [1,3,4]
#assert l2 == [4]

#l1 = [2,4,1]
#l2 = [6,7,91]
#uniao_listas(l1,l2)
#assert l1 == [2,4,1,6,7,91]
#assert l2 == [6,7,91]

#l1 = []
#l2 = [6,7,91]
#uniao_listas(l1,l2)
#assert l1 == [6,7,91]
#assert l2 == [6,7,91]

#l1 = []
#l2 = []
#uniao_listas(l1,l2)
#assert l1 == []
#assert l2 == []

l1 = [1,1,7,7,0,0]
l2 = [0,1,7]
uniao_listas(l1,l2)
#assert l1# == []
#assert l2# == []

