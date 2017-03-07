def meu_in(str_sigla,lista_siglas):
    for i_sigla in lista_siglas:
        if i_sigla == str_sigla:
            return True
    return False

def eh_roteiro(iata,voos,roteiro):
    cidades = roteiro.split("/")

    for i_cidades in range(len(cidades)-1):
        destinos = voos[iata[cidades[i_cidades]]]
        for i_destinos in range(len(destinos)):
            prox_destino = iata[cidades[i_cidades + 1]]
            if meu_in(prox_destino,destinos) == False:
                return False
    return True


iata = {"Campina Grande": "CPV","Recife": "REC","Salvador": "SSA","Brasilia": "BSB","Sao Paulo": "GRU","Rio de Janeiro": "GIG"}


voos = {"CPV": ["REC", "SSA"],"REC": ["CPV", "BSB", "GRU", "GIG"],"SSA": ["REC", "GRU", "GIG"],"BSB": ["CPV", "GIG", "GRU"],"GRU": ["GIG", "BSB"],"GIG": ["GRU", "REC"]}

assert eh_roteiro(iata, voos, "Campina Grande/Recife/Rio de Janeiro")
assert eh_roteiro(iata, voos, "Sao Paulo/Rio de Janeiro/Recife/Brasilia")
assert not eh_roteiro(iata, voos, "Recife/Rio de Janeiro/Salvador/Recife")
assert not eh_roteiro(iata, voos, "Campina Grande/Campina Grande")
assert not eh_roteiro(iata, voos, "Rio de Janeiro/Salvador/Recife")
assert eh_roteiro(iata, voos, "Campina Grande/Recife/Campina Grande")
assert not eh_roteiro(iata, voos, "Campina Grande/Brasilia")
assert eh_roteiro(iata, voos, "Brasilia/Campina Grande")
