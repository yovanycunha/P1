# coding: utf-8
# Tiro ao Alvo
# (C) 2016, Yovany Cunha / UFCG, Programação 1

import math

media = 0.0
contador = 0

while True:
	entrada = raw_input('')
	x,y = entrada.split(", ")
	x = float(x)
	y = float(y)
	distancia = pow(pow(x,2)+pow(y,2),0.5)
	if distancia >= 200: break
	if distancia < 200:
		media += distancia
		contador += 1
	print "%.2f" % distancia
media = media / contador
print '--'
print 'num disparos: %d' % contador
print 'distancia media: %.2f' % media

