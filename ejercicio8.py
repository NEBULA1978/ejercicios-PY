def invertir_numero(numero):
    invertido = int(str(abs(numero))[::-1]) * (-1 if numero < 0 else 1)
    return invertido

print("El numero invertido es", invertir_numero(-1256))


# /*
# Dado un numero entero, inviertelo y devuelve el nuevo entero.

# Ejemplos:
# invertir(67)  //Devuelve: 76


# Como Hacerlo:
# -Funcion que reciba el nunero
# -Convertir numero en string
# -Crear un array para cada letra
# -Darle la vuelta
# -Unir el array en un sring
# -Convertir el string en un entero

# */

# function invertirNumero(numero){

#     let invertido = parseInt(numero
#                         .toString()
#                         .split('')
#                         .reverse()
#                         .join('')
#                         ) * Math.sign(numero);

#     //console.log(typeof(invertido));
#     return invertido;
# }

# console.log("El numero invertido es", invertirNumero(-1256));