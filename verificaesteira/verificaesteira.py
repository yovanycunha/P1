#coding: utf-8
# Verifica Esteira
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def verifica_esteira(lista1, lista2):
	tem_na_esteira = False
	j = 0
	if len(lista2) < 1 and len(lista1) < 1:
		return True
	elif len(lista2) < 1 and len(lista1) > 0:
		return False
	else:
		while j < len(lista1):
			if lista2[0] == lista1[j]:
				tem_na_esteira = True
				break
			j += 1

		if tem_na_esteira == True:
			for i in range(1,len(lista2)):
				for k in range(len(lista1)):
					if lista2[i] == lista1[k]:
						tem_na_esteira = False
						return False
		if tem_na_esteira == False:
			return False
		else:
			return True

l1 = [1,3,2]
l2 = [1,2] #false ou true ????
print verifica_esteira(l1,l2)
#assert l1 == [2,1,3,4]
#assert l2 == [2]

#l1 = [1,3,4]
#l2 = [4,1]
#assert not verifica_esteira(l1,l2)
#assert l1 == [1,3,4]


