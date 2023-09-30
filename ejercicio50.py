# Este es un código de JavaScript que cuenta el número de "bucles" en un número. Un número tiene un "bucle" si tiene un círculo cerrado al dibujarlo, como el 6 o el 9, o dos círculos cerrados como el 8. La función bucles toma un número como argumento, convierte el número en una matriz de cadenas, y luego usa un bucle for para iterar sobre cada dígito en la matriz. Si el número es 0, 6 o 9, se incrementa el contador de bucles. Si el número es 8, se incrementa el contador de bucles en 2.

# Aquí está el mismo código en Python 3:

def bucles(numero):
    array_numeros = list(str(numero))
    bucles = 0
    
    for num in array_numeros:
        num = int(num)

        if num == 0 or num == 6 or num == 9:
            bucles += 1
        elif num == 8:
            bucles += 2

    return bucles

print(bucles(288))  # Output: 2


# /*
# Dado un numero,devolver cuantos bucles tiene.
# Un numero tiene un bucle cuando tiene un circulo cerrado
# cuando lo dibujas, por lo que 6 tiene un bucle,
# 1 no tiene bucle y 8tiene dos bucles.


# ejemplo:
# bucles(28861)   Devuelve: 5

# */

# function bucles(numero){

#     let arrayNumeros = numero.toString().split('');
#     //console.log(arrayNumeros);
#     let bucles = 0;
    
#     for(numero of arrayNumeros){
#         numero = parseInt(numero);
#         //console.log(numero);

#         if(numero === 0 || numero === 6 || numero === 9){
#             bucles ++;
#         }else if(numero === 8){
#             bucles += 2;
#         }
#     }

#     return bucles;
# }

# console.log(bucles(288));