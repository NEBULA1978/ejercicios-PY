import re

def coincidencias(frase, busqueda):
    # Limpiar frase de puntuaciones y convertir a minúsculas
    text_limpio = re.sub(r'[!¿?.,=]', '', frase.lower())
    
    resultado = 0
    
    if busqueda in text_limpio:
        # Dividir la frase en palabras
        palabras = text_limpio.split()
        mapa = {}
        
        # Contar la cantidad de veces que aparece cada palabra
        for palabra in palabras:
            if palabra in mapa:
                mapa[palabra] += 1
            else:
                mapa[palabra] = 1
        
        resultado = mapa.get(busqueda, 0)
    
    return resultado

print(
    "Numero de coincidencias en la frase:",
    coincidencias("Hola, que tal, soy RAMON pascual. ramon ramon", "que"),
    coincidencias("Esta es mi frase", "paco")
)


# /*
# Dada una palabra buscarla en una frase y devolver cuantas veces aparece en ella.

# La frase y la palabra deben ser parametro de una funcion.

# ejemplo:
# coincidencias("soy la frase", "victor") // Devuelve: 0

# COMO HACERLO:

# -Funcion con dos parametros "frase" y "busqueda"
# -Poner string en minusculas y limpiarlo(eliminar puntos comas guiones ,etc)
# -Comporbar si la busqueda esta inckluida en la frase
# -Mapear esas palabras y hace un contador de cada una(dentro de objeto JSON)
# -Devolver el contador de la busqueda

# */

# //limpiar frase de puntos y comas ,etc:

# function coincidencas(frase,busqueda){
#     let text_limpio = frase.toLowerCase().replace(/[!¿?.,=]/gi, '')//si quiero añada algo entre palabras entre comillas despues gi
#     // para decirle elimine let text_limpio = frase.toLowerCase().replace(/[!¿?.,=]/gi, '')
#     let resultado = 0;
#     //console.log(text_limpio);
#     if(text_limpio.includes(busqueda)){

#         let palabras = text_limpio.split(" ");
#         let mapa = {};
        
#         //recorrer cada palabra que se encuenrtra en array de palabras con for
#         //co of( conseguir el valor da cada elemento que hay dentro de una array) seria como un foreach 
#         for(let palabra of palabras){
#             if(mapa[palabra]){
#                 mapa[palabra]++;
#             }else{
#                 mapa[palabra] = 1;
#             }
#         }

#         resultado = mapa[busqueda]

#         //console.log(palabras);
#         //console.log(mapa);

#     }else{
#         resultado = 0;
#     }
#     return resultado;

# }

# console.log(
#     "Numero de coincidencias en la frase: ",
#     coincidencas("Hola, que tal, soy RAMON pascual. ramon ramon","que"),
#     coincidencas("Esta es mi frase","paco")
#     );

