#coding: utf-8
# Extremos
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

n = int(raw_input(''))
numeros = []
maiores = 0
menores = 0
menor = 0

for i in range(n):
	num = int(raw_input(''))
	numeros.append(num)

if numeros[0] > numeros[len(numeros)-1]:
	menor = numeros[len(numeros)-1]
else:
	menor = numeros[0]

for i in range(0,len(numeros)):
	if numeros[i] > menor:
		maiores += 1
	elif numeros[i] < menor:
		menores += 1

print 'Menor dos extremos: %d' % menor
print '%d número(s) abaixo do menor' % menores
print '%d número(s) acima do menor' % maiores
