#coding: utf-8
# MDC por Euclides
# (C) 2016, Yovany Cunha/UFCG, Programaçao I


m = int(raw_input(''))
n = int(raw_input(''))
aux = 0
mdc = 0
if m == n:
	mdc = m
elif m == 0:
	mdc = n
elif n == 0:
	mdc = m

if n > m:
	aux = n
	n = m
	m = aux
if m != 0 and n != 0:
	while True:
		resto = m % n
		if resto == 0: 
			mdc = n
			break
		m = n
		n = resto

print mdc
