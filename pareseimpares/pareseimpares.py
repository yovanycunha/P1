#coding: utf-8
# Pares e Ímpares
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

soma_par = 0
soma_impar = 0
cont_par = 0
cont_impar = 0
media_par = 0.0
media_impar = 0.0


n = int(raw_input())

for i in range(n):
	numero = int(raw_input())
	if numero % 2 == 0:
		soma_par += numero
		cont_par += 1
	else:
		soma_impar += numero
		cont_impar += 1

media_par = soma_par/float(cont_par)
media_impar = soma_impar/float(cont_impar)

print 'pares: %d' % cont_par
print 'ímpares: %d' % cont_impar
print 'média pares: %.1f' % media_par
print 'média ímpares: %.1f' % media_impar
