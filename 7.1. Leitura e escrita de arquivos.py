# LEITURA E ESCRITA DE ARQUIVOS.

# Python nos permite ler e escrever dados em arquivos externos. Podemos abrir arquivos em diferentes modos, como leitura('r'), escrita ('w') ou anexar ('a'), e realizar operações de leitura e escritra. 

# LEITURA DE ARQUIVOS

# Para ler o conteúdo de um arquivo, primeirp devemos abrilo-lo utilizando a função open() em modo de leitura ('r'). Depois, podemos ler o conteúdo do arquivo utilizando
# métodos como read() ou readlines().

arquivo = open('dados.txt', 'r') # Cria=se uma variável para abrir o arquivo
conteudo = arquivo.read() # Cria-se outra variável para ler o arquivo
print(conteudo) # Imprime na tela o conteudo que está dentro do arquivo .txt
arquivo.close()

# Neste exemplo, o arquivo "dados.txt" é aberto em modo de leitura utilizando open(). Depois, todo o conteúdo do arqquivo é lido utilizando o método read() e armazenado
# na variável conteudo. Finalmente, o conteúdo é mostrado na tela e o arquivo é fechado utilizando o método close().
print('_' * 130)

# ESCRITA DE ARQUIVOS

# Para escrever dados em um arquivo, abrimos em modo de escrita('w') utilizando a função open(). Se o arquivo não existir, será criado automaticamente. 
# Se o arquivo já existir, seu conteúdo será sobrescrito. 

arquivo = open('dados.txt', 'w')
arquivo.write('Olá mundo!')
arquivo.close()

# Neste exemplo, o arquivo "dados.txt" é aberto em modo de escrita utilizando open(). Depois, a string "Olá mundo" é escrita no arquivo utilizando o método write().
# Finalmente, o arquivo é fechado utilizando o método close(). 
# Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática. 

with open('dados.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    print(conteudo)

# A entrada e saída de dados em Python nos oferece uma grande flexibilidadepara interagir com o usuárioe manipular arquivos externos. Podemos solicitar informações ao usuário,
# mostrar resultados natela e ler ou escrever dados em arquivos de texto. Lembre-se sempre manejar adequadamente a abertura e fechamento de arquivos, e considerar as 
# possíves exceções que podem ocorrer durante as operações de entrada/saída. 