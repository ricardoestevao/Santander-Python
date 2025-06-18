# As funções são blocos de código reutilizáveis que nos permitem encapsular rarefas específicas e execut=a-las quando necessário.
# as funções nos ajudam a organizar nosso código, evitar a repetição e fazer com que nossos programas sejam mais modulares e fáceis de manter. 

# Definicação e chamada de funções

# Para definir uma função em Python, utilizamos a palavr-chave def seguida do noma da função e parênteses. Opcioalmente, podemos especificar parêmetros dentro dos 
# parênteses. O bloco do código da função é indentado após os dois pontos. 

# Para chamar uma função, simplesmente escrevemos o nome da função seguido de parênteses: 

def saudacao():
    print('Olá, mundo!')

saudacao() # Imprime, "Olá, mundo!"

def media(*numeros):
    soma=sum(numeros)
    quantidade=len(numeros)
    media = soma / quantidade
    return media

print('Media:', media(10, 50, 30, 15))
#_________________________________________________________________________________________________________________________________________________________________________

# Parâmentros e argumentos

# As funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. Os parâmentros são especificados dentro dos parênteses na
# definição da função. 

def saudacao(nome):
    print(f'Olá, {nome}!')

print('\nAo chamar a função, fornecemos os argumentos correspondentes aos parâmetros:')
saudacao('Ricardo') # Imprime 'Olá, Ricardo!'
saudacao('Nair') # Imprime, 'Olá, Nair!'
#_____________________________________________________________________________________________________________________________________________________________________

# Valores de retorno

print('\nAs funções podem retornar valores usando a palavra-chave return. O valor de retorno pode ser usado pelo código que chama a função.')

def soma(a, b):
    return a + b

resultado = soma(2, 5)
print(resultado) # Imprime 7
#_______________________________________________________________________________________________________________________________________________________________________

# Funções anônimas(lambda)

print('\nPython permite criar funções anônimasou funções lambda, que são funções sem nome definidas em uma única linha. ' \
'São comumente usadas para funções pequenas e concisas.')

quadrado = lambda x: x ** 2
print(quadrado(9))# Imprime 91

adicao = lambda x: x + 3
print(adicao(5)) # imprime 8
#________________________________________________________________________________________________________________________________________________________________________

# Escopo das variáveis (local vs. global)

# As variáveis definidas dentro de uma função têm um espoco local, o que significa que só são acessíveis dentro da função. Por outro lado, as variáveis definidas
# fora de qualquer função têm um escopo global e podem ser acessadas de qualquer parte do programa. 

print('\n________________________________________________________________________________________________________________________________________')

def funcao():
    variavel_local = 10
    print(variavel_local) # Acessível dentro da função. 

varivel_global = 20

def funcao2():
    print(varivel_global) # Acessível de qualquer lugar.
funcao() # imprime 10
funcao2() # imprime 20
print(varivel_global) # Imprimi 20
print('______________________________________________________________________________________________________________________________________')

# Documentação de funções (docstrings)

# É uma boa prática documentos nossas funções utilizando docstrings. Os docstrings são cadeias de texto de descrevem o propósito, os parâmetros e os valor de retorno
# de uma função. São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas. 
print('\n')
def area_retagulo(base, altura):
    """
    Calcula a área de um retângulo.
    
    Args: 
        base (float): A base do retângulo.
        altura(float): A alturado retângulo.

    Returns:
        Float: A área do retângulo.
    """
    return base * altura
print(f'{area_retagulo(2, 6)}')
print('_' * 130)
# Funções com número variável de argumentos

print('Python permite definir funções que aceitem um número variável de argumentos. Isso é feito utilizando o operador * antes do nome do parâmetro. ')
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
print(soma_variavel(1, 2, 4))
print(soma_variavel(5, 6, 10, 19))

# As funções são uma ferramenta fundamental na programação e nos permitem estruturar e modularizar nosso código. Com a capacidade de definir funções personalizadas, podemos
# encapsular tarefas específicas e reitulizá-las em diferentes partes do nosso programa. 
# Além das funções definidas pelo usuário, Python também fornece uma amplas gama de funções incorporadas que podemos utilizar diretamente, como print(), len(), range() entre outros. 