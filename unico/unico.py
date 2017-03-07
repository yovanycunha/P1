# coding: utf-8
# Único
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def unico(palavra):
	nova = ''
	if len(palavra) == 0:
		return nova
	else:
		for i in range(0,len(palavra)-1):
			if palavra[i] != palavra[i-1]:
				nova += palavra[i]
		if len(palavra) != 0 and len(nova) == 0:
			nova += palavra[0]
		return nova

