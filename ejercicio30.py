def eliminarDuplicdos(elementos):
    elementos = list(filter(lambda x: isinstance(x, int), elementos))
    sin_duplicados = set(elementos)
    return list(sin_duplicados)

print(eliminarDuplicdos(["uno", "dos", 1, 2, 3, 3, 1, 4, "hola", 5]))
# The filter function in Python takes a function and a list as arguments and returns a new list with only the elements from the original list for which the function returns True. In this case, we're using the isinstance function to check if each element is an integer.

# The set function in Python creates a set, which is an unordered collection of unique elements. We're using it here to remove duplicates from the list of integers.

# Finally, we're converting the set back to a list using the list function, and returning the list. The output should be [1, 2, 3, 4, 5].

# La función filter en Python recibe como argumentos una función y una lista, y devuelve una nueva lista con solo los elementos de la lista original para los cuales la función devuelve True. En este caso, estamos usando la función isinstance para comprobar si cada elemento es un número entero.

# La función set en Python crea un conjunto, que es una colección desordenada de elementos únicos. La estamos usando aquí para eliminar los duplicados de la lista de enteros.

# Finalmente, estamos convirtiendo el conjunto de nuevo a una lista usando la función list, y devolviendo la lista. La salida debería ser [1, 2, 3, 4, 5].

# ///////////////////
# ///////////////////

# # function eliminarDuplicdos(elementos){
#     elementos = elementos.filter(elemento => {
#         return typeof elemento === "number";
#     });

#     let sin_duplicados = new Set(elementos);

#     return Array.from(sin_duplicados);
#     //return new Set(elementos);
#     //console.log(elementos);
# }

# console.log(eliminarDuplicdos(["uno", "dos", 1, 2 ,3, 3, 1, 4, "hola", 5]));