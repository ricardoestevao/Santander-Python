# CRIAÇÃO DE MÓDULOS PRÓPRIOS

# Além de utiliar os módulois padrão do Python, também podemos criar nossos próprios módulos para organizar e reutilizar nosso código. 

# CRIAR E UTILIZAR MÓDULOS PERSONALIZADOS.

# Para criar um módulo personalizado, simplesmente criamos um novo arquivo Python com nome desejado e definimos as funções, classes e variáveis que queremos incluir no módulo.
# Por exemplo, criamos um arquivo(no mesmo diretório onde estamos executando Python) chamado meu_modulo.py com o segunte conteúdo. 

import meu_modulo

meu_modulo.saudar('Ricardo') # Imprime o nome que for inserido
resultado = meu_modulo.calcular_soma(5, 10)
print(resultado) # Imprime o valor colocado como parâmetro da soma. 
# Neste exemplo, importa-se o módulo meu_modulo e utilizam-se as funções saudar() e calcular_soma() definidas nele.
print('_' * 130)

# ORGANIZAÇÃO DO CÓDIGO EM MÓDULOS

# À medida que nossos programas crescem em tamanho e complexidade, é uma boa prática organizar nosso código em módulos separar segundo sua funcionalidade. Isso nos
# Permite manter um código mais legível, agrupado em módulos e fácil de manter. 
# Por exemplo, podemos ter um módulo operacoes.py que contenha funções relacionadas com operações matemáticas, e outro utilidades.py que contenha funções de uso geral. 

import operacoes
import utilidades

resultado = operacoes.somar(5, 5)
print(f'O resultado da soma é {resultado}')

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f'Olá, {nome}')

#Ao organizar nosso código em módulos, podemos reutilizar funções e manter um código mais estruturado e agrupado em módulos. 