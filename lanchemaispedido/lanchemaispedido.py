# coding: utf-8
# Lanche Mais Pedido
# (C) 2016, Yovany Cunha / UFCG, Programação 1


def lanchemaispedido(pedidos):
	mais_pedido = ''
	tem_saida = False
	for i in range(len(pedidos)):
		cont = 0
		var_ajuda = pedidos[i]
		print var_ajuda
		for l in range(len(pedidos)):
			if pedidos[l] == var_ajuda:
				cont += 1
		if cont > (len(pedidos)/2):
			mais_pedido = var_ajuda
			tem_saida = True
	print mais_pedido
	if tem_saida == True:
		return mais_pedido
	else:
		return None

ines = ['tapioca','tapioca','salada','bolo','misto','tapioca', 'tapioca']
marcos = ['suco','coxinha','suco','misto','folhado']
assert lanchemaispedido(ines) == 'tapioca'
assert lanchemaispedido(marcos) == None
