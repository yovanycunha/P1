#coding: utf-8
# Disciplinas de um Professor
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def disciplinas(alocacao,professor):
	disciplinas = []
	creditos = 0
	for i,j in alocacao.iteritems():
		turmas = 0
		for k in j:
			if k == professor:
				turmas += 1
		if turmas > 0:
			disciplinas.append(i[0])
			creditos += int(i[1]) * turmas
	carga = (disciplinas,creditos)
	return carga


alocacao = {("P1", 4): ['Jorge', 'Dalton','Wilkerson'],
         ("LP1", 4): ['Jorge', 'Dalton', 'Eliane', 'Wilkerson'],
         ("EVOL", 2): ['Dalton'],
         ("IC", 4): ['Eliane', 'Joseana'],
         ("P2", 4): ['Livia', 'Raquel', 'Nazareno'],
         ("GRAFOS", 2): ['Patricia', 'Patricia']}

assert set(disciplinas(alocacao, "Dalton")[0]) == set(['P1', 'LP1', 'EVOL'])
assert disciplinas(alocacao, "Dalton")[1] == 10
assert set(disciplinas(alocacao, "Eliane")[0]) == set(['LP1', 'IC'])
assert disciplinas(alocacao, "Eliane")[1] == 8
assert set(disciplinas(alocacao, "Patricia")[0]) == set(['GRAFOS'])
assert disciplinas(alocacao, "Patricia")[1] == 4


