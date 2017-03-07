#coding: utf-8
# Questões para P1
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

colaboradores = []
questoes = []
soma_total = 0
colaborador = raw_input('')
while colaborador != '**':
	colaboradores.append(colaborador)
	soma = 0
	questao = raw_input('')
	while questao != '*':
		questao = int(questao)
		soma += questao
		questao = raw_input('')
	soma_total += soma
	questoes.append(soma)
	colaborador = raw_input('')


print 'Relatório de novas questões:\n'

for i in range(len(colaboradores)):
	print '%s: %d' % (colaboradores[i],questoes[i])

print '---'
print 'Total de novas questões: %d' % soma_total
