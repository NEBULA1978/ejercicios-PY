def soloUnaVez(texto):
    contadores = {}
    resultado = []
    letras = [letra for letra in texto if letra.strip()]  # Se utiliza una comprensión de lista para eliminar los espacios en blanco con el método strip()

    for letra in letras:
        if letra not in contadores:  # Se utiliza el operador in para verificar si una clave está en el diccionario
            contadores[letra] = 1
        else:
            contadores[letra] += 1

    for letra in contadores:
        if contadores[letra] == 1:
            resultado.append(letra)  # Se utiliza el método append para agregar elementos a la lista

    return [resultado, resultado[0]]

print(soloUnaVez("frase frase HOY"))

# Ten en cuenta que la función filter() se reemplaza con una comprensión de lista que elimina los espacios en blanco utilizando el método strip(). Además, se utiliza el operador in para verificar si una clave está en el diccionario, y se utiliza el método append() para agregar elementos a la lista.

# def soloUnaVez(texto):
#     contadores = {}
#     resultado = []
#     letras = [letra for letra in texto if letra.strip()]
    
#     for letra in letras:
#         if letra not in contadores:
#             contadores[letra] = 1
#         else:
#             contadores[letra] += 1
            
#     for letra in contadores:
#         if contadores[letra] == 1:
#             resultado.append(letra)
    
#     return [resultado, resultado[0]]

# print(soloUnaVez("frase frase HOY"))


# # /*
# # Dado un string, devolver cuales son las letas que aparecen solo una vez y cual es la primera.


# # Ejemplo
# # soloUnaVez("frase frase HOY")

# # Devuelve: [["H", "O", "Y"], "H"]

# # */

# # function soloUnaVez(texto){
    
# #     //definir variables
# #     let contadores = {},
# #         resultado = []
# #         letras = texto.split('').filter(letra => letra.trim().length >=1)
# #         ;
# #         //generar contadores
# #         for(letra of letras){
# #             //console.log(letra)
# #             if(!contadores[letra]){
# #                 contadores[letra] = 1;
# #             }else{
# #                 contadores[letra]++;
# #             }
# #         }


# #         //eliminar la letras que se repitan
# #         for(letra in contadores){
# #             if(contadores[letra] === 1){
# #                 resultado.push(letra);
# #             }
                
# #         }           
# #      /*es lo mismo que arriba

# #        for(letra in contadores){
# #             if(contadores[letra] >= 2){
# #                 delete contadores[letra];
# #             }else{
# #                 resultado.push(letra);
# #             }
# #         }*/


# #         return [resultado, resultado[0]];
        
# # }

# # console.log(soloUnaVez("frase frase HOY"));