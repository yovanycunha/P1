#coding: utf-8
# Receita
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

lucro = 0.0
meses = ['','jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
for i in range(1,13):
	valor1,valor2 = raw_input('').split(" ")
	valor1 = float(valor1)
	valor2 = float(valor2)
	lucro = valor1 - valor2
	if lucro >= 0:
		print '%s  %.1f' % (meses[i],lucro)
	else:
		lucro = lucro * (-1)
		print '%s -%.1f' % (meses[i],lucro)
