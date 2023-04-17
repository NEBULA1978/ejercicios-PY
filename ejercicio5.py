def tantoPorCiento(porcentaje, numero):
    operacion = numero * (porcentaje/100)
    resultado = f"El {porcentaje}% de {numero} es {operacion}"
    return resultado

print(tantoPorCiento(20, 897))


# /*
# ENUNCIADO 
# ¿Cuanto es el x por ciento de x numero ?

# ejemplos:
#             //el 20% de 100 es 20
# tantoPorCiento(20,100)  // Devuelve: 20
# tantoPorCiento(43,897)  // Devuelve: 385.71

# COMO HACERLO

# -Funcion conparametros "porcentaje" y "numero"
# -Crear una variable para la operacion del porcentaje
# -Devolver string que responda a la pregunta delenunciado
# */

# function tantoPorCiento(porcentaje, numero){
#     let operacion = (numero * (porcentaje/100))
#     let resultado = `El ${porcentaje}% de ${numero} es ${operacion}`;

#     return resultado;
#     //console.log(operacion)
# }

# console.log(tantoPorCiento(20, 897))