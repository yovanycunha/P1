#coding: utf-8
# Média Final
# (C) 2016, Yovany Cunha/UFCG, Programaçao I
import math

ultimoMT = float(raw_input())
qMT= int(raw_input())

if (qMT == 1):
	print '%.1f. Ainda não aprovado.' % ultimoMT
else:
	mediap = float(raw_input())
	media = ultimoMT*0.6 + mediap*0.4
	if(media>=6.0):
		print '%.1f. Aprovado.' % media
	else:
		print '%.1f. Ainda não aprovado.' % media
