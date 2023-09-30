def escalera(numero):
    escalera_completa = ""

    for nivel in range(1, numero+1):
        escalones = ""

        for escalon in range(1, nivel+1):
            escalones += "[-]"

        escalera_completa += escalones + '\n'

    return escalera_completa

print(escalera(7))


# /* 

# Enunciado:
# Dado un numero, mostrar una escalera con escalones de "[-]"
# usando el numero para los niveles de la escalera:

# Ejemplo:
# escalera(4)  //Devuelve:

# [-]
# [-][-]
# [-][-][-]
# [-][-][-][-]

# Como hacerlo
# -Funcion que reciba un numero
# -Recorrer el numero de niveles de la escalera
# -En cada iteracion pintar las escalones de ese nivel
# -Haciendo un bucle desde 1 hasta el nivel en el que estamos
# */

# function escalera(numero){
#     let escalera_completa = "";

#     for(let nivel = 1; nivel <= numero; nivel++){
#         //console.log("Nivel:", nivel);
#         let escalones = "";

#         for(let escalon = 1; escalon <= nivel; escalon++){
#             escalones += "[-]";
#         }
#         //console.log("Nivel",nivel, escalones);
#         escalera_completa += escalones + '\n';
#     }
#     return escalera_completa;
# }

# console.log(escalera(7))