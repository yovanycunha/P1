mapa = {"klaudio":"2008.1", "yovany":"2015.2", "clara":"2015.1", "raquel":"2015.1", "matheus":"2015.2", "tarsila":"2015.2", "luciana":"2015.2", "luciano":"2015.1"}
mapa_inv = {}
for elem in mapa.items():
	chave = elem[0]
	valor = elem[1]
	if valor not in mapa_inv.keys():
		mapa_inv[valor] = [chave]
	else:
		mapa_inv[valor] = mapa_inv[valor] + [chave]


colegas = []
nome = raw_input()
for elem in mapa_inv[mapa[nome]]:
	if elem != nome:
		colegas.append(elem)
#print mapa_inv[mapa[nome]]

print colegas
