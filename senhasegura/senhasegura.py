#coding: utf-8
# Senha Segura
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

palavra = raw_input()
new = ''
for i in range(0,len(palavra)):
	if palavra[i] == " ":
		new += palavra[i]
	else:
		new += palavra[i] + palavra[i]
print new
if len(new) >= 13:
	print 'senha segura'
else:
	print 'senha insegura'
