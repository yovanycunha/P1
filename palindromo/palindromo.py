#coding: utf-8
# Receita
# (C) 2016, Yovany Cunha/UFCG, Programaçao I
import string
pali = raw_input()
palavra = ''
new = ''
for i in pali:
	if i != " ":
		palavra += i
	
for i in range(len(palavra)-1,-1,-1):
	new += palavra[i]
if new == palavra:
	print '%s é palíndromo' % pali
else:
	print '%s não é palíndromo' % pali
