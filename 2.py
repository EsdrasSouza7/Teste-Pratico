res = 0
fib = 1
temp = 1
NumeroParaEncontrar = 3


while res < NumeroParaEncontrar:
    if res != 0:
        temp = res
    res = fib + res
    fib = temp

if res == NumeroParaEncontrar:
    print(f"O Numero {NumeroParaEncontrar} pertence ao sequencia Fibonacci.")
else:
    print(f"O Numero {NumeroParaEncontrar} NÃO PERTENCE ao sequencia Fibonacci.")
