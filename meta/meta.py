#coding: utf-8
# Meta
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

meta_total = float(raw_input(''))
meta_individual = meta_total/6.0
vendas_total = 0.0
metas_func = []
bonus_func = []

for i in range(6):
	venda = float(raw_input(''))
	vendas_total += venda
	if venda >= meta_individual:
		metas_func.append(venda)
if vendas_total >= meta_total and len(metas_func) == 6:
	print 'Total de vendas: R$ %.2f (meta atingida)' % vendas_total
	print '----'
	print 'Bonificação:'
	for i in range(6):
		bonus = metas_func[i]/100.0
		bonus_func.append(bonus)
	for i in range(1,7):
		print 'Funcionário %d: R$ %.2f' % (i, bonus_func[i-1])	
else:
	print 'Total de vendas: R$ %.2f (meta não foi atingida)' % vendas_total
	print '----'

