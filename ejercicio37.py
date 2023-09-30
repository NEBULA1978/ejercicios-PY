def el_que_mas_aparece(datos):
    mapeo = {}
    mas_frecuente = ""
    mayor_valor = 0

    if isinstance(datos, str):
        datos = datos.split()

    for elemento in datos:
        if elemento in mapeo:
            mapeo[elemento] += 1
        else:
            mapeo[elemento] = 1

    for elemento, valor in mapeo.items():
        if valor > mayor_valor:
            mayor_valor = valor
            mas_frecuente = elemento

    return {
        "mas_frecuente": mas_frecuente,
        "mayor_valor": mayor_valor
    }

print(el_que_mas_aparece("victor robles hola victor"))
print(el_que_mas_aparece([1,2,3,4,4,4]))



# function elQueMasAparece(datos){

#     let mapeo = {}, mas_frecuente = "", mayor_valor = 0;

#     if(typeof datos === "string"){
#         datos = datos.split(" ");
#     }

#     for(let elemento of datos){

#         if(mapeo[elemento]){
#             mapeo[elemento]++;

#         }else{
#             mapeo[elemento] = 1;
#         }
        
#     }

#     for(let elemento in mapeo){
#         if(mapeo[elemento] > mayor_valor){
            
#             mayor_valor = mapeo[elemento];
#             mas_frecuente = elemento;

#         }
#     }

#     //console.log(mayor_valor, mas_frecuente);
#     //hago JSON abajo
#     return {
#         "mas_frecuente": mas_frecuente,
#         "mayor_valor": mayor_valor
#     };
# }

# console.log(elQueMasAparece("victor robles hola victor"))
# console.log(elQueMasAparece([1,2,3,4,4,4]))