#coding: utf-8
# Resumo Compras
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

maior = 0.0
soma = 0.0
contador = 0

while True:
	valor = raw_input('')
	if valor == 'fim': break
	valor = float(valor)
	soma += valor
	contador += 1
	if valor > maior:
		maior = valor

media = soma/contador

print 'O valor médio por produto foi R$ %.2f. O produto mais caro custa R$ %.2f.' % (media,maior)
