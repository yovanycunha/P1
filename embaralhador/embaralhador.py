# coding: utf-8
# Embaralhador
# (C) 2016, Yovany Cunha / UFCG, Programação 1


def intercalar(seq_cartas):
	aux = 0
	for i in range(0 ,(len(seq_cartas) - 1), 2):
		aux = seq_cartas[i + 1]
		seq_cartas[i + 1] = seq_cartas[i]
		seq_cartas[i] = aux
	imprime_lista(seq_cartas)

def girar_esquerda(seq_cartas):
	aux = seq_cartas[len(seq_cartas) - 1]
	seq_cartas.pop(len(seq_cartas) - 1)
	seq_cartas.insert(0,aux)
	imprime_lista(seq_cartas)

def girar_direita(seq_cartas):
	aux = seq_cartas[0]
	seq_cartas.pop(0)
	seq_cartas.insert(len(seq_cartas), aux)
	imprime_lista(seq_cartas)

def imprime_lista(seq):
	print seq[0],
	for i in range(1,len(seq)):
		print '%s' % seq[i],
	print


if __name__ == '__main__':
	sequencia_cartas = raw_input('').split()
	tipo_embaralha = raw_input('')
	while tipo_embaralha != 'fim':
		if tipo_embaralha == 'I':
			intercalar(sequencia_cartas)
			#modificadas.append(sequencia_cartas)
		elif tipo_embaralha == 'GE':
			girar_esquerda(sequencia_cartas)
			#modificadas.append(sequencia_cartas)
		elif tipo_embaralha == 'GD':
			girar_direita(sequencia_cartas)
			#modificadas.append(sequencia_cartas)

		tipo_embaralha = raw_input('')

	#for i in range(len(modificadas)):
		#print modificadas[i]
