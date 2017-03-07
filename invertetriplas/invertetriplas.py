#coding: utf-8
# Inverte Triplas
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def inverte3a3(palavra):
	palavra_invertida = ''
	for i in range(len(palavra)-3,-1,-3):
		tripla = ''
		for j in range(i,i+3):
			tripla += palavra[j]
		palavra_invertida += tripla
	return palavra_invertida

def soma_interna(num):
	soma = 0
	while num != 0:
		soma += (num%10)
		num /= 10
	return soma

assert inverte3a3("paisimtio") == "tiosimpai"
