
import re

def comprobar_email(email):
    # Comprobacion email
    return re.match(r'^\w+@\w+\.\w+$', email) is not None

print(comprobar_email("victor@victorrrobles.com"))

# Note that the regular expression pattern is enclosed in quotes, and the re module is used to match the pattern against the email string. The is not None check is used to convert the re.match result into a boolean value. en castellano:
#  En este caso, la expresión regular se encuentra entre comillas y se utiliza el módulo re para buscar la coincidencia del patrón con la cadena de email. La verificación is not None se utiliza para convertir el resultado de re.match en un valor booleano.   

# ///////////////////////////
# ///////////////////////////

# //validacion email con expresion regular

# function comprobarEmail(email){

#     //comprobacion email
#     return /^\w+@\w+\.\w+$/gi.test(email);

# }

# console.log(comprobarEmail("victor@victorrrobles.com"));