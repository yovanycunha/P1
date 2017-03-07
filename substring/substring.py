#coding: utf-8
# Substring
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def is_substring(palavra1,palavra2):
	pos_compair = 0
	count_compair = 0
	tem_sub = False
	for i in range(len(palavra2)):
		for l in range(pos_compair,len(palavra1)):
			if palavra2[i] == palavra1[l]:
				print palavra1[l]
				pos_compair = l
				count_compair += 1
				break
	if count_compair == len(palavra2):
		return True
	else:
		return False



print is_substring('arroio','rro')
#assert not is_substring('casorio', 'casa')
