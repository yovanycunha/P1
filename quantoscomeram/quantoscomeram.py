# coding: utf-8
# Quantos Comeram
# (C) 2016, Yovany Cunha / UFCG, Programação 1


def quantos_comeram(feijoadas,fila):
	a = True
	i = 0
	saida = 0
	while a == True and i < len(fila):
		if feijoadas >= fila[i]:
			saida += fila[i]
			feijoadas = feijoadas - fila[i]
			i += 1
			a = True
		else:
			a = False
	return saida
