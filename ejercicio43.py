def la_media(numeros):
    suma = sum(numeros)
    media = suma / len(numeros)
    return media

print(la_media([1,2,3,4,5,6, 20, 50]))

# Note that in Python, the convention is to use underscores to separate words in function names (i.e., la_media instead of laMedia). The rest of the code is straightforward and should work as expected.

# //dado un array de numero,sacar la media de todos ellos
# //Ejemplo laMedia([1,2,3]);
# //devuelve: 3

# function laMedia(numeros){
#     let suma = numeros.reduce((valorAcumulado, numeroActual) =>{

#         return valorAcumulado + numeroActual;
#     });

#     let media = suma / numeros.length;

#     return media;
# }

# console.log(laMedia([1,2,3,4,5,6, 20, 50]));