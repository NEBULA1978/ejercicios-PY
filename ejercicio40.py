def alto_bajo(numeros):
    ordenados = sorted(numeros)

    # dictionary
    return {
        'bajo': ordenados[0],
        'alto': ordenados[-1]
    }

print(alto_bajo([88, 100, 1, 2, 3, 43, 20, 12, 600, 900, 22]))

# In Python, function names are written in lowercase with words separated by underscores. The sorted function is used to sort the list in ascending order by default. The dictionary is created using curly braces {} with key-value pairs separated by colons. The negative index -1 is used to access the last element of the list. en castellano

# En Python, los nombres de las funciones se escriben en minúsculas con palabras separadas por guiones bajos. La función sorted se utiliza para ordenar la lista por defecto en orden ascendente. Los diccionarios se crean utilizando llaves {} con pares clave-valor separados por dos puntos. El índice negativo -1 se utiliza para acceder al último elemento de la lista.

# /////////////////////////
# /////////////////////////

# function altoBajo(numeros){

#     let ordenados = numeros.sort((a,b) => a - b);

#     //json
#     return {
#         bajo: ordenados[0],
#         alto: ordenados[ordenados.length -1]
#     }
# }

# console.log(altoBajo([88, 100, 1, 2, 3, 43, 20, 12, 600, 900,22]));