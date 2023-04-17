def lado(numero):
    lado = ""

    for i in range(numero):
        lado += "*"
    return lado


def cuadrado(numero):
    
    # Lado arriba
    dibujo = lado(numero) + "\n"

    # Contenido del cuadrado
    contenido = ""

    # Filas
    for i in range(numero-2):
        contenido = "*"
        
        # Contenido nuevo
        for x in range(numero-2):
            contenido += " "

        contenido += "*"
        
        # Añadir fila al dibujo
        dibujo += contenido + "\n"

    # Lado abajo
    dibujo += lado(numero)

    return dibujo

print(cuadrado(10))


# /*

# Dibujar un cuadrado hueco con asteriscos

# ejemplo:

# cuadrado(4)

# Devuelve: 4por arriba 4por abajo y 4 por los lados

# ****
# *  *
# *  *
# ****


# COMO HACERLO

# -Funcion para crear el lado de arriba y abajo del cuadrado
# -Funcion que haga los lados y el hueco del cuadrado
# -Bucle de 0 al tamaño del lado de menos 2 para equilibrar
# con el asterisco de izq a der.
# -Ir concadenado en una variable cada linea de cuadrado.
# -Mostrar el cuadrado

# por minuto 5.30 vid26 ejercicio 6 por la mitad
# */

# function lado(numero){
#     let lado = "";

#     for(let i = 0; i < numero; i++ ){
#         lado += "*";
#     }
#     return lado;
# }


# function cuadrado(numero){
    
#     //Lado arriba
#     let dibujo = lado(numero) + "\n";

#     let contenido = "";

#     //Filas
#     for(let i=0; i < (numero-2); i++){
#         contenido = "*";
        
#         //Contenido Nuevo
#         for(let x=0; x<(numero-2); x++){
#             contenido += " ";

#         }
#         contenido += "*";
        
#         //añadir fila al dibujo
#         dibujo += contenido + "\n";
#     }
#     //Lado abajo
#     dibujo += lado(numero);
    
#     return dibujo;
    
# }

# console.log(cuadrado(10));