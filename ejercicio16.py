def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count

print("Número de vocales:", count_vowels("victorrovlesweb.es"))


# /*

# Dada una cadena de texto, devolver cuantas vocales
# (a,e,i,o,u) tiene.

# Ejemplos:
# vocales("victorrovlesweb.es") // devuelve: 6

# Como hacerlo:

# -Crear una funcion que reciba texto
# -Metodo match.js con expresion regular
# -Devolver resultado


# */

# function vocales(texto){
#     let coincidencias = texto.match(/[aeiou]/gi);

#     //console.log(coincidencias);
#     return coincidencias ? coincidencias.length : 0;
# }

# console.log("Numero de vocales:", vocales("victrrblswb.s"));