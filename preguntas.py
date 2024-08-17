"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

with open('data.csv', 'r') as f:
    file = f.readlines()

matriz = []

for fila in file:
    elemento = fila.split('\t')
    elemento[-1]  = elemento[-1].replace('\n', '')
    matriz.append(elemento)



def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    rta = 0

    for i in matriz:
        rta += int(i[1])

    return rta



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    diccionario = dict()

    for fila in matriz:
        letra = fila[0]

        if letra in diccionario.keys():
            diccionario[letra] += 1

        else:
            diccionario[letra] = 1

    diccionario = sorted(diccionario.items())

    return diccionario



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    diccionario = dict()

    for fila in matriz:
        letra = fila[0]

        if letra in diccionario.keys():
            diccionario[letra] += int(fila[1])

        else:
            diccionario[letra] = int(fila[1])

    diccionario = sorted(diccionario.items())

    return diccionario


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    diccionario = dict()

    for fila in matriz:
        letra = fila[2][5:7]
    
        if letra in diccionario.keys():
            diccionario[letra] += 1

        else:
            diccionario[letra] = 1
            
    diccionario = sorted(diccionario.items())

    return diccionario


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    letras = []
    diccionario = []

    for fila in matriz:
        letras.append(fila[0])

    letras = sorted(list(set(letras)))
        
    for letra in letras:
        diccionario.append([letra, 0, 10000])

    for elemento in matriz:
        num = int(elemento[1])
        letra = elemento[0]

        for i in range(len(diccionario)):
            if letra == diccionario[i][0]:

                if num < diccionario[i][2]:
                    diccionario[i][2] = num

                elif num > diccionario[i][1]:
                    diccionario[i][1] = num
    
    final = []
    for i in diccionario:
        final.append((i[0], i[1], i[2]))

    return final


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    minimos = dict()
    maximos = dict()
    elementos = set()

    for elemento in matriz:
        
        a = elemento[-1].split(',')

        for j in range(len(a)): 
            par = a[j].split(':')
            num = int(par[1])


            if par[0] in elementos:
                
                

                if num <= minimos[par[0]]:
                    minimos[par[0]] = num

                if num >= maximos[par[0]]:
                    maximos[par[0]] = num

            else:
                elementos.add(par[0])
                minimos[par[0]] = num
                maximos[par[0]] = num

    elementos = sorted(list(elementos))
    final = []

    for i in elementos:
        final.append((str(i), minimos[i], maximos[i]))

    return final

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    elementos = {str(l) : [] for l in range(10)}

    for i in matriz:
        elementos[i[1]].append(i[0])

    final = []

    for i in list(elementos.items()):
        final.append((int(i[0]), i[1]))

    return final

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """


    elementos = {str(l) : set() for l in range(10)}

    for i in matriz:
        elementos[i[1]].add(i[0])

    for i in range(10):
        i = str(i)
        elementos[i] = list(elementos[i])
    
    final = []

    for i in list(elementos.items()):
        final.append((int(i[0]), i[1]))

    return final


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    cantidad = dict()

    for elemento in matriz:

        lista = elemento[-1].split(',')

        for par in lista:

            e = par[0]*3
            if e in cantidad:
                cantidad[e] += 1
            else:
                cantidad[e] = 1


    return dict(sorted(cantidad.items()))



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    final = []
    for i in matriz:
        final.append((i[0], len(i[-2].split(',')), len(i[-1].split(','))))

    return final




def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """


    diccionario = dict()

    for fila in matriz:

        for letra in fila[3].split(','):
    
            if letra in diccionario.keys():
                diccionario[letra] += int(fila[1])

            else:
                diccionario[letra] = int(fila[1])

    diccionario = dict(sorted(diccionario.items()))

    return diccionario




def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    final = dict()

    for fila in matriz:
        suma = sum([int(y.split(':')[1]) for y in fila[-1].split(',')])
        letra = fila[0]

        if letra in final:
            final[letra] += suma
        
        else:
            final[letra] = suma

    return dict(sorted(final.items()))
