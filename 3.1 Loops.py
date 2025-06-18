# Os loops nos permitem repetir um bloco de código várias vezes. Em Python, os loops mais comuns são for e while.

#For

#O loop for é utilizado para iterar sobre uma sequência(como uma lista, uma tupla ou uma string) ou qualquer objeto iterável. A sintaxe básica é a seguinte: 
# for "variavel" in "sequência":
    #bloco de código a repetir 
    #instruções
#Exemplo: 

frutas = ["maça", "banana", 'laranja']

for frutas in frutas:
    print(frutas)

print('\nNúmeros de 1 a 5 multiplicados por 2 com a estrutura for:')
for numero in range(1, 6): 
    print(numero * 2)

# Neste exemplo, o loop for itera ("percorre") sobre a lista frutas. Em cada iteração, a variável fruta assume o valor de um elemento da lista, e o bloco de código dentro 
# do loop é executado. Neste caso, cada fruta é impressa em uma linha separada. 
#__________________________________________________________________________________________________________________________________

# While

# O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira. A sintaxe básica é a seguinte: 
# While condição: 
    # Bloco de código a repetir
    # instruções

# Exemplo

print('\nNúmeros de 1 a 5 multiplicados por 2 com a estrutura While')
contador = 1
while contador <5: 
    print(contador * 2)
    contador += 1
 
#Neste exemplo, o loop while é executado enquanto a variável contador for menor que 5. Em cada iteração, o valor do contador é impresso e depois incrementado em 1 pela
# instrução contador += 1. O loop será interrompido quando contador atingir o valor de 5.

# É importante ter cuidado ao usar o loop While, pos, se a condição nunca se tornar falsa, o loop será executado indefinidamente, o que é conhecido como um loop infinito. 
#__________________________________________________________________________________________________________________________________________________________________

# Controle de Loops
# Python fornece algumas instruções especiais para controlar o fluxo de execução dentro dos loops:

# Break
# A instrução break é utilizada para sair prematuramente de um loop, independentemente da condição. 
# Quando um break  é encontrado, o loop é interrompido e o fluxo de execução continua com a próxima instrução fora do loop. 

contador = 0
print('\nNeste exemplo, o loop while é executado indefinidamente devido à condição True. No entento, dentro do loop é utilizada uma estrutura condicional if para verificar' \
'se o contador é igual a 5.')
while True:
    print(contador)
    contador += 1

    if contador == 5:
        break

# Quando essa condição é satisfeita, a instrução break é executada, fazendo com que o loop seja interrompido e o fluxo de execução continue com a próxima instrução fora do loop.
#___________________________________________________________________________________________________________________________________________________________________

# Continue

# A instrução continue é utilizada para pular o restante do bloco de código dentro de um loop e passar para a próxma iteração. 
# Exemplo:
print('\nNeste exemplo, o loop for itera sobre os números de 0 a 9 utilizando a função range(). ' \
'Dentro do loop, verifica-se se o número é divisível por 2 utilizando o operador de módulo %. ' \
'Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada, ' \
'fazendo com que o restante do bloco de código seja pulado e passando para a próxima iteração do loop. Como resultado, apenas os números ímpares serão impressos.')

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print('\nPara exibir o resultado real da divisão sem executar o continue é só apagar o continue que o for será excutado normalmente.')

for i in range(10):
    if i % 2 == 0:
        print(i)
#______________________________________________________________________________________________________________________________________________________________________
# Pass

print('\nA instrução pass é uma operação nula que não faz nada.')

# Exemplo: 

for i in range(5):
    pass
    print(i)