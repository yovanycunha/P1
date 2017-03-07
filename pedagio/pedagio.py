#coding: utf-8
# Média Final
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

tipo_veic = raw_input()

if tipo_veic == 'Automóvel utilitário':
	pedagio = 11.40
	print 'Valor a pagar: R$ %.2f.' % pedagio
elif tipo_veic == 'Ônibus':
	eixos_veic = int(raw_input())
	pedagio = eixos_veic * 11.40
	print 'Valor a pagar: R$ %.2f.' % pedagio
elif tipo_veic == 'Caminhão':
	eixos_veic = int(raw_input())
	pedagio = eixos_veic * 9.60
	print 'Valor a pagar: R$ %.2f.' % pedagio
elif tipo_veic == 'Motocicleta':
	pedagio = 5.70
	print 'Valor a pagar: R$ %.2f.' % pedagio
else:
	print 'Veículo não cadastrado.'
