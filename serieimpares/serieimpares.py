#coding: utf-8
# Série de ímpares
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

for i in range(1,102):
	if i % 2 != 0:
		if i % 7 == 0 or i % 10 == 7:
			print '*'
		else:
			print i
