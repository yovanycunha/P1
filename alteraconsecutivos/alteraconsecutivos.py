# coding: utf-8
# Altera Consecutivos
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def inverte2a2(seq):
	aux = 0
	if len(seq) % 2 == 0:
		for i in range(0,len(seq),2):
			aux = seq[i + 1]
			seq[i + 1] = seq[i]
			seq[i] = aux
		return seq
	else:
		for i in range(0,len(seq)-1,2):
			aux = seq[i + 1]
			seq[i + 1] = seq[i]
			seq[i] = aux
		return seq

