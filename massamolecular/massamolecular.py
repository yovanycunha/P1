#coding: utf-8
# Massa Molecular
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

import string

tabela_elementos = {'H':1, 'S':32, 'O':16, 'C':12, 'Ca':40, 'Na':23, 'P':31}

def massa_molecular(tabela_elementos,listaatomoelemento):
	massa_molecular = 0
	for i in range(len(listaatomoelemento)):
		massa_molecular += tabela_elementos[listaatomoelemento[i][0]] * listaatomoelemento[i][1]
	massa_molecular
	for j in range(len(listaatomoelemento)):
		proporcao = 0.0
		proporcao = (tabela_elementos[listaatomoelemento[j][0]] * listaatomoelemento[j][1]) / float(massa_molecular) * 100
		#print listaatomoelemento[j]
		print '%s=%.2f' % (listaatomoelemento[j][0],proporcao)



if __name__ == '__main__':
	while True:
		lista_atomo_elemento = []
		element = raw_input('')
		if element == 'fim': break
		#elemento = elemento.upper()
		element = element.split()
		i = 0
		elemento = []

		for k in range(len(element)):
			c = ''
			if len(element[k]) == 2:
				c += element[k][0].upper() + element[k][1].lower()
			else:
				c += element[k][0].upper()
			elemento.append(c)

		if len(elemento) <= 1:
			atomoelemento = (elemento[0],1)
			lista_atomo_elemento.append(atomoelemento)
		else:
			while i < (len(elemento)-1):
				atomo = 1
				element = ''
				if str.isdigit(elemento[i+1]) == True:
					atomoelemento = (elemento[i],int(elemento[i+1]))
					lista_atomo_elemento.append(atomoelemento)
					i += 2
				else:
					atomoelemento = (elemento[i],atomo)
					lista_atomo_elemento.append(atomoelemento)
					i += 1
				if i == len(elemento)- 1 and str.isdigit(elemento[len(elemento)-1]) == False:
					atomoelemento = (elemento[len(elemento)-1],atomo)
					lista_atomo_elemento.append(atomoelemento)
		massa_molecular(tabela_elementos,lista_atomo_elemento)
		print '---'



