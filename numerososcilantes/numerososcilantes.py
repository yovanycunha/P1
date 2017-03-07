# coding: utf-8
# Números Oscilantes
# (C) 2016, Yovany Cunha / UFCG, Programação 1


def verifica_codigo(code):
	code_list = []
	seguro_ounao = True
	algarismos = 1
	while code >= 10:
		code_list.append(code % 10)
		code = code / 10
		algarismos += 1
	code_list.append(code)
	
	for i in range(1,len(code_list)):
		if code_list[i - 1] % 2 == 0 and code_list[i] % 2 == 0:
			seguro_ounao = False
			return 'falso: %d algarismos.' % algarismos
		elif  code_list[i - 1] % 2 != 0 and code_list[i] % 2 != 0:
			seguro_ounao = False
			return 'falso: %d algarismos.' % algarismos
	if seguro_ounao == True:
		return 'verdadeiro: %d algarismos.' % algarismos

if __name__ == '__main__':
	codigo = int(raw_input(''))
	print verifica_codigo(codigo)
