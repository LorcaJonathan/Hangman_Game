import random

def choose_word():
    palabras = ["python", "programacion", "inteligencia", "datos", "aprendizaje", "computadora"]
    return random.choice(palabras)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    MAX_ATTEMPTS = 6
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 0

    print("Bienvenido al juego del ahorcado!")
    print("La palabra tiene", len(word_to_guess), "letras.")

    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Ingresa una letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Ingresa una sola letra válida.")
            continue

        if guess in guessed_letters:
            print("Ya has adivinado esa letra.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("¡Correcto!")
        else:
            attempts += 1
            print("Letra incorrecta.")
            print(f"Te quedan {MAX_ATTEMPTS - attempts} intentos.")

        if all(letter in guessed_letters for letter in word_to_guess):
            print("\n¡Felicidades! ¡Has adivinado la palabra correctamente!")
            break

        if attempts >= MAX_ATTEMPTS:
            print("\nLo siento, has agotado tus intentos.")
            print(f"La palabra era: {word_to_guess}")
            break

    play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if play_again == "s":
        hangman()
    else:
        print("¡Hasta luego!")

if __name__ == "__main__":
    try:
        hangman()
    except (KeyboardInterrupt, EOFError):
        print("\n¡Adiós!")
