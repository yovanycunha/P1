#coding: utf-8
# Decifra Segredo
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def decifra(chave,mensagem):
	new = ''
	for i in range(len(mensagem)):
		new += chave[mensagem[i]]
		
	return new


chave1={'@':'V','a':'v','n':'o','l':'i','#':' ','4':'a','+':'u'}
assert decifra( chave1, '+a4') == 'uva'
assert decifra(chave1, '@nan#al+#4#+a4') == 'Vovo viu a uva'
