#coding: utf-8
# Guerra Baralho
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

empates= 0
jogador1 = 0
jogador2 = 0

while True:
	entrada = raw_input('')
	if entrada == '0 0': break
	jog1,jog2 = entrada.split()
	jog1 = int(jog1)
	jog2 = int(jog2)
	if jog1 == jog2:
		empates += 1
	elif jog1 > jog2:
		jogador1 += 1
	else:
		jogador2 += 1

print 'Jogador 1: %d, Jogador 2: %d, Empates: %d' % (jogador1,jogador2,empates)
