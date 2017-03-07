#coding: utf-8
# Altera Vetor
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def altera_vetor_por_escalar(vetor,escalar):
	for i in range(len(vetor)):
		vetor[i] *= escalar
	
vetor_1 = [1, 2, 3]
assert altera_vetor_por_escalar(vetor_1, -1) == None
assert vetor_1 == [-1, -2, -3]
assert altera_vetor_por_escalar(vetor_1, 2) == None
assert vetor_1 == [-2, -4, -6]

