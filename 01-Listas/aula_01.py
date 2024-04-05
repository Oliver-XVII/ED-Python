'''
Estruturas de Dados Python - Aula 01:

    - Listas: As listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. 


    Tipos de Índice de uma lista:

        Para localizarmos um item numa lista utilizamos índices e estes podem ser valores positivos ou negativos.

    Índices Positivos: Começa no 0 se referindo ao primeiro valor da lista.

    Índices Negativos: Começa no -1, se referindo ao último valor da lista.


    Listas aninhadas:

    As listas podem armazenar todos os tipos de objetos Python, portando podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (Tabelas), e acessar informando os índices de linha e coluna.
    
    Fatiamento:

    Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve 'pular no acesso.

    Percorrer valores em uma lista: Utilizando a iteração, a saber, o comando for.

    Compreesão de listas:

    A compreensão de listas oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

Métodos da classe list

1º .append:
    Adiciona um elemento ao final da lista. Exemplos serão vistos no código abaixo:

2º .clear:
    Limpa a lista. Exemplos serão vistos no código abaixo:

3º .copy:
    Retorna uma cópia da lista. Exemplos serão vistos no código abaixo:

4º .count:
    Retorna a quantidade de vezes que um elemento aparece na lista. Exemplos serão vistos no código abaixo:

5º .extend:
    Adiciona um ou mais elementos ao final da lista. Exemplos serão vistos no código abaixo:

6º .index:
    Retorna o índice de um elemento na lista. Exemplos serão vistos no código abaixo:

7º .insert:
    Insere um elemento na lista. Exemplos serão vistos no código abaixo:

8º .remove:
    Remove um elemento da lista. Exemplos serão vistos no código abaixo:

9º .reverse:
    Inverte a ordem dos elementos da lista. Exemplos serão vistos no código abaixo:

10º .sort:
    Ordena a lista. Exemplos serão vistos no código abaixo:

11º .pop:
    Remove o último elemento da lista. Exemplos serão vistos no código abaixo:


'''



# =-=-=-=-=-=-=-=-=-=--=-=-=-= LISTAS DAS CORES =-=-=-=-=-=-=-=-=-=--=-=-=-=
cores = [
    'Azul',
    'Vermelho',
    'Amarelo',
    'Roxo'
]
print(cores)


# =-=-=-=-=-=-=-=-=-=--=-=-=-= LISTAS DAS PALAVRAS =-=-=-=-=-=-=-=-=-=--=-=-=-=
palavras = list(
    'python'
)
print(palavras)


# =-=-=-=-=-=-=-=-=-=--=-=-=-= LISTAS DOS NUMEROS =-=-=-=-=-=-=-=-=-=--=-=-=-=
numeros = list(
    range(10)
)
print(numeros)



# =-=-=-=-=-=-=-=-=-=--=-=-=-= LISTA DOS CARROS =-=-=-=-=-=-=-=-=-=--=-=-=-=
carro = [
    'Ferrari',
    'F8',
    4200000,
    2020,
    2900,
    "São Paulo",
    True
]
print(carro)


# =-=-=-=-=-=-=-=-=-=--=-=-=-= LISTA DAS MATRIZES =-=-=-=-=-=-=-=-=-=--=-=-=-=
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

matriz[0] # [1, 'a', 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # 'c'

# =-=-=-=-=-=-=-=-=-=--=-=-=-= LISTA DAS LISTAS =-=-=-=-=-=-=-=-=-=--=-=-=-=
lista = list(
    'python'
)
lista[2:] # ['t', 'h', 'o', 'n']
lista[:2] # ['p', 'y']
lista[1:3] # ['p', 't']

# =-=-=-=-=-=-=-=-=-=--=-=-=-= LISTA DOS CARROS =-=-=-=-=-=-=-=-=-=--=-=-=-=
carros = [
    'gol',
    'audi',
    'bmw',
    'toyota',
    'volkswagen'
]

for carro in carros:
    print(carro)


# =-=-=-=-=-=-=-=-=-=--=-=-=-= FILTRO =-=-=-=-=-=-=-=-=-=--=-=-=-=
numeros = [
    range(100)
]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# =-=-=-=-=-=-=-=-=-=--=-=-=-= Compreranger =-=-=-=-=-=-=-=-=-=--=-=-=-=

numerosNovos =  [
    range(100)
]

pares = [
    numero for numero in numerosNovos if numero % 2 == 0
]
# Elevando valores

numerosBase = [
    range(10)
]
quadrado = [
    numero ** 2 for numero in numerosBase
]


#  


lista_med = []
lista_med.append(1)
lista_med.append('Python')
lista_med.append([40, 30, 20])
print(lista_med)

lista_med2 = lista_med.copy()
print(lista_med2)

lista_med.clear()
print(lista_med)

coresDoExemplo = [
    'Azul',
    'Vermelho',
    'Amarelo',
    'Roxo',
    'Verde',
    'Azul',
    'Vermelho',
    'Amarelo',
    'Roxo',
    'Verde',
    'Azul',
    'Vermelho',
    'Roxo',
]

coresDoExemplo.count('Vermelho') #3
coresDoExemplo.count('Azul') #3


linguagens = [
    'Python',
    'C++',
    'Java',
    'C#',
]
linguagens.extend(['Js', 'PHP'])
print(linguagens)

linguagens.index("Java")

linguagens.remove('PHP')

print(linguagens)

linguagens.reverse()
print(linguagens)

linguagens.sort()
print(linguagens)

linguagens.pop()
print(linguagens)
