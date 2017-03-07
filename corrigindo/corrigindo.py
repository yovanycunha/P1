#coding: utf-8
# Média Final
# (C) 2016, Yovany Cunha/UFCG, Programaçao I
import math

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

delta = pow(b,2) - 4*a*c

if delta < 0:
	print 'sem raizes reais'
elif delta == 0:
	x = ( -b + pow(delta,0.5) )/float(2*a)
	print 'x = %.2f' % x	
else:
	x1 = ( -b + pow(delta,0.5) )/float(2*a)
	x2 = ( -b - pow(delta,0.5) )/float(2*a)
	print 'x1 = %.2f' % x1
	print 'x2 = %.2f' % x2

