#coding: utf-8
# Média Final
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

soma = num1 + num2 + num3

if soma%3 == 0 and soma%5 != 0:
	print 'plif'
elif soma%3 != 3 and soma%5 == 0:
	print 'plof'
elif soma%3 == 3 and soma%5 == 0:
	print 'plifplof'
elif soma%3 != 3 and soma%5 != 0:
	print soma
