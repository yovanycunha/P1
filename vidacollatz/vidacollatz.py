#coding: utf-8
# Vida Collatz
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

numero = int(raw_input(''))
lista = []
lista.append(numero)
i = 1


while True:
	if lista[i-1] % 2 == 0:
		novo = lista[i-1] / 2
		lista.append(novo)
	else:
		novo = 3 * lista[i-1] + 1
		lista.append(novo)
 
	if lista[i] == 1:
		lista.append(1)
		break
	i += 1
print i + 1
