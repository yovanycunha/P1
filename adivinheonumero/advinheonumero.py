#coding: utf-8
# Advinhe o Número
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

import random

#numero = random.randint(0,1000)
numero = int(raw_input(''))
palpite = int(raw_input('Palpite? '))
tentativas = 1
while palpite != numero:
	if palpite > numero:
		print 'alto'
	else:
		print 'baixo'
	tentativas += 1
	palpite = int(raw_input('Palpite? '))

print 'Você acertou em %d tentativas.' % tentativas
