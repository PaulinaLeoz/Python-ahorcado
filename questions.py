import random
words = {"programación": [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista"],
"colores": [
    "azul", 
    "blanco", 
    "amarillo", 
    "violeta"],
"comidas": [
    "milanesa", 
    "hamburguesa", 
    "ensalada", 
    "asado", 
    "tacos", 
    "fideos"]}
print("¡Bienvenido al Ahorcado!")
print()
print ("Categorías: ")
for categoria in words:
    print(categoria)
categoria = input("Elige una categoría: ")
if categoria not in words:
    print ("Categoría inválida.")
    exit()
word_random = random.sample(words[categoria],len(words[categoria]))
i = 0
while i < len(word_random):
    word = word_random[i]
    guessed = []
    attempts = 6
    score = 0
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            score += 6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida.")
            continue
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        score = 0
    print(f"Puntaje final: {score}")
    seguir = input("Querés seguir jugando? (s/n): ")
    if seguir.lower() != "s":
        break
    i += 1