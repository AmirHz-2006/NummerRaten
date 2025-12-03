import random
from tkinter import *
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self):
        self.window = Tk()
        self.window.title("Guess the Number Game")
        self.window.geometry("500x430")
        self.window.resizable(False, False)
        self.color = "#6677ee"
        self.window.configure(bg = self.color)

        # Variablen initialisieren
        self.min_range = 1
        self.max_range = 100
        self.number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        self.max_attempts = 10
        self.game_controller = True                 # Flagge für Spielstatus
        self.difficulty = StringVar(value="mittel")