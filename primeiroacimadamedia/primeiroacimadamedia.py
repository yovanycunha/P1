# coding: utf-8
# Primeiro Acima da Média
# (C) 2016, Yovany Cunha / UFCG, Programação 1


entrada = raw_input('')
valores = []
i = 0
soma = 0

while entrada != 'fim':
	valor = float(entrada)
	soma += valor
	valores.append(valor)
	entrada = raw_input('')

media = soma / len(valores)

while True:
	if valores[i] >= media:break
	i += 1

print '%d, %.2f > %.2f' % (i,valores[i],media)
