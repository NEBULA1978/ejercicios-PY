def existePropiedad(objeto, propiedad):
    if isinstance(objeto, dict) and isinstance(propiedad, str) and propiedad in objeto:
        return True
    return False

usuario = {
    "nombre": "victor",
    "apellido": "Robles"
}

print(existePropiedad(usuario, "nombre")) # Output: True

# Note that in Python, we use isinstance() to check if an object is of a certain type. Here, we check if objeto is a dictionary using isinstance(objeto, dict), and if propiedad is a string using isinstance(propiedad, str).

# To check if a dictionary has a certain key, we can simply use the in operator. So, we check if propiedad is in objeto using propiedad in objeto.

# Finally, we use print() to print the output of the function. En castellano:

# En Python, usamos isinstance() para verificar si un objeto es de un cierto tipo. Aquí, verificamos si objeto es un diccionario usando isinstance(objeto, dict), y si propiedad es una cadena usando isinstance(propiedad, str).

# Para verificar si un diccionario tiene una determinada clave, simplemente podemos usar el operador in. Así, verificamos si propiedad está en objeto usando propiedad in objeto.

# Finalmente, usamos print() para imprimir la salida de la función.


# /*

# Dado un objeto,comprobar si existe una propiedad en concreto.

# Ejemplos:
# existePropiedad(niObjeto, "nombre")  Devuelve: true

# */

# function existePropiedad(objeto, propiedad){
#     if(typeof objeto == 'object' && typeof propiedad === "string" &&
#     hasOwnProperty.call(objeto, propiedad)// es lo mismo de antes:  objeto.hasOwnProperty(propiedad)
#     ){
#      return true;
#     }
    
#     return false;

# }
# let usuario ={
#     nombre: "victor",
#     apellido:"Robles"
# }

# console.log(existePropiedad(usuario, "nombre"));