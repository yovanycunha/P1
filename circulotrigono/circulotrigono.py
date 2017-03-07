#coding: utf-8
# Média Final
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

angulo = int(raw_input())

if angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
	print 'Sobre eixos'
elif angulo < 0 or (90 > angulo%360 > 0):
	print 'Quadrante 1'
elif angulo < 90 or (180 > angulo%360 > 90):
	print 'Quadrante 2'
elif angulo < 180 or (270 > angulo%360 > 180):
	print 'Quadrante 3'
else:
	print 'Quadrante 4'
