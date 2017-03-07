#coding: utf-8
# Média Final
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

salario_bruto = float(raw_input())
dias = int(raw_input())
custo_trans = float(raw_input())

vale_trans = dias * custo_trans
FGTS = salario_bruto * 0.08
INSS1 = salario_bruto * 0.12

if salario_bruto <= 1317.07:
	INSS2 = salario_bruto * 0.08
elif salario_bruto <= 2195.12 and salario_bruto > 1317.07:
	INSS2 = salario_bruto * 0.09
else:
	INSS2 = salario_bruto * 0.11

if vale_trans > salario_bruto*0.06:
	vale = vale_trans - (salario_bruto*0.06)	
	custo_mensal = salario_bruto + vale + FGTS + INSS1
	salario_liq = salario_bruto - INSS2 - vale
	print 'O salário base é R$ %.2f' % salario_bruto
	print 'O custo mensal para o empregador é de R$ %.2f' % custo_mensal
	print 'O salário líquido que o trabalhador irá receber no mês é R$ %.2f' % salario_liq
else:
	custo_mensal = salario_bruto + vale_trans + FGTS + INSS1
	salario_liq = salario_bruto - INSS2 
	print 'O salário base é R$ %.2f' % salario_bruto
	print 'O custo mensal para o empregador é de R$ %.2f' % custo_mensal
	print 'O salário líquido que o trabalhador irá receber no mês é R$ %.2f' % salario_liq

