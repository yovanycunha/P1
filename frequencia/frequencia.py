#coding: utf-8
# Frequência
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def get_frequencia(sequencia):
	repetidos = []
	while len(sequencia) != 0:
		repetido = 0
		elemento = sequencia[0]
		for i in range(len(sequencia)-1,-1,-1):
			if sequencia[i] == elemento:
				sequencia.pop(i)
				repetido += 1
		repetidos.append(repetido)
	return repetidos

assert get_frequencia(['b','b','c','b', 'a']) == [3,1,1]
