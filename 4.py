SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

valor_Total = SP + RJ + MG + ES + Outros
#porcentagem = (valor_especifico / valor_total) * 100

print(f'São Paulo foi {round((SP/valor_Total) * 100, 2)}%')
print(f'Rio de Janeiro foi {round((RJ/valor_Total) * 100, 2)}%')
print(f'Minas Gerais foi {round((MG/valor_Total) * 100, 2)}%')
print(f'Espirito Santo foi {round((ES/valor_Total) * 100, 2)}%')
print(f'Os Outros Estados foi {round((Outros/valor_Total) * 100, 2)}%')