# coding: utf-8
# subtração de Polinômios
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def subtrai_polinomios(poli1,poli2):
	subtracao = []
	if len(poli1) <= len(poli2):
		for i in range(len(poli1)):
			if poli1[i]-poli2[i] != 0:
				subtracao.append(poli1[i]-poli2[i])
		for l in range(len(poli1),len(poli2)):
			subtracao.append(poli2[l]*(-1))
		return subtracao
	else:
		for i in range(len(poli2)):
			if poli1[i]-poli2[i] != 0:
				subtracao.append(poli1[i]-poli2[i])
		for l in range(len(poli2),len(poli1)):
			subtracao.append(poli1[l])
		return subtracao

		
#p1 = [-5, 4, 3]
#p2 = [-1, 0, 2, 0, 0, 0, 5]
#print subtrai_polinomios(p1, p2)# == [-4, 4, 1, 0, 0, 0, -5]

#p1 = [-5, 4, 3]  # 3x2 + 4x - 5
#p2 = [-4, 2, 3]  # 3x2 + 2x - 4
#print subtrai_polinomios(p1, p2)# == [-1, 2]  # 2x - 1

p1 = []  # 3x2 + 4x - 5
p2 = [0,0,0,0]  # 3x2 + 2x - 4
print subtrai_polinomios(p1, p2)# == [-1, 2]  # 2x - 1
