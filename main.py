numeros = [10, 5, 7, 4, 6, 3, 8]

# classifica em ordem decrescente
numeros.sort(reverse=True)

for numero in numeros:
    print(numero)
# ou "print(numero, end=' _ ')"" para serarar na horizontal os numeros

media  =  sum(numeros)/len(numeros)

print(f'\nResultado da média: {media:,.2f}.')
