#coding: utf-8
# Sequência
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

numero = int(raw_input(''))
sequencia = 1
soma = 0

while True:
	soma += sequencia
	if soma >= numero: break
	else:
		print sequencia
	sequencia += sequencia
