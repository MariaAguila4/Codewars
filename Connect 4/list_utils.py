import re

# Funciones para:
# 1. Detectaremos la presencia de UNA instancia del elemento dentro de una lista, en cualquier posición.
# 2. Detectaremos la presencia de N instancias dentro de una lista, en cualquier posición
# 3. Detectaremos la presencia de N elementos SEGUIDOS dentro de una lista.

def find_one(list, needle):
    """
    Devuelve True si encuentra a needle en la lista en alguna posición
    Sino, devuelve False
    """
    # inicializo el contador y el booleano que indica si se cumple o no la condición
    found = False
    index = 0
    # me recorro la lista mientras no encuentre a la aguja
    while not found and index < len(list):
        # comprueba a ver si el elemento actual es la aguja
        if needle == list[index]:
            # si lo es, actualizo found
            found = True
            #return True
        else:
            found = False
            #return False
        # avanzamos al siguiente elemento
        index = index + 1

    # devolvemos el resultado guardado en found
    return found


def find_n(list, needle, n):
    # inicializo el contador de veces que lo he encontrado
    # inicializo el indice del elemento actual
    index = 0
    count = 0
    # mientras no haya encontrado n veces y no haya terminado la lista
    while count < n and index < len(list):
        # si la encuento, actualizo el contador
        if needle == list[index]:
            count = count + 1

        # pase lo que pase, actualizo el contador
        index = index + 1

    # devuelvo el resultado de comparar n con el contador
    return count >= n
print(find_n([1,2,3,4], 'a',3))

def find_streak(list, needle, n):
    """
    Devuelve True si en list hay n o más needles seguidos
    False, para to do lo demás
    """
    # si n >= 0
    if n >= 0:
        # Inicializo el indice, el contador y el indicador de racha
        index = 0
        count = 0
        streak = False

        # Mientras no haya encontradoa n seguidos u la lista no se haya acabao....
        while count < n and index < len(list):
            # si lo encuentro, activo el indicado de rachas y actualizo el contador
            if needle == list[index]:
                streak = True
                count = count + 1
            else:
                # si no lo encuentro, desactivo el indicador de de racha y pongo a cero el contador
                streak = False
                count = 0

            # avanzo al siguiente elemento
            index = index + 1

        # devolvemos el resultado de comparar el contador con n SIEMPRE Y CUANDO  estemos en racha
        return count >= n and streak
    else:
        # para valores de n < 0, no tiene sentido
        return False


def first_elements(list_of_lists):
    """
    Recibe una lista de listas y devuelve una lista
    con los primeros elementos de la original
    """
    return nth_elements(list_of_lists, 0)


def nth_elements(list_of_lists, n):
    """
    Recibe una lista de listas y devuelve una lista
    con los enésimos elementos de la original
    """
    result = []
    for list in list_of_lists:
        result.append(list[n])
    return result


def transpose(matrix):
    """
    Recibe una matriz y devuelve su transpuesta
    """
    # Creo un amatriz vacía y la llamo transp
    transp = []
    # Recorremos todas las columnas de la matriz original
    for n in range(len(matrix[0])):
        # extraigo los elementos enésimos y los encasqueto a transp
        transp.append(nth_elements(matrix, n))
    # devuelvo trnasp
    return transp


def displace(l, distance, filler=None):
    if distance == 0:
        return l
    elif distance > 0:
        filling = [filler] * distance
        res = filling + l
        res = res[:-distance]
        return res
    else:
        filling = [filler] * abs(distance)
        res = l + filling
        res = res[abs(distance):]
        return res


def displace_matrix(m, filler=None):
    # creamos una matriz vacía
    d = []
    # por cada calumna de la matriz original la desplazamos su índice -1
    for i in range(len(m)):
        # añadimos la columna desplazada a m
        d.append(displace(m[i], i - 1, filler))

    # devolvemos d
    return d


def reverse_list(l):
    return list(reversed(l))


def reverse_matrix(matrix):
    rm = []
    for col in matrix:
        rm.append(reverse_list(col))
    return rm


def all_same(l):
    """
    Devuelve True si todos los elemenmtos de la lista son iguales
    o la lista está vacía
    """
    if l == []:
        return True
    else:
        same = True
        first = l[0]
        for elt in l:
            if elt != first:
                same = False
                break
        return same


def collapse_list(l, empty='.'):
    """
    Concatena todas las cadenas de la lista en una sola lista
    """
    collapsed = ''
    for elt in l:
        if elt == None:
            collapsed = collapsed + empty
        else:
            collapsed = collapsed + elt
    return collapsed


def collapse_matrix(m, empty='.', fence='|'):
    """
    Conatena todas las cadenas en una sola separada por |
    """
    collapsed = ''
    for elt in m:
        collapsed = collapsed + fence + collapse_list(elt, empty)

    return collapsed[1:]


def replace_all_in_list(original, old, new):
    """
    Cambia todas las ocurrencias de old por new
    """
    result = []
    for elt in original:
        if elt == old:
            result.append(new)
        else:
            result.append(elt)
    return result


def replace_all_in_matrix(original, old, new):
    """
    Aplica replace_all_in_list a todas las listas
    """
    result = []
    for each_list in original:
        result.append(replace_all_in_list(each_list, old, new))
    return result


