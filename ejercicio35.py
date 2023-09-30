def primero_y_ultimo(elementos):
    nuevos_elementos = [elementos[0], elementos[-1]]
    return nuevos_elementos

print(primero_y_ultimo([100, 200, 300, 780]))

# The function primero_y_ultimo takes an array elementos as its argument. It creates a new array nuevos_elementos and adds the first and last elements of elementos to it. Finally, it returns nuevos_elementos.

# When the function is called with the argument [100, 200, 300, 780] and the result is printed using the print() function, the output will be [100, 780]. This is because the function takes the first element (100) and the last element (780) of the input array and returns a new array containing only those two elements. en casrtellano

# La función primero_y_ultimo toma como argumento un arreglo llamado elementos. Luego, crea un nuevo arreglo llamado nuevos_elementos y agrega el primer y último elemento del arreglo elementos a él. Finalmente, devuelve el arreglo nuevos_elementos.

# Cuando se llama a la función con el argumento [100, 200, 300, 780] y se imprime el resultado usando la función print(), la salida será [100, 780]. Esto se debe a que la función toma el primer elemento (100) y el último elemento (780) del arreglo de entrada y devuelve un nuevo arreglo que contiene solo esos dos elementos.


# function primeroYultimo(elementos){

#     let nuevos_elementos = [];
#     nuevos_elementos.push(elementos[0], elementos[elementos.length -1]);

#     return nuevos_elementos;
# }

# console.log(primeroYultimo([100, 200, 300, 780]));