#coding: utf-8
# Expressão Regular
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def is_substring_expr(palavra1,palavra2):
	pos_asterisco = 0
	is_sub = True
	termo1 = ''
	termo2 = ''
	j = 0

	while True:
		if palavra2[j] == '*': break
		else:
			termo1 += palavra2[j]
		j += 1

	for k in range(j + 1, len(palavra2)):
		termo2 += palavra2[k]
	for l in range(len(termo1)):
		if termo1[l] != palavra1[l]:
			return False

	for m in range(-1,-len(termo2)-1,-1):
		if termo2[m] != palavra1[m]:
			return False

	if is_sub == True:
		return True


assert is_substring_expr('oicarovoce','oi*voce')
#assert is_substring_expr('oicvoce','oi*voce')


