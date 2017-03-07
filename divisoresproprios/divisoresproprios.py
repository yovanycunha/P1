#coding: utf-8
# Divisores Próprios
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

numero = int(raw_input(''))

for i in range(1,numero):
	if numero % i == 0:
		print i
