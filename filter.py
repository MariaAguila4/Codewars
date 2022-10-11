numbers = [1, 2, 3, 4, 5, 6, 7]

# the lambda function returns True for even numbers
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)


def my_filter(elements, predicate):
    """
    recibe una lista y un predicado. devuelve otra lista con aquellos elementos
    que superan el test del predicado
    """
    accum = [] #qué se va acumulando? cial es el valor inicial?
    for element in elements:
      if predicate(element) == True:
        accum.append(element) # qué se hace en con cada elemento??
    return accum
print(my_filter([1,2,3,4,5,6], lambda x: (x%2 == 0)))