def pares(numeros):
    return {
        "pares": [num for num in numeros if num % 2 == 0],
        "impares": [num for num in numeros if num % 2 != 0]
    }

print(pares([1,2,3,4,5,6,7,8100, 753]))

# Este código utiliza una sintaxis similar a la de JavaScript para crear un diccionario con dos claves: "pares" e "impares". Los valores asociados a estas claves son listas de números pares e impares, respectivamente. Para obtener estas listas, se utiliza la comprensión de listas en Python, que es similar al método filter en JavaScript.

# //Dado un array de numeros,devolver un array nuevo conlos numero pares e impares separados
# /*
# ejemplo:
# pares([1,2,3,4])

# Devuelve:
# {
#     pares:[2,4]
#     impares:[1,3]
# }
# */

# function pares(numeros){
#     return{
#         pares: numeros.filter(num => num % 2 === 0),
#         impares: numeros.filter(num => num % 2 !== 0)
#     }
# }

# console.log(pares([1,2,3,4,5,6,7,8100, 753]));