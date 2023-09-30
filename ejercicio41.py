import math

def triangulo(numero):
    mitad = math.floor(numero - 1)
    resultado = ""

    # bucle total filas
    for fila in range(numero):
        nivel = ""

        # bucle para pintar asteriscos y espacios
        for columna in range(2 * numero - 1):

            if mitad - fila <= columna and mitad + fila >= columna:
                nivel += "*"
            else:
                nivel += " "

        resultado += nivel + "\n"

    return resultado

print(triangulo(14))

# Note that in Python, you need to use the import statement to use the math library and access the floor function. Additionally, the range function is used to iterate over a range of values. The rest of the code is similar to the JavaScript version. En castellano:

# En Python, es necesario usar la instrucción import para importar la biblioteca math y acceder a la función floor. Además, en lugar de usar un bucle for con una condición de comparación como en JavaScript, en Python se utiliza la función range para iterar sobre un rango de valores. El resto del código es similar a la versión JavaScript.

# function triangulo(numero){
#     let mitad = Math.floor(numero - 1);
#     let resultado = "";
#     //console.log(mitad)
#     //bucle total filas
#     for(let fila = 0; fila < numero; fila++){
#         let nivel = "";
#         //bucle para pintar asteriscos y espacios
#         for(let columna = 0; columna < (2 * numero - 1); columna++){
            
#             //console.log(mitad - fila, mitad + fila)
#             if(mitad - fila <= columna && mitad + fila >= columna){
#                 nivel += "*";
#             }else{
#                 nivel += " ";
#             }
                
            
#         }
#         resultado += nivel + "\n";

#         //console.log(nivel)
#     }

#     return resultado;
# }

# console.log(triangulo(14));