def mas_usado(texto):
    mapeo_letras = {}
    maximo_repeticiones = 0
    letra_mas_repetida = ""

    for letra in texto:
        if letra not in mapeo_letras:
            mapeo_letras[letra] = 1
        else:
            mapeo_letras[letra] += 1

    for letra in mapeo_letras:
        if len(str(mapeo_letras[letra]).strip()) == 1 and mapeo_letras[letra] > maximo_repeticiones:
            maximo_repeticiones = mapeo_letras[letra]
            letra_mas_repetida = letra

    return letra_mas_repetida

print("La letra mas repetida es:", mas_usado("He subido un nuevo video a mi canal de you tube"))


# /*
# Dada una cadena de texto, devolver el caracter mas usado.

# Ejemplo:
# masUsado("Victorroblesweb.es")  // Devuelve Lo que mas se repite es: e

# Como hacerlo:
# -Crear una funcion que reciba el texto.
# -Maprear letras en un json
# -Recorreremos el mapeo
# -Hacemos condicion para ver que contador es mayor

# */

# function masUsado(texto){

#     let mapeo_letras = {};
#     let maximo_repeticiones = 0;// wardo cual es el valor en cada momento
#     let letra_mas_repetida = "";//cual es la letra mas repetida

#     for(let letra of texto){
#         //console.log(letra)
#         //añadir propiedad por cada una de estas letras al objeto  json
#         if(!mapeo_letras[letra]){
#             mapeo_letras[letra] = 1;
#         }else{//si si existe mapeo json letra
#             mapeo_letras[letra]++;
#         }
#     }// con in me saca el indice de las letras
#     for(let letra in mapeo_letras){
#         //console.log(letra);
#         // en cada iteracion comprobar: si la letra que se esta recorriento su valor numerico en base a las repeticiones del string es mayor al anterior que hay, entonces lo wardo dentro de maximo repeticiones y ademas dentro de letra repetida wardo la letra en el caso que se cumpla esta condicion
#         if(mapeo_letras[letra].toString().trim().length ===1 && mapeo_letras[letra] > maximo_repeticiones){// .trim() elimina espacios
#             maximo_repeticiones = mapeo_letras[letra];
#             letra_mas_repetida = letra;
#         }
#     }
#    // console.log(mapeo_letras); comprobar 
#     return letra_mas_repetida;
#     //console.log(maximo_repeticiones, letra_mas_repetida);comprobar es correcto
# }
# console.log("La letra mas repetida es;",masUsado("He subido un nuevo video a mi canal de you tube"));