#coding: utf-8
# Troca Chave
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def troca_chave(meu_dic):
	
	new = {}
	
	for i in range(len(meu_dic)):
		
		new[meu_dic.values()[i]]= meu_dic.keys()[i]
	
	return new


assert troca_chave({1:2}) == {2:1}
assert troca_chave({1:2, 2:3, 3:4}) == {2:1, 3:2, 4:3}
assert troca_chave({ '@':'V','a':'v', 'n':'o'}) == { 'V':'@','v':'a', 'o':'n'}
