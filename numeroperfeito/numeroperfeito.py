#coding: utf-8
# Número Perfeito
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

numero = int(raw_input())
soma_div = 0
for i in range(1,numero):
	if numero % i == 0:
		soma_div += i
if soma_div == numero:
	print '%d é um número perfeito.' % numero
else:
	print '%d não é um número perfeito.' % numero
