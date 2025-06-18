#Tuplas

# Uma tupla é uma estrutura de dados imutável e ordenada quepermite armazenar uma coleção de elementos. Os elementos de uma tupla são encerrados entre parênteses ()
# separados por vírgulas. 

# Criação e Acesso
print('\nPara criar uma tupla, encerre oselementos entre parênteses: ')
ponto = (3, 4)
print(ponto)

# Para acessar os elementos de uma tupla, utilize o índice do elemento entre colchetes, similar às listas:
print(ponto[0])  # Imprime 3
print(ponto[1])  # Imprime 4

# A contrário das listas, as tuplas são imutáveis, o que significa que são podemser modificadas uma vez que criadas. Não se pode adicionar, eliminar ou alterar elementos 
# em uma tupla existente. 
# As tuplas são úteis quando você precisa armazenar uma coleção de elementos que são devem ser modificados, como coordernadas ou dados de configuração. 

# Métodos de tuplas

# Embora as tuplas sejam imutáveis, Python fornece vários métodos úteis para trabalhar com elas: 
# count(elemento): devolve o números de vezes que um elemento aparace na tupla.
# index(elemento): devolve o índice da primeira aparição de um elemento da tupla. Opcionalmente, pode-se espeficicar o início e fim da busca. 
# len(tupla): embora não seja um método de tuple propriamente dito, essa função incoporada devolve o comprimento da tupla.
print('\n')

minha_tupla = (1, 2, 3, 2, 4, 2)
print(minha_tupla.index(2)) # Imprime 1