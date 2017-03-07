#coding: utf-8
# Sub Sequência 1, 2, 3
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def tem123plus(numeros):
	pos_1 = 0
	pos_2 = 0
	seq_ok = False
	k = 0
	procurado = 1
	while True:
		if k == len(numeros): break
		if procurado == numeros[k]:
			pos_1 = k
			procurado += 1
			break
		k += 1
	while True:
		if k == len(numeros): break
		if procurado == numeros[k]:
			procurado += 1
			break
		k += 1
	while True:
		if k == len(numeros): break
		if procurado ==  numeros[k]:
			return pos_1
		k += 1
	return -1

assert tem123plus([3,2,1,2,3]) == 2
assert tem123plus([4,1,1,1,4,2,3]) == 1
assert tem123plus([1,2,2,3]) == 0
assert tem123plus([1,2,2,4]) == -1

