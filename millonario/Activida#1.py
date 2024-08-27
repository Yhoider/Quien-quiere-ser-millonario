import random as rd 

def numero_de_jugadores ():
    numero = int(input("Ingresa el numero de personas que van a jugar:")) + 1
    name = []
    for i in range (1, numero):
        n = (input(f"Ingresa el nombre del jugador {i}:"))
        name.append(n)
    return name

def elegir_jugador(name):
    print("Elige un jugador:")
    lenght = len(name)
    for i in range (lenght):
        print (i, name[i])
    elegir = int(input("Elige el numero del presonaje que quieres escoger:" ))
    player = name[elegir]
    return player

def Bienvenida (player):
    print(f"¡Bienvenido a {player} ¿Quién quiere ser millonario?!")
    print("Las reglas son las siguientes:")
    print("1) Se te hara una pregunta en cada ronda, si respondes bien pasas a la siguiente,")
    print("   si tu respondes mal pierdes y se termina el juego.")
    print("2) En el transcurso del tendras disponible 1 comodines disponibles: cambiar pregunta")
    print("   Para usar los comodines escribe la palabra comodin en la casilla de respuesta.")
    print("Buena suerte")

# preguntas
preguntas = [
    {"pregunta": "¿Cuál es la capital de Francia?", "respuestas": ["A) París", "B) Londres", "C) Berlín", "D) Roma"], "correcta": "A) París"},
    {"pregunta": "¿Cuál es el planeta más grande de nuestro sistema solar?", "respuestas": ["A) Tierra", "B) Saturno", "C) Júpiter", "D) Urano"], "correcta": "C) Júpiter"},
    {"pregunta": "¿Cuál es la capital de Francia?", "respuestas": ["A) París", "B) Londres", "C) Berlín", "D) Roma"], "correcta": "A) París"},
    {"pregunta": "¿Cuál es el río más largo del mundo?", "respuestas": ["A) Amazonas", "B) Nilo", "C) Yangtsé", "D) Mississippi"], "correcta": "B) Nilo"},
    {"pregunta": "¿Cuál es la montaña más alta del mundo?", "respuestas": ["A) Elbrus", "B) K2", "C) Kilimanjaro", "D) Everest"], "correcta": "D) Everest"},
    {"pregunta": "¿Cuál es el país más poblado del mundo?", "respuestas": ["A) Estados Unidos", "B) India", "C) China", "D) Brasil"], "correcta": "B) India"},
    {"pregunta": "¿Cuál es la ciudad más poblada del mundo?", "respuestas": ["A) Londres", "B) Nueva York", "C) Tokio", "D) París"], "correcta": "C) Tokio"},
    {"pregunta": "¿Cuál es el idioma más hablado del mundo?", "respuestas": ["A) Chino", "B) Español", "C) Inglés", "D) Árabe"], "correcta": "C) Inglés"},
    {"pregunta": "¿Cuál es el deporte más popular del mundo?", "respuestas": ["A) Baloncesto", "B) Fútbol ", "C) Tenis", "D) Golf"], "correcta": "B) Fútbol"},
    {"pregunta": "¿Cuál es la empresa más grande del mundo?", "respuestas": ["A) Apple", "B) Google", "C) Amazon", "D) Microsoft"], "correcta": "A) Apple"},
    {"pregunta": "¿Cuál es el país con la mayor economía del mundo?", "respuestas": ["A) Estados Unidos", "B) China", "C) Japón", "D) Alemania"], "correcta": "A) Estados Unidos"},
    {"pregunta": "¿En que año inicio la segunda guerra mundal?", "respuestas": ["A) 1945", "B) 1914", "C) 1948", "D) 1939"], "correcta": "D) 1939"},
    {"pregunta": "¿Cuánto vale el número pi?", "respuestas": ["A) 3.14", "B) 2.71", "C) 1.61", "D) 4.21"], "correcta": "A) 3.14"},
    {"pregunta": "¿Cuál es la fórmula de la velocidad de la luz?", "respuestas": ["A) c = λν", "B) c = 2πr", "C) c = F/m", "D) c = E/m"], "correcta": "A) c = λν"},
    {"pregunta": "¿Quién es el autor de la teoría de la evolución?", "respuestas": ["A) Charles Darwin", "B) Gregor Mendel", "C) Albert Einstein", "D) Isaac Newton"], "correcta": "A) Charles Darwin"},
    {"pregunta": "¿Cuál es el nombre del proceso por el cual el agua se convierte en vapor?", "respuestas": ["A) Evaporación", "B) Condensación", "C) Fusión", "D) Solidificación"], "correcta": "A) Evaporación"},
    {"pregunta": "¿Quién es el inventor de la máquina de vapor?", "respuestas": ["A) Guglielmo Marconi", "B) Thomas Edison", "C) Nikola Tesla", "D) James Watt"], "correcta": "D) James Watt"},
    {"pregunta": "¿Cuál es el nombre del planeta más cercano al Sol?", "respuestas": ["A) Mercurio", "B) Venus", "C) Tierra", "D) Marte"], "correcta": "A) Mercurio"},
    {"pregunta": "¿Quién es el autor de la teoría de la relatividad?", "respuestas": ["A) Albert Einstein", "B) Isaac Newton", "C) Galileo Galilei", "D) Marie Curie"], "correcta": "A) Albert Einstein"},
    {"pregunta": "¿Cuál es el nombre del proceso por el cual los organismos se adaptan a su entorno?", "respuestas": ["A) Evolución", "B) Selección natural", "C) Mutación", "D) Genética"], "correcta": "B) Selección natural"},
    {"pregunta": "¿Quién es el inventor del teléfono?", "respuestas": ["A) Nikola Tesla", "B) Thomas Edison", "C) Alexander Graham Bell", "D) Guglielmo Marconi"], "correcta": "C) Alexander Graham Bell"},
]



# pregunta aleatoria
def obtener_pregunta_aleatoria(preguntas_hechas):
    pregunta = rd.choice(preguntas)
    while pregunta in preguntas_hechas:
        pregunta = rd.choice(preguntas)
    return pregunta

# Mostrar la pregunta y obtener la respuesta del usuario
def hacer_pregunta(pregunta):
    print(pregunta["pregunta"])
    for i, respuesta in enumerate(pregunta["respuestas"]):
        print(f"{i+1}) {respuesta}")
    respuesta_usuario = input("Ingrese su respuesta (A, B, C o D): ")
    return respuesta_usuario

# Función para verificar si la respuesta es correcta
def verificar_respuesta(pregunta, respuesta_usuario):
    respuesta_correcta = pregunta["correcta"]
    if respuesta_usuario.upper() == respuesta_correcta[0]:
        return True
    else:
        return False

# Función para mostrar el puntaje actualizado
def actualizar_puntaje(puntaje):
    print(f"Su puntaje actual es: {puntaje}")

# Función para jugar el juego
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Función para jugar el juego
def jugar_juego():
    puntaje = 1
    preguntas_hechas = []
    comodines = 0
    number_player = numero_de_jugadores()
    player = elegir_jugador(number_player)
    reglas = Bienvenida(player)
    for i in range(1, 16):  
        pregunta = obtener_pregunta_aleatoria(preguntas_hechas)
        preguntas_hechas.append(pregunta)
        respuesta_usuario = hacer_pregunta(pregunta)
        # Verifica si el jugador quiere usar un comodín
        if respuesta_usuario.lower() == "comodin":
            
            if comodines < 2:
                print("¿Qué comodín deseas usar?")
                print("1. Cambiar pregunta")
                print("2. Eliminar 2 opciones")
                comodin = input("Ingrese el número del comodín: ")

                if comodin == "1":
                    # Cambia la pregunta
                    pregunta = obtener_pregunta_aleatoria(preguntas_hechas)
                    comodines += 1
                    continue
            else:
                print ("Ohh lo siento ya no la puedes usar ")
                continue       
                    
        if verificar_respuesta(pregunta, respuesta_usuario):
            puntaje += fibonacci(i-1)
            print(f"Correcto! Su puntaje es: {puntaje}")
        else:
            print("Incorrecto. Juego terminado.")
            new_gamen = input("Deseas jugar de nuevo?")
            if new_gamen.lower() in ["si", "sí"]:
                jugar_juego ()
            else:
                break
        if i == 5 or i == 7:
            print("¿Desea retirarse del juego?")
            eleccion_usuario = input("Ingrese sí o no: ")
            if eleccion_usuario.lower() in ["si", "sí"]:
                print(f"Su puntaje final es: {puntaje}")
                break
    if i == 15:
        print("¡Felicidades! Ha completado el juego. Su puntaje final es:", puntaje)

# Iniciar el juego
jugar_juego()

