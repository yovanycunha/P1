#coding: utf-8
# Primeira Vogal
# (C) 2016, Yovany Cunha/UFCG, Programaçao I



placa = raw_input('').split(" ")

for i in placa:
	if i[-1] == '1' or i[-1] == '2':
		print '%s: janeiro' % i
	elif i[-1] == '3' or i[-1] == '4':
		print '%s: fevereiro' % i
	elif i[-1] == '5':
		print '%s: marco' % i
	elif i[-1] == '6':
		print '%s: abril' % i
	elif i[-1] == '7':
		print '%s: maio' % i
	elif i[-1] == '8':
		print '%s: junho' % i
	elif i[-1] == '9':
		print '%s: julho' % i
	elif i[-1] == '0':
		print '%s: agosto' % i

