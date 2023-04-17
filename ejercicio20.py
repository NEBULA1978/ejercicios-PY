def limpiar_texto(texto):
    return ''.join(filter(str.isalpha, texto)).lower()

def anagramas(texto1, texto2):
    return limpiar_texto(texto1) == limpiar_texto(texto2)

print(anagramas('Riesgo', 'Sergio'))  # Devuelve: True
print(anagramas('Victor', 'Robles'))  # Devuelve: False


# /*

# Dadas dos cadenas de taxto,crear un algoritmo que compruebe
# si son anagramas entre si.

# Una cadena es un anagrama de otra si usa los mismos caracteres
# en la misma cantidad.

# No tener en cuenta espacios, simboles raros,puntos,etc.

# Ejemplos:
# anagramas('Riesgo', 'Sergio')  // Devuelve: true
# anagramas('Victor', 'Robles')  // Devuelve: false


# Como hacerlo:
# -Crear una funcion para limpiar los textos
# -Quitar todo lo que no sea texto
# -Poner en minusculas
# -Crear array de letras
# -Ordenarlo
# -Unirlo
# -Funcion para comparar las dos palabras

# */


# function limpiarTexto(texto){
#     return texto
#         .replace(/[^\w]/gi, '')//elimina todo lo que no sean letras
#         .toLowerCase()
#         .split('')//separar todas las letras en un array de caracteres
#         .sort()//ordena
#         .join('')//une
#     ;
# }

# function anagramas(texto1, texto2){
#     return limpiarTexto(texto1) === limpiarTexto(texto2);
# }

# //console.log(limpiarTexto("Hola. soy - Ramon¡¡"))
# console.log(anagramas("Sergio ¡¡ -., ", "serGIO!!!,,, ''"));