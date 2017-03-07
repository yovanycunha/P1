#coding: utf-8
# Receita
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

lucro = 0.0

for i in range(1,13):
	valor1,valor2 = raw_input('').split(" ")
	valor1 = float(valor1)
	valor2 = float(valor2)
	lucro = valor1 - valor2
	if lucro >= 0:
	 	print ' %.1f' % lucro
	else:
		lucro = lucro* (-1.0)
		print '-%.1f' % lucro
