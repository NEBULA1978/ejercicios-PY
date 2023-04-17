print("Bienvenido al juego de preguntas de Python 3. ¡Buena suerte!")
print("")

preguntas = [
    {
        "pregunta": "¿Cuál es el operador de comparación que se utiliza para verificar si dos valores son iguales en Python?",
        "respuestas": [
            {"texto": "==", "correcta": True},
            {"texto": "=", "correcta": False},
            {"texto": "!=", "correcta": False},
            {"texto": "<>", "correcta": False}
        ]
    },
    {
        "pregunta": "¿Cuál es el método que se utiliza para leer la entrada del usuario en Python?",
        "respuestas": [
            {"texto": "read()", "correcta": False},
            {"texto": "input()", "correcta": True},
            {"texto": "get_input()", "correcta": False},
            {"texto": "get_user_input()", "correcta": False}
        ]
    },
    {
        "pregunta": "¿Cuál es la función que se utiliza para imprimir en la consola en Python?",
        "respuestas": [
            {"texto": "print()", "correcta": True},
            {"texto": "log()", "correcta": False},
            {"texto": "echo()", "correcta": False},
            {"texto": "display()", "correcta": False}
        ]
    },
    {
        "pregunta": "¿Qué tipo de estructura de datos se utiliza para almacenar una colección ordenada y mutable de elementos en Python?",
        "respuestas": [
            {"texto": "Tupla", "correcta": False},
            {"texto": "Lista", "correcta": True},
            {"texto": "Conjunto", "correcta": False},
            {"texto": "Diccionario", "correcta": False}
        ]
    },
    {
        "pregunta": "¿Cuál es la palabra clave que se utiliza para definir una función en Python?",
        "respuestas": [
            {"texto": "def", "correcta": True},
            {"texto": "function", "correcta": False},
            {"texto": "define", "correcta": False},
            {"texto": "func", "correcta": False}
        ]
    }
]

puntuacion = 0

for i, pregunta in enumerate(preguntas):
    print("Pregunta {}:".format(i+1))
    print(pregunta["pregunta"])
    print("")
    
    for j, respuesta in enumerate(pregunta["respuestas"]):
        print("{}. {}".format(j+1, respuesta["texto"]))
    
    respuesta_usuario = input("Ingrese el número de su respuesta: ")
    print("")
    
    try:
        respuesta_usuario = int(respuesta_usuario)
        if respuesta_usuario > 0 and respuesta_usuario <= len(pregunta["respuestas"]):
            respuesta_correcta = pregunta["respuestas"][respuesta_usuario-1]["correcta"]
            if respuesta_correcta:
                print("¡Respuesta correcta!")
                puntuacion += 1
            else:
                print("Respuesta incorrecta.")
        else:
            print("Respuesta inválida.")
    except ValueError:
        print("Respuesta inválida.")
    
    print("")

print("¡Juego terminado!")

# Este es un juego de preguntas de Python 3 en el que el usuario debe responder una serie de preguntas relacionadas con la programación en Python. Cada pregunta tiene cuatro posibles respuestas, y el usuario debe seleccionar la respuesta correcta ingresando el número correspondiente. Al final del juego, se mostrará la puntuación del usuario basada en el número de respuestas correctas.

# El juego comienza con un saludo y una introducción. Luego, se define una lista de preguntas, cada una de las cuales es un diccionario que contiene la pregunta y las respuestas posibles. Cada respuesta posible también es un diccionario que contiene el texto de la respuesta y un indicador booleano que indica si la respuesta es correcta o no.

# Luego, se recorre la lista de preguntas con un bucle for. Para cada pregunta, se muestra la pregunta y las respuestas posibles en la consola. Se solicita al usuario que ingrese el número correspondiente a su respuesta elegida. Si el usuario ingresa una respuesta inválida, se le informa de que la respuesta es inválida y se le solicita que vuelva a intentarlo. Si el usuario ingresa una respuesta válida, se verifica si la respuesta es correcta o no. Si la respuesta es correcta, se le informa al usuario que ha respondido correctamente y se incrementa su puntuación en 1. Si la respuesta es incorrecta, se le informa al usuario que ha respondido incorrectamente.

# Al final del juego, se muestra la puntuación final del usuario en la consola.