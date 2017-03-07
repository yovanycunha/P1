#coding: utf-8
# Inverte Dicionário
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def insere_ordenado(elem,lista_elem):
    for i_elem in range(len(lista_elem)):
        if lista_elem[i_elem] > elem:
            lista_elem.insert(i_elem,elem)
            return

def inverte_dicionario(dic):
    invertido = {}
    for i,j in dic.iteritems():
        if invertido.has_key(j):
            if invertido[j][-1] < i:
                invertido[j].append(i)
            else:
                insere_ordenado(i,invertido[j])

        else:
            invertido[j] = [i]
    return invertido

#def test_exemplo(self):
#	m = {"A": 2, "b": 3, "a": 2}
#	assert inverte_dicionario(m) == {2: ["a", "c"],3: ["b"]}
#	n = {"b": 2 , "a":2 , "c":2}
#	assert inverte_dicionario(n)
m = {"A": 2, "b": 3, "a": 2}
assert inverte_dicionario(m)# == {2: ["a", "c"],3: ["b"]}

