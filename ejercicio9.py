def elementosComunes(array1, array2):
    filtrado = list(filter(lambda x: x in array2, array1))
    return filtrado

print(elementosComunes([4,5,6,7],[7,8,9,7,5]))
print(elementosComunes(["ramon","Paco","Pepe","Andres"],["juan","ramon","jesus","victor","Andres"]))


# /*

# Dados 2arrays ,devolver array consolo los elementos comunes 
# entrea ambos.

# Ejemplos:
# elementosComunes([4,5,6,7], [7,8,9,7,5])  // Devuelve: [5,7]

# Como hacerlo;
# -Funcion que reciba dos arrays
# -Filtrar array y evaluando una condicion
# -Devolver array nuevo


# */

# function elementosComunes(array1, array2){

#     const filtrado = array1.filter(elemento => {
#         return array2.includes(elemento);
#     });

#     return filtrado;
# }

# console.log(elementosComunes([4,5,6,7],[7,8,9,7,5]));
# console.log(elementosComunes(["ramon","Paco","Pepe","Andres"],["juan","ramon","jesus","victor","Andres"]));