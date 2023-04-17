import random

def aleatorio(minimo, maximo):
    return random.randint(minimo, maximo)

print(aleatorio(1, 5))

# En este ejemplo, se importa el módulo random y se define una función llamada aleatorio que toma dos argumentos: el valor mínimo y máximo para el rango de números aleatorios. La función utiliza el método randint del módulo random para generar un número aleatorio entero dentro del rango especificado y lo devuelve como resultado.

# Luego, se llama a la función aleatorio con los valores 1 y 5 como argumentos y se imprime el resultado con la función print.

# //sacar numero aleatorios entre los dos numeros le digamos

# function aleatorio(minimo, maximo){
#     return Math.round(Math.random() * (maximo - minimo + minimo));
# }

# console.log(aleatorio(1, 5));