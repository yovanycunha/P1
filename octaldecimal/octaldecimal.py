#coding: utf-8
# Série: Octal/Decimal
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

import math

numero = raw_input('')
octal = []
potencia = []
decimal = 0

for i in range(len(numero)):
	num = int(numero[i])
	octal.append(num)

for i in range(len(numero)):
	pot = pow(8,i)
	potencias.append(pot)

for i in range(len(numero)):
	decimal += octal[i] * potencias[i]
	print '4 * 8^3 = 2048'
