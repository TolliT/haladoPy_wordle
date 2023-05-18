import nltk
import random
from tkinter import *
from tkinter import messagebox

# CONSTANTS #
NUM_GUESSES = 5

# WORD GENERATION #
nltk.download('words')

word_list = nltk.corpus.words.words()
five_char_words = [word for word in word_list if len(word) == 5]

words = random.sample(five_char_words, 5)
words = [word.lower() for word in words]

target_word = random.choice(words)
WORD_LENGTH = len(target_word)
guessed_word = ['_'] * WORD_LENGTH

# Debug
print(target_word)

# TK INIT #
window = Tk()
window.title("HaladoPY")
window.geometry("250x150")

word_label = Label(window, text=' '.join(guessed_word), font=("Arial", 16), pady=5)
word_label.pack()

entry = Entry(window)
entry.pack()
entry.focus_set()

guess_label = Label(window, text=f"Guesses Remaining: {NUM_GUESSES}", font=("Arial", 12), pady=5)
guess_label.pack()


# CHECK CURRENT GUESS #
def check_guess():
    global NUM_GUESSES
    guess = entry.get().lower()
    entry.delete(0, END)

    if len(guess) != WORD_LENGTH:
        messagebox.showinfo("Invalid Guess", f"Please enter a {WORD_LENGTH}-letter word.")
        return

    if guess == target_word:
        messagebox.showinfo("Congratulations", "You guessed the word correctly!")
        window.quit()
        return

    for i in range(WORD_LENGTH):
        if guess[i] == target_word[i]:
            guessed_word[i] = guess[i]

    word_label.config(text=' '.join(guessed_word))

    NUM_GUESSES -= 1
    guess_label.config(text=f"Guesses Remaining: {NUM_GUESSES}")

    if NUM_GUESSES == 0:
        messagebox.showinfo("Game Over", f"You ran out of guesses. The word was {target_word}.")
        window.quit()


submit_button = Button(window, text="Submit", command=check_guess, font=("Arial", 12), pady=5)
submit_button.pack()

window.mainloop()