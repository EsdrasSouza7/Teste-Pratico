import json

dados_Filtrados = []
maior_Faturamento = 0 
media = 0
i = 0
dias_Faturamento = 0

with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
#Filtrando os Dados
for da in dados:
    if da["valor"] > 0:
        dados_Filtrados.append(da)

#Coletando o Menor Faturamento
for dado in dados_Filtrados:
    if dado["valor"] > maior_Faturamento:
        maior_Faturamento = dado["valor"]

#Coletando o maior Faturamento
menor_Faturamento = maior_Faturamento
for dado in dados_Filtrados:
    if dado["valor"] < menor_Faturamento:
        menor_Faturamento = dado["valor"]

#Descobrindo A Media
for dado in dados_Filtrados:
    media += dado["valor"]
    i += 1
media = media/i
for dado in dados_Filtrados:
    if dado["valor"] > media:
        dias_Faturamento += 1

#Prints
print("O Menor Valor de Faturamento Foi:", menor_Faturamento)
print("O Maior Valor de Faturamento Foi:", maior_Faturamento)
print("O numero de Dias que o Faturamento foi acima da media foi:", dias_Faturamento)