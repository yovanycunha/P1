# coding: utf-8
# Mais Consoantes
# (C) 2016, Yovany Cunha / UFCG, Programação 1

palavra = 0

while True:
	word = raw_input('')
	palavra += 1
	consoantes = 0
	vogais = 0
	for i in range(len(word)):
		if word[i] == 'A' or word[i] == 'E' or word[i] == 'I' or word[i] == 'O' or word[i] == 'U' or word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
			vogais += 1
		else:
			consoantes += 1

	if consoantes > vogais: break
	

print palavra
