# coding: utf-8
# Calculadora de Médias
# (C) 2016, Yovany Cunha / UFCG, Programação 1

import math

def media_arit(numeros):
	media_a = 0.0
	soma = 0.0
	for i in range(len(numeros)):
		soma += float(numeros[i])
	media_a = soma / len(numeros)
	return media_a

def media_geo(numeros):
	media_g = 0.0
	produto = 1.0
	exp = 1/float(len(numeros))
	for i in range(len(numeros)):
		produto = produto * float(numeros[i])
	media_g = pow(produto,exp)	
	return media_g

def media_harm(numeros):
	media_h = 0.0
	soma = 0.0
	for i in range(len(numeros)):
		soma  += 1.0/float(numeros[i])
	media_h = len(numeros) / soma
	return media_h	

media_tipo = raw_input('')
#entrada = raw_input('')
#numeros = raw_input('').split()

while media_tipo != 'Q':
	numeros = raw_input('').split()
	if media_tipo == 'MA':
		#numeros = raw_input('').split()
		#numeros.append(float(entrada))
		print 'Média aritmética: %.4f' % media_arit(numeros)
		print '----'
	elif media_tipo == 'MG':
		#entrada = raw_input('')
		#numeros.append(float(entrada))
		print 'Média Geométrica: %.4f' % media_geo(numeros)
		print '----'
	elif media_tipo == 'MH':
		#numeros = raw_input('')
		#numeros.append(float(entrada))
		print 'Média Harmônica: %.4f' % media_harm(numeros)
		print '----'
	media_tipo = raw_input('')
