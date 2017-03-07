#coding: utf-8
# Fila de Atendimento
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def filas_de_atendimento(fila, medicos):
	contador = 0
	contador2 = 0
	atendimento = []
	while True:
		if contador == len(fila): break
		while True:
			atendimento.insert(contador,fila[contador])
			if contador == len(fila):
				return atendimento
			contador += 1
			contador2 += 1
			if contador2 == medicos:
				contador2 = 0
	return atendimento

fila_1 = ['Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia']
print filas_de_atendimento(fila_1, 3)# == [['Andre','Carlos'],['Antonio', 'Claudia'], ['Bianca']]
