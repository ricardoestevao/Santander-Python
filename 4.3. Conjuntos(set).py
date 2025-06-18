# Conjutos (set)

# Um conjunto é uma estrutra de dados mutável e não ordenada que permiete armazenar uma coleção de elementos únicos. Os conjutos são delimitados por "{}" pi são criados
# utilizando a função set().

# Criação e operações básicas

print('Para criar um conjunto, utilize chaves ou função set():')

frutas = {'Maça', 'Banana', 'Laranja'}
numeros = set([1, 2, 3, 4, 5])

# Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}


intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}


diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}
 
def multiplicar (a,b):
    return a*b

