# Exceções Personalziadas

# Além de exceções incorporadas no Python, você também pode cirar suas próprias exceções personalizadas. Isso é útil quando deseja lidar com situações específicas do seu programa. 

# Para criar uma exceção personalizada, você deve criar uma classe que herde da classe base Exception ou de uma de suas subclasses. 

def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do Erro")
try:
    funcao()
except Exception as e:
    print(f'Erro: {str(e)}')

# Neste exemplo, define-se uma função chamada funcao(). Dentro da função, verifica-se uma condição e, se for satisfeita, gera-se uma exceção utilizando a declaração raise.
# Em vez de criar uma classe personalizada, utiliza-se diretamente a classe base Exceotion para gerar a exceção. 

# Depois, tuiliza-se um bloco try-except para pacturar e lidar com a exceção. A variável e é utilizada para acessar a descrição do erro fornecida ao ferar a exceção.
# O tratamento de erros e exceções é uma parta fundamenta da programação em Python. Permite lidar com situações insperar de maneira controlada e evitar que seu programa trave ou para abruptamente. 
# Quando ocorre uma erro no seu código, o Oython gera uma exceção. Ao utilizar blocos try-except, você pode capturar e lidar com essas exceções de maneira adequada. 
# Pode espeficiar diferentes blocos e except para lidar com diferente tipos de exceções e realizar ações específicas em cada caso. 

# Além disso, o bloco finallypermite exceutar código de limpeza ou liberação de recursos, independentemente de ter ocorrido uma exceção ou não. 
# Isso é útil para garantir que certas ações sejams sempre realizadas, como fechar arquivos ou conexões de banco de dados. 
