Sting = 'Paralelepípedo'
numero_de_Letras = len(Sting)
reverso = ""

for n in range(numero_de_Letras):
    reverso += Sting[numero_de_Letras-n-1]

print(reverso)