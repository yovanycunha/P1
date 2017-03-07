#coding: utf-8
# Agrupa Pares
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def agrupa_pares_impares(numeros):
	pares = []
	impares = []
	for i in numeros:
		if i % 2 == 0:
			pares.append(i)
		else:
			impares.append(i)
	agrupados = dict([('pares',pares),('impares',impares)])
	return agrupados

assert agrupa_pares_impares([10, 24, 97, 88]) == {"pares":[10, 24, 88], "impares":[97]}
assert agrupa_pares_impares([11, 23, 35]) == {"pares":[ ], "impares":[11, 23, 35]}

