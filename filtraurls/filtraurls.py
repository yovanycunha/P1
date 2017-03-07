#coding: utf-8
# Filtra URLs
# (C) 2016, Yovany Cunha/UFCG, Programaçao I

def filtra_urls(links):
	link_google = 'google.com'
	google_acess = []
		
	for m in range(len(links)):
		is_substring(links[m],link_google)
		if is_substring(links[m],link_google):
			google_acess.append(links[m])
	return google_acess

def is_substring(palavra1,palavra2):
	pos_compair = 0
	count_compair = 0
	tem_sub = False
	for i in range(len(palavra2)):
		for l in range(pos_compair,len(palavra1)):
			if palavra2[i] == palavra1[l]:
				#print palavra1[l]
				pos_compair = l
				count_compair += 1
				break
	if count_compair == len(palavra2):
		return True
	else:
		return False




p1 = ['www.uol.com','www.google.com','http://mail.google.com']
print filtra_urls(p1)# == ['www.google.com','http://mail.google.com']
