#coding: utf-8
# Abaixo da Média
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

media = 0.0
maiores = []
soma = 0
while True:
	entrada = raw_input('')
	if entrada == 'fim': break
	num = int(entrada)
	maiores.append(num)
	soma += num

media = soma * 1.0 / len(maiores)

print "%.2f" % media

for i in range(len(maiores)):
	if maiores[i] < media:
		print "%d %d" % (i + 1,maiores[i])
