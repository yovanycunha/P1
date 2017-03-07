#coding: utf-8
# Mastery Learning
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

print 'Mastery Learning'
print 'Cálculo da nota na unidade\n'

nota1 = float(raw_input('Nota? '))
nota2 = float(raw_input('Nota? '))
media = (nota1 + nota2) / 2.0
#aux = 0
penalidade = 0.0

if media < 6.5:
	print 'Média: %.1f (cursando)' % media
else:
	print 'Média: %.1f (aprovado)' % media
print 'Penalização: %.1f\n' % penalidade

while True:
	if media >= 6.5: break
	num = float(raw_input('Nota? '))
	penalidade += 0.5
	if num > nota1:
		nota1 = num
		media = (nota1 + nota2)/ 2.0
		
	elif num > nota2:
		nota2 = num
		media = (nota1 + nota2) / 2.0

	if media < 6.5:
		print 'Média: %.1f (cursando)' % media
	else:
		print 'Média: %.1f (aprovado)' % media
	print 'Penalização: %.1f\n' % penalidade

print '==='
print 'Notas válidas: %.1f e %.1f' % (nota1,nota2)
print 'Média parcial na unidade: %.1f' % media
print 'Penalizações: %.1f' % penalidade
media2 = media - penalidade
print 'Média final na unidade: %.1f' % media2
