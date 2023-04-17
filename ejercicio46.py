def todosSubStrings(palabra):
substrings = []
for letra in range(len(palabra)):
comienzo = letra
for i in range(len(palabra) - comienzo):
final = i + comienzo + 1
substrings.append(palabra[comienzo:final])
return list(filter(lambda x: len(x) >= 1, substrings))

print(todosSubStrings("ramonpascualweb"))

# // Dado un string,devolver todos los posibles substrings
# function todosSubStrings(palabra){

#     let substrings = [];

#     for(letra in palabra){

#         let comienzo = parseInt(letra);

#         for(let i = 0; i <= palabra.length - comienzo; i++){
#             let final = parseInt(i) + parseInt(comienzo);

#             substrings.push(palabra.substring(comienzo, final))
#             //console.push(palabra.substring(comienzo, final));
#         }
#     }
#     return substrings.filter(elemento => elemento.length >= 1);
# }



# console.log(todosSubStrings("ramonpascualweb"));