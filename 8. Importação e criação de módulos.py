# IMPORTAÇÃO E CRIAÇÃOP DE MÓDULOS

# Em Python, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas. A importação de módulos nos permite
# Acessar a funcionalidade definida emoutros arquivos e reutilizar código de maneira eficiente. Além disso, podemos cirar nossos próprios módulois para organizar e modularizar nosso código. 

# IMPORTAR MÓDULOS

# Para utilizar um módulo em nosso programa, devemos importa-lo utilizando a declaração import. Podemos importar um  módulo completo ou funções específicas de um módulo. 

import math

resultado = math.sqrt(81) # Módulo SQRT que calcula a raiz quadrada de 81
print(resultado)
# Neste exemplo, importa-se o módulo math utilizando a declaração import. Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz quadrade de 25.
# Também podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função. 

from math import sqrt

resulta = sqrt(25)
print(resulta) # Imprime 5.0
# Neste caso, importa=se apenas a função sqrt() do módulo math, o  que nos permiteza utilizá-la diretamente sem ter que precedê-la com o nome do módulo. 
print('_' * 130)

# FUNÇÕES E CLASSES DE MÓDULOS PADRÃO 

# A biblioteca padrão de Python oferece uma ampla gama de módulos com funções e classes úteis. Alguns exemplos comuns incluem: 
# MATH - Fornece funções matemáticas, como sqrt()(raiz quadrada), sin()(seno), cos()(cosseno), entre outros...
# RANDOM - Ofere funções para ferar números aleatórios, como random()(número aleatório entre 0 e 1), randint()(número inteiro aleatório em um intervalo), entre outros..
# DATETIME - Permite trabalhar com datas e horas, como datetime.now()(data e hora atual), datetime.date()(data), datetime.time()(hora), entre outros... 
print('\n')
import random
import datetime

numero_aleatorio = random.randint(1, 10) # Irar gerar números aleatórios entre 1 ao 10 
print(numero_aleatorio)

data_atual =datetime.datetime.now()
print(data_atual)

# Esestão apenas alguns exemplis dos muitos módulos disponíveis na biblioteca padrão de Python. Você pode consultar a documentação oficial de Python para obter mais informaç~pes sobre os módulos e sua funcionalidades. 