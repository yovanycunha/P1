#coding: utf-8
# Conjectura Collatz
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

numero = int(raw_input(''))

while numero != 1:
	print numero
	if numero % 2 == 0:
		numero = numero / 2
	else:
		numero = (3 * numero) + 1
print 1
