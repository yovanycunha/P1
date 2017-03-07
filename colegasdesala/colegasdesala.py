#coding: utf-8
# Colegas de Sala
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def colegas_de_sala(salasprofs, professor):
	colegas = []
	for i,j in salasprofs.iteritems():
		if i != professor and j == salasprofs[professor]:
			colegas.append(i)
	print colegas	
	return colegas


salasprofs = {'Franklin': 206,'Tiago':206,'Eliane': 206,'Adalberto':209,'Wilkerson':207,'Dalton': 204,'Jorge': 204}

assert set(colegas_de_sala(salasprofs, 'Franklin')) == set(['Tiago', 'Eliane'])
assert set(colegas_de_sala(salasprofs, 'Adalberto')) == set([])

