#coding: utf-8
# Tabela de Quadrados
# (C) 2016, Yovany Cunha/UFCG, Programaçao I
import math

ano1 = int(raw_input())
ano2 = int(raw_input())
qnt_acima = 0
qnt_abaixo = 0
media_acima = 0
media_abaixo = 0
soma_acima = 0
soma_abaixo = 0
percent_acima = 0.0
percent_abaixo = 0.0

for i in range(ano1, ano2+1):
	salario = float(raw_input())
	if salario >= 100:
		qnt_acima += 1
		soma_acima += salario
	else:
		qnt_abaixo += 1
		soma_abaixo += salario
if qnt_acima == 0:
	percent_abaixo = float(100*qnt_abaixo)/(ano2 - ano1 + 1)
	media_abaixo = soma_abaixo/qnt_abaixo
	print '0 ano(s) acima (0% dos anos)'
	print '%d ano(s) abaixo (%.0f%% dos anos)' % (qnt_acima,percent_abaixo)
	print 'média dos anos abaixo: U$ %.2f' % media_abaixo
elif qnt_abaixo == 0:
	percent_acima = float(100*qnt_acima)/(ano2 - ano1 + 1)
	media_acima = soma_acima/qnt_acima
	print '0 ano(s) abaixo (0% dos anos)'
	print '%d ano(s) acima (%.0f%% dos anos)' % (qnt_acima,percent_acima)
	print 'média dos anos acima: U$ %.2f' % media_acima
else:	
	percent_abaixo = float(100*qnt_abaixo)/(ano2 - ano1 + 1)
	media_abaixo = soma_abaixo/qnt_abaixo
	percent_acima = float(100*qnt_acima)/(ano2 - ano1 + 1)
	media_acima = soma_acima/qnt_acima
	print '%d ano(s) abaixo (%.0f%% dos anos)' % (qnt_abaixo,percent_abaixo)
	print 'média dos anos abaixo: U$ %.2f' % media_abaixo
	print '%d ano(s) acima (%.0f%% dos anos)' % (qnt_acima,percent_acima)
	print 'média dos anos acima: U$ %.2f' % media_acima
