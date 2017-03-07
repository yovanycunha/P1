# coding: utf-8
# Valor Polinômio
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def valor_polinomio(polinomio,valor):
	soma = 0
	for i in range(len(polinomio)):
		soma += polinomio[i] * pow(valor,i)
	return soma
