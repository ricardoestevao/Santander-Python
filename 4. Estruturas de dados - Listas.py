# Estruturas de dados

# As estruturas de dados nospermitem organizare armazenar dados de maneira eficiente em nossos programas. Python fornece várias estruturas de dados integradas, como listas
#tuplas, dicionários e conjuntos, cada uma com suas próprias características e usos. 

# Listas

# Uma lista é uma estrutura de dados mutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma lsita podem ser de diferentes tipos de dados
# e são encerrados entre colchetes'[]', separados por vírgulas. 

# Criação e Acesso

# Para criar uma lsita, simplesmente encerre os elementos entre colchetes: 
print('Para criar uma lista,simplesmente encerre os elementos entre colchetes: ')
frutas = ['Maça', 'Banana', 'Laranja']
print(frutas)

print('\nPara acessar os elementos de uma lista, utiliza o indice do elemento entre colchetes. Os ìndices começam a partir do 0.')
print(frutas[0]) # Imprime "Maça"
print(frutas[1]) # Imprime "Banana"
print(frutas[2]) # Imprime "Laranja"

print('\nVocê também pode acessar os elementos a partir dofinal da lista utilizando índices negativos.O índice -1 representaoúltimo elemento e assim por diante.')
print(frutas[-1]) # Imprime "Laranja"
print(frutas[-2]) # Imprime "Banana"
print(frutas[-3]) # Imprime "Maça"

# Métodos de listas

# As listas em Python têm vários métodos incorporados que nos permitem manipular e modificar os elementos da lista. Alguns métodos comuns são: 
# append(elemento): adiciona um elemento ao final da lista.
# insert(indice, elemento): insere um elemento em uma posição específica da lista. 
# remove(elemento): remove a primeira ocorrência de um elemento na lista. 
# pop(indice): remove e retorna o elemento em uma posição específica da lista. 
# sort(): ordena os elementos da lista em ordem crescente. 
# reverse(): inverte a ordem dos elementos da lista. 

print('\nExemplo: ')
frutas = ['Maça', 'Banana', 'Laranja']
frutas.append('Pera') #Irá adicionar a Pera ao final da lista. 
print(frutas)

print('\nExemplo: ')
frutas.insert(1, 'Uva') #Irá adicionar a "Uva" no índice 1
print(frutas)

print('\nExemplo: ')
frutas.remove('Banana') # irá remover a banana da lista
print(frutas)

print('\nExemplo: ')
frutas_removida = frutas.pop(2)
print(frutas) # Imprime "maçã", "uva","pera"
print(frutas_removida) # Imprime "laranja"

print('\nExemplo: ')
frutas.sort() # irá ordenar os elementos da lista em ordem crescente. 
print(frutas)

print('\nExemplo: ')
frutas.reverse()
print(frutas) # irá inverter a ordem dos elementos da lista. 

# Lista de compreensão

# As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequência existente. Permitem filtrar e tranformar os elementos de uma lista em
# uma única linha de código.

# nova_lista = [expressão for elemento in sequência if condição]

print('\nExemplo: Neste exemplo, é criada uma nova lista chamada quadrados, que contém os quadrados dos números pares da lista números. ' \
'A expressão x ** 2 eleva cada elemento ao quadrado, e a condição if x % 2 == 0 filtra apenas os números pares.')
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)