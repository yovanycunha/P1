# coding: utf-8
# Soma e Diminui Vizinhos!
# (C) 2016, Yovany Cunha / UFCG, Programação 1


def soma_diminui_vizinhos(lista):
	soma = 0
	resultado = 0
	if len(lista) == 0:
		return 0
	else:
		for i in range(0,len(lista),3):
			soma = lista[i] + lista[i+1]
			resultado = soma - lista[i+2]
	return resultado


