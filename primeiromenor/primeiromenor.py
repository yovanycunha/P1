# coding: utf-8
# Primeiro Menor
# (C) 2016, Yovany Cunha / UFCG, Programação 1


def primeiro_menor(numero, num):
	i = 0
	tem_menor = False
	while True:
		if i == len(num): break
		if num[i] < numero:
			tem_menor = True
			break
		else:
			i += 1
	if tem_menor == False:
		return -1
	else:
		return i

	nums = [7, 5, 3, 9, 11, 8]
	assert primeiro_menor(4, nums) == 2
	assert primeiro_menor(3, nums) == -1

if __name__ == '__main__':
	numeros = raw_input('').split()
	lista_numeros = []
	numero = int(raw_input(''))
	for i in range(len(numeros)):
		lista_numeros.append(int(numeros[i]))

	if primeiro_menor(numero, lista_numeros) == -1:
		print 'sem menores que %d' % numero
	else:
		print 'primeiro menor que %d: %d' % (numero,lista_numeros[primeiro_menor(numero,lista_numeros)])

