#coding: utf-8
# Média Final
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

cargo = int(raw_input())

if cargo == 1:
	print 'Deverá receber em dezembro R$ 25000.00.'
elif cargo == 2:
	print 'Deverá receber em dezembro R$ 15000.00.'
elif cargo == 3:
	faltas = int(raw_input())
	if faltas == 0:
		print 'Valor da gratificação R$ 500.00.'
		print 'Deverá receber em dezembro R$ 8500.00.'
	else:
		gratif = (235-faltas) * 2.00
		salario = 8000.00 + gratif
		print 'Valor da gratificação R$ %.2f.' % gratif
		print 'Deverá receber em dezembro R$ %.2f.' % salario
elif cargo == 4:
	faltas = int(raw_input())
	if faltas == 0:
		print 'Valor da gratificação R$ 300.00.'
		print 'Deverá receber em dezembro R$ 5300.00.'
	else:
		gratif = (235-faltas) * 1.00
		salario = 5000.00 + gratif
		print 'Valor da gratificação R$ %.2f.' % gratif
		print 'Deverá receber em dezembro R$ %.2f.' % salario
elif cargo == 5:
	faltas = int(raw_input())
	if faltas == 0:
		print 'Valor da gratificação R$ 200.00.'
		print 'Deverá receber em dezembro R$ 3000.00.'
	else:
		gratif = (235-faltas) * 0.70
		salario = 2800.00 + gratif
		print 'Valor da gratificação R$ %.2f.' % gratif
		print 'Deverá receber em dezembro R$ %.2f.' % salario
