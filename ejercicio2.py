def palindromo(texto):
    invertido = ''.join(reversed(texto))  # invertir la cadena
    return invertido == texto  # comprobar si la cadena invertida es igual a la original


print("¿Es un palíndromo?", palindromo("hola"))


# La función palindromo recibe un parámetro texto que es la cadena que queremos comprobar si es un palíndromo o no. En primer lugar, se invierte la cadena utilizando la función reversed, que devuelve un objeto iterable de los caracteres de la cadena invertidos. Luego, estos caracteres se unen utilizando la función join para formar una cadena invertida. Por último, se compara esta cadena invertida con la cadena original para determinar si es un palíndromo o no.

# Para probar la función, se utiliza la función print para imprimir la cadena "¿Es un palíndromo?" seguida del resultado devuelto por la función palindromo al pasarle la cadena "hola" como parámetro. El resultado será False, ya que "hola" no es un palíndromo.
# # /*

# Dada una cadena de texto, comprobar si es polindromo o no.
# Se leen igual de dereacha a izquierda

# ejem:
# ana, bob, otto, allivessevilla

# No tener en cuenta espacios raros

# Como hacerlo:
# -Funcion con parametro "texto"
# -Separar-el-texto-en-un-array- de letras
# -Darle la vuelta
# -Unir el array de letras en un string y comparar con el parametro

# */ 

# function palindromo(texto){
#     let invertido = texto
#                     .split('')
#                     .reverse()
#                     .join('')//lo que pongo enmedio comillas me separa las letras
#                     ;
#     return (invertido === texto);// Es lo mismo que abajo pero mas corto
#     //console.log(invertido)
#     /*
#     if(invertido === texto ){
#         return true;
#     }else{
#         return false;
#     }*/

# }

# console.log("Es un palindormo? " + palindromo("hola"));

