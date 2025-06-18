# Entradas/Saídas

# Em Python, a entrada e saída de dados nos permiteiterar com o usuário e manipular arquivos. Podemos solicitar informações ao usuário,
#  mostrar resultados na tela e ler ou escerver dados em arquivos externos. 

# ENTRADA DE DADOS DO USÚARIO

# Para obter informações do usuário durante a excução do programa, podemos utilizar a função input(). Esta função mostra uma mensagem natela e espera que o usuário insira um valor. 
nome = input('Insira seu nome: ')
idade = input('Insira sua idade: ')

print(f'Olá, {nome}!')
print(f'Você tem {idade} anos')
# Neste exemplo, solicita-se ao usuário que insira seu nome e idade utilizando a função input(). Os valores inseridos são armazenados nas variáveis nome e idade
# respectivamente. Em seguida, essas variáveis são tulizadas para mostraruma saudação personalizada na tela. 

print('_' * 130)
print('\n')
idade = int(input('Insira sua idade: '))

if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade')

# Neste exemplo, solicita-se ao usúario que insira sua idade e converte o valor inserido um número inteiro utilizando int(). Em seguida, utiliza-se uma estrutura 
# condicional para verificar se a idade é maior ou igual a 18 e mostrar uma mensagem correspondente. 
print('_' * 130)

# SAIDA DE DADOS

# Para mostrar informações na tela, utilizamos a função print(). Esta função recebe um ou mais argumentos e  os mostra no console. 
# Podemos utulizar a f-string(formatação de cadeia) para inserar variáveis diretamente dentro de uma cadeia de texto. 
nome = "Juan"
idade = 25

print(f'Olá meu nome é {nome} e tenho {idade} anos.')
# Neste caso, as variáveis são inseridas dentro da cadeira utilizando chaves{} e a cadeia é precedida pela letra f para inficar que é uma f-string. 