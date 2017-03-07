#coding: utf-8
# Divisores Pares
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

numero = int(raw_input(''))

for i in range(1,numero):
	if i%2 == 0  and numero%i == 0:
		print i
