#coding: utf-8
# Operações Bancárias
# (C) 2016, Yovany Cunha/UFCG, Programaçao I


cliente,saldo = raw_input('').split()
saldo = float(saldo)


while True:
	entrada = raw_input('')
	if entrada == '3': break
	operacao,quantia = entrada.split()
	operacao = int(operacao)
	quantia = float(quantia)
	if operacao == 1:
		#quantia = float(raw_input(''))
		saldo -= quantia
	elif operacao == 2:
		#quantia =  float(raw_input(''))
		saldo += quantia
print 'Saldo de R$ %.2f na conta de %s' % (saldo, cliente)
