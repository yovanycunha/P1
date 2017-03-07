#coding: utf-8
# Resumos Iguais
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def agrupa_resumos_iguais(seq):
	resumos = {}
	for i in range(len(seq)):
		soma = soma_interna(seq[i])
		if resumos.has_key(soma):
			resumos[soma].append(seq[i])
		else:
			resumos[soma] = [seq[i]]
	return resumos

def soma_interna(num):
	soma = 0
	while num != 0:
		soma += (num%10)
		num /= 10
	return soma


lista1 = [60, 343, 19, 1230, 51, 123]
print agrupa_resumos_iguais(lista1)# == {6:[60, 1230, 51, 123], 10:[343,19]}
