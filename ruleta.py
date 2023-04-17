import random

def jugar_ruleta(dinero, apuesta):
    while dinero >= apuesta:
        numero_elegido = random.randint(0, 36)
        if (numero_elegido % 2 == 0 and apuesta % 2 == 0) or (numero_elegido % 2 != 0 and apuesta % 2 != 0):
            dinero += apuesta
            print("¡Ganaste {}! Tu saldo es ahora de {}".format(apuesta, dinero))
            apuesta = 10  # Apuesta inicial
        else:
            dinero -= apuesta
            print("Perdiste. Tu saldo es ahora de {}".format(dinero))
            apuesta *= 2  # Duplicar la apuesta para la siguiente ronda
        
        if dinero <= 0:
            print("Te quedaste sin dinero. ¡Fin del juego!")
            break
        elif apuesta > 640:
            print("Alcanzaste el límite de apuesta. ¡Fin del juego!")
            break

dinero = int(input("¿Cuánto dinero tienes para apostar? "))
apuesta = 10  # Apuesta inicial
jugar_ruleta(dinero, apuesta)

# Este código utiliza la biblioteca random para elegir un número aleatorio entre 0 y 36 en cada ronda. La función jugar_ruleta() implementa la estrategia Martingala: si el jugador pierde una ronda, duplica su apuesta para la siguiente ronda. Si gana una ronda, su apuesta vuelve a ser la apuesta inicial. El juego continúa hasta que el jugador se quede sin dinero o alcance un límite de apuesta predefinido (en este caso, 640).
