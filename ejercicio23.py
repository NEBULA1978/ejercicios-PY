def en_mayuscula(texto):
    palabras = []
    for palabra in texto.split(" "):
        palabras.append(palabra[0].upper() + palabra[1:])
    return " ".join(palabras)

print(en_mayuscula("hola soy victor"))  # devuelve: 'Hola Soy Victor'

# In Python, the naming convention for functions and variables is to use underscores instead of camelCase. The split() method is used to split the input string into a list of words, which are then processed individually in a loop using the upper() method to capitalize the first letter of each word, and the join() method is used to combine the modified words into a single string.
# En Python, se sigue la convención de nombrar funciones y variables utilizando guiones bajos en lugar de camelCase. El método split() se utiliza para dividir la cadena de entrada en una lista de palabras, las cuales se procesan individualmente en un bucle utilizando el método upper() para capitalizar la primera letra de cada palabra, y el método join() se utiliza para combinar las palabras modificadas en una única cadena.
# /*

# Enunciado:
# Dada una cadena de texto ,poner en mayusculas la primera letra
# de cada palabra en la cadena y luego devolver la cadena.

# Ejemplos:
# enMayuscula('hola soy victor)  // devuelve: 'Hola Soy Victor'

# Como hacerlo:
# -Crear una funcion con parametro de texto
# -Poner la primera letra del string en mayisculas
# -Recorrer el string completo
# -Devolverelresultado
# -Si el caracter anterior a la letra actual es un espacio
# -Ponerlo en mayusculas
# -Si el caracter no es un espacio añadirlo al resultado

# */


# function enMayusculaOriginal(texto){
#     let resultado =  ""; //texto[0].toUpperCase();

#     for(letra in texto){//con for in necesito tener el indice
#         //console.log(letra);
#         if(texto[letra - 1] === " " || parseInt(letra) === 0){
#             resultado += texto[letra].toUpperCase();
#         }else{
#             resultado += texto[letra];
#         }
#     }

#     return resultado;
# }
# function enMayuscula(texto){
#     let palabras = [];//array vacio

#     for(let palabra of texto.split(" ")){

#         palabras.push(palabra[0].toUpperCase() + palabra.substring(1))
#     }

#     return palabras.join(' ');

# }

# console.log(enMayuscula("hola visita vitorrobles.es cincuenta palabras"));