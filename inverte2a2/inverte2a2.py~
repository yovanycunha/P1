# coding: utf-8
# Inverte 2 a 2
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def inverte2a2_condicional(seq):
	aux = 0
	if len(seq) % 2 == 0:
		for i in range(0,len(seq),2):
			if seq[i+1] != seq[i]+1:
				aux = seq[i + 1]
				seq[i + 1] = seq[i]
				seq[i] = aux
		#return seq
	else:
		for i in range(0,len(seq)-1,2):
			if seq[i+1] != seq[i]+1:
				aux = seq[i + 1]
				seq[i + 1] = seq[i]
				seq[i] = aux
		#return seq

seq = [3,1,2,3,10,5,6]
inverte2a2_condicional(seq)
assert seq == [1,3,2,3,5,10,6]

seq = []
inverte2a2_condicional(seq)
assert seq == []

seq = [3,1,2]
inverte2a2_condicional(seq)
assert seq == [1,3,2]

seq = [3]
inverte2a2_condicional(seq)
assert seq == [3]

seq = [1,-1]
inverte2a2_condicional(seq)
assert seq == [-1,1]

seq = [-1,0]
inverte2a2_condicional(seq)
assert seq == [-1,0]



