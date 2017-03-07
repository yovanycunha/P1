#coding: utf-8
# Média Final
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

import math
Nota1 = float(raw_input())
Nota2 = float(raw_input())
Nota3 = float(raw_input())
Peso1 = float(raw_input())
Peso2 = float(raw_input())
Peso11 = float(Peso1/100)
Peso22 = float(Peso2/100)
Peso3 = 100 - Peso1 - Peso2
Peso33 = float(Peso3/100)

MediaFinal = (Nota1*Peso11 + Nota2*Peso22 + Nota3*Peso33) / float(Peso11 + Peso22 + Peso33)


print ("Média Final: %.1f") % (MediaFinal)

