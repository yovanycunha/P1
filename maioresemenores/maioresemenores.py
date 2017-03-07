# coding: utf-8
# Maiores e Menores
# (C) 2016, Yovany Cunha / UFCG, Programação 1

pivot = int(raw_input(''))
numero = int(raw_input(''))
maiores = []
menores = []

while numero >= 0:
	if numero > pivot:
		maiores.append(numero)
	else:
		menores.append(numero)
	numero = int(raw_input(''))

print menores
print pivot
print maiores
