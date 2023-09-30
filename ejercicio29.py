def capi(numero):
    procesado = int(str(numero)[::-1])
    return numero == procesado

print(capi(2002))


# function capi(numero){
#     let procesado = parseInt(numero
#                     .toString()
#                     .split('')
#                     .reverse()
#                     .join('')
        
#         );

#         return numero === procesado;
# }

# console.log(capi(2002));