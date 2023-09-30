def al_cuadrado(numeros):
    numeros_cuadrados = [num ** 2 for num in numeros if isinstance(num, (int, float))]
    return numeros_cuadrados
numeros = [23, 56, 77, "hola", True, ["hola"], 80]
print(al_cuadrado(numeros))

# La salida esperada de este código es:


# [529, 3136, 5929, 6400]

# /*

# Como hacerlo:
# -Crear una funcion con parametro numeros
# -Filtrar array
# -Modificar contenido aeeay
# -Devolver resultado

# */

# function alCuadrado(numeros){

#     let numeros_cuadrados = numeros
#         .filter(numero => typeof numero === "number")
#         // con map metemos resultados pow elevar al cuadrado en array con .map
#         .map(numero => Math.pow(numero, 2))
#     ;

#     return numeros_cuadrados;
# }

# console.log(alCuadrado([23, 56, 77, "hola", true, ["hola"], 80]));