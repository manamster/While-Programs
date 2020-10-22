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

def quit():
  sys.exit()

def guess():
  if number == int(textBox.get(1.0, 'end-1c')):
    congrats = tk.Label(window, text= "Congrats you win!!!").pack()
    exitButton.pack()
  else:
    count = count - 1
    tryAgain = tk.Label(window, text = "Try Again!").pack()

def startButton():
  count = 10
  number = random.randint(0, 101)
  exitButton = tk.Button(window, text="Press this to exit!", command=quit)
  
  # Create while loop that accounts for running down guesses and guessing the correct number. 
  while count != 0:
    questionText = tk.Label(window, text = "What number am I thinking of between 1 and 100? You have " + str(count) + " guess left. ")
    textBox = tk.Text(window, height=1, width=10)
    textBox.pack()
    guessButton = tk.Button(window, text="Press to guess.", command= guess).pack()

  ranOut = tk.Label(window, text = "You ran out of guesses :( better luck next time!").pack()
  exitButton.pack()

#Step 3. Create the start Button
startButton = tk.Button(window, text="Press this to start the game!", command=startButton)
startButton.pack()

window.mainloop()