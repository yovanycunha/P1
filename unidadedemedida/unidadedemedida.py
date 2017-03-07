#coding: utf-8
# Unidade de Medida
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

tabela ={1000:km,100:hm,10:dam
1 	m
0,1 	dm
0,01 	cm
0,001 	mm

if __name__ == '__main__':
	while True:
		entrada = raw_input()
		entrada = entrada.split()
		if entrada[0] == 0 and entrada[2] == 0: break
		for i in range(0,len(entrada),2):
			tupla_medida = (entrada[i],entrada[i=1])
			soma(tabela,tupla_medida)
