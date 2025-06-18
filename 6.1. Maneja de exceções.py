# Maneja de exceções

# O manejo de exceções nos permite capturar e lidar com erros de maneira controlada utilizando as declarações try, except e opcionalmente finally.

# TRY

# O bloco try contém o código que pode gerar uma exceção. Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.

try:
    # Código que pode gerar uma exceção 
    resultado = 10 / 0 # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print('Erro: Divisão por zero')

print('\n')

# EXCEPT

# O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter múltiplos blocos except parar lidar com diferentes tipos de exceções. 

try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0 # divisão por zero
    print(resultado)
except ZeroDivisionError:
    print('Erro: Divisão por zero')
except ValueError:
    print("Erro: Valor inválido!")

# FINALLY

# O bloco finally é opcional e é executado sempre, indepedentemente de ter ocorrido uma exceção ou não. É comumennte utilizado para realizar tarefas de limpeza ou liberação de recursos.

try:
    # Código que pode gerar uma exceção
    arquivo = open('arquivo.txt', 'r')
    # Realizar operações com o arquivo
except FileNotFoundError:
    print('Erro: Arquivo não encontrado')
finally:
    arquivo.close() # Fecha o arquivo sempre, mesmo se ocorrer uma exceção. 