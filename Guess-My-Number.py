# Calvin Comstock-Fisher and Natalie Scholz
# 10/22/20
# Guess My Number

#Step 1. Import Tkinter
import tkinter as tk
import random
import sys

#Step 2. Create the window and Title
window = tk.Tk()
window.title("Guess My Number")

#textBox = tk.Text(window, height=1, width=10)
#textBox.pack()

entry = tk.Entry(window)
entry.pack()
entry.insert(0, "0")

count = 0
number = random.randint(0, 101)
exitButton = tk.Button(window, text="Press this to exit!", command=quit)

def quit():
  sys.exit()

def cool():
  startButtonDef(count)

def startButtonDef(round):
  # Create while loop that accounts for running down guesses and guessing the correct number. 
  if round <= 10:
    guessesLeft = 10 - round
    questionText = tk.Label(window, text = "What number am I thinking of between 1 and 100? You have " + str(guessesLeft) + " guess(es) left. ").pack()
    if number == int(entry.get()):
      congrats = tk.Label(window, text= "Congrats you win!!!").pack()
      exitButton.pack()
    elif number != int(entry.get()):
      round += 1
      tryAgain = tk.Label(window, text = "Try Again!").pack()
    elif round > 10:
      ranOut = tk.Label(window, text = "You ran out of guesses :( better luck next time!").pack()
      exitButton.pack()


#Step 3. Create the start Button
startButton = tk.Button(window, text="Press this to start the game!", command=cool)
startButton.pack()

window.mainloop()