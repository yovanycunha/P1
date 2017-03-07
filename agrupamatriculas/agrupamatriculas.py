#coding: utf-8
# Agrupa Matrículas
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def agrupa_por_periodo(alunos):
	new = {}
	
	for i in range(len(alunos)):
		
		new[alunos[i][:3:]] = new.get(alunos[i][:3:],0) + 1
		
	
	return new

turma = [
    '0511114', '0521137', '0611001',
    '0611003', '0611004', '0621006',
    '0811007', '0811009', '0811502',
    '0811604', '0811605',
]
assert agrupa_por_periodo(turma) == {
    '051': 1,
    '052': 1,
    '061': 3,
    '062': 1,
    '081': 5,
}
