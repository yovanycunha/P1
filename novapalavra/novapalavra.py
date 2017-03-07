#coding: utf-8
# Nova Palavra
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

palavra = raw_input('')
tamanho = raw_input('')
new = ''

for i in range(len(tamanho)):
	for l in range(1,len(palavra)):
		new += int(tamanho[-l]) * palavra[i]

print new
