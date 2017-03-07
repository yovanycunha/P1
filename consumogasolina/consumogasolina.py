#coding: utf-8
# Média Final
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

pos_ini = float(raw_input())
gas_ini = float(raw_input())
pos_final = float(raw_input())
gas_final = float(raw_input())

consumo = (pos_final-pos_ini)/(gas_ini-gas_final)

print 'O consumo total foi de %.1f km/l.' % consumo
