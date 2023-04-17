def factorial(numero):
    resultado = 1
    
    for i in range(1, numero + 1):
        resultado *= i
        
    return resultado

print("El factorial de 5 es:", factorial(5))

# The range function is used in Python to generate a sequence of numbers. In this case, we use range(1, numero + 1) to generate a sequence of numbers from 1 to numero, inclusive.

# Note that Python uses colons to indicate the start of a code block and indentation to indicate which statements are part of that block, whereas JavaScript uses curly braces. en castellano

# La función range se utiliza en Python para generar una secuencia de números. En este caso, usamos range(1, numero + 1) para generar una secuencia de números desde 1 hasta numero, inclusivo.

# Es importante destacar que en Python se utilizan dos puntos (:) para indicar el inicio de un bloque de código y la indentación para indicar qué declaraciones forman parte de ese bloque, mientras que en JavaScript se usan llaves ({}) para ello.

# function factorial(numero){
#     let resultado = 1;

#     for(let i = 1; i <= numero; i++){
#         resultado *= i;
#     }

#     return resultado;
# }

# console.log("El factorial de 5 es:", factorial(5));