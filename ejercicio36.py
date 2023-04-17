def cuenta_letras(texto):
    consonantes = 0
    vocales = 0
    texto_limpio = ""

    # Limpiamos el texto de caracteres no deseados
    for letra in texto:
        if letra.isalpha() or letra in "áéíóúÁÉÍÓÚ":
            texto_limpio += letra

    # Contamos las vocales y consonantes en el texto limpio
    for letra in texto_limpio:
        if letra in "aeiouAEIOU":
            vocales += 1
        else:
            consonantes += 1

    return (consonantes, vocales)

letras = cuenta_letras("victorroblesweb.es")
print("Consonantes:", letras[0])
print("Vocales:", letras[1])
# //dado un texto ,devolever cuantas consonantes y cuantas vocales tiene


# function cuentaLetras(texto){
#     let consonantes = 0, vocales = 0, texto_limpio = "";

#     texto_limpio = texto.split("")
#                         .filter(letra => /[áéíóú\w]/gi.test(letra) && isNaN(letra))
#                         .join("");

#     //console.log(texto_limpio);
#     //comprobamos si es una vocal o consoonate y sumamos a contador
#     for(let letra of texto_limpio){
#         if(/[áéíóúaeiou]/gi.test(letra)){
#             vocales++;
#         }else{
#             consonantes++;
#         }

#     }
#     return[consonantes, vocales];
# }

# let letras = cuentaLetras("victorroblesweb.es");

# console.log("Consonantes:", letras[0]);
# console.log("Vocales:", letras[1]);