from functies import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox # if you want to send messages to the user.

# functions
def calculate():
    textToBeCalculated = calculateInput.get('1.0', 'end') # get all the text from inputfield
    characterLabel.config(text =f"Karakters: {getNumberOfCharacters(textToBeCalculated)}")
    sentencesLabel.config(text =f"Zinnen: {getNumberOfSentences(textToBeCalculated)}")
    WordsLabel.config(text =f"word(en): {getNumberOfWords(textToBeCalculated)}")
    AviScore.config(text =f"AviScore: {GetAviscore(textToBeCalculated)}")
    


#variables TK
root = tk.Tk()              # create tkInter window
root.title('Text analyser') # set title
root.geometry('600x600')    # set dimension
calculateInput = tk.Text(root, width = 70, height = 30, background='lightgrey')            # generate imput element
calculateButton = ttk.Button(root, text='Bereken score(s)', command=calculate)        # generate button when pressed -> calculate
characterLabel = tk.Label(root, text=f'Karakters:', width=20, bg='black', fg='white') # generate characterLabel
sentencesLabel = tk.Label(root, text=f'Zinnen:', width=20, bg='black', fg='white')    # generate sentencesLabel
WordsLabel = tk.Label(root, text=f'word(en):', width=20, bg='black', fg='white')      
AviScore = tk.Label(root, text=f'Avi Score:', width=10, bg='black', fg='white') 


calculateInput.place(x=20, y=20)   # place is one of the ways to put elements on root (window).
calculateButton.place(x=20, y=520)
characterLabel.place(x=180, y=560) 
sentencesLabel.place(x=20, y=560)
WordsLabel.place(x=340, y=560)
AviScore.place(x=500, y=560)

# start program
root.mainloop() # runs until stopped with default stop button.
