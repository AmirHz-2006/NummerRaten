import random
from tkinter import *
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self):
        self.window = Tk()
        self.window.title("Guess the Number Game")
        self.window.geometry("500x430")
        self.window.resizable(False, False)
        self.color = "#4f5fd5"
        self.window.configure(bg = self.color)

        # Variablen initialisieren
        self.min_range = 1
        self.max_range = 100
        self.number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        self.max_attempts = 10
        self.game_controller = True                 # Flagge für Spielstatus
        self.difficulty = StringVar(value="mittel")
        
        self. create_widgets()
    def  create_widgets(self):
        # Titel-Label
        title_label = Label(self.window, text="Number Guessing Game", font=("Arial", 20 , "bold"),
                            fg='white',bg=self.color)
        title_label.pack(pady=18)

        # Anleitung-Label
        instruction_label = Label(self.window,
                                     text=f"Im thinking of a number between {self.min_range}"
                                          f" and {self.max_range}.\n Can you guess it?",
                                     font=("Arial", 13 ,'bold') , bg=self.color , fg='white')
        instruction_label.pack(pady=5)

        # Eingabefeld
        self.input_entry = Entry(self.window, font=("Arial", 16) ,width=15, justify='center')
        self.input_entry.pack(pady=10)
        self.input_entry.bind('<Return>', lambda event: self.check_guess())
        self.input_entry.focus()

        # Button zum Raten
        self.guess_button = Button(self.window, text="Guess",
                                 font=("Arial", 13), command= lambda : self.check_guess(),
                                 width=12, bg="#4CAF50", fg="white" ,relief='raised' ,cursor="hand2")
        self.guess_button.pack(pady=5)

        # Ergebnis-Label
        self.attempt_text = Label(self.window, text="",
                                     font=("Arial", 12), fg="blue" , bg= self.color)
        self.attempt_text.pack(pady=10)

        # Anzeige der Versuche
        self.attempts_label = Label(self.window, text=f"Attempts : {self.attempts}/{self.max_attempts}",
                                       font=("Arial", 12) , bg = self.color , fg="yellow")
        self.attempts_label.pack(pady=2)

        # Rahmen für Steuerungs-Buttons
        button_frame = Frame(self.window , bg= self.color)
        button_frame.pack(pady=15)

        # Button für neues Spiel
        restart_button = Button(button_frame, text="New Game",
                                   font=("Arial", 12), command= lambda :self.restart_game(),
                                fg='white' , bg="#FF9800" , relief='raised' , cursor="hand2")
        restart_button.pack(padx = 5 , pady=5 , side=RIGHT)
        # Button zum Anzeigen der Antwort
        show_button = Button(button_frame, text= 'Show Answer!',
                             font=("Arial", 12), command= lambda : self.show_answer(),relief='raised',
                             bg="#9C27B0", fg="white" , cursor="hand2")
        show_button.pack(side=LEFT, padx=8)

        # Auswahl für Schwierigkeitsgrad
        difficulty_frame = Frame(self.window, bg=self.color)
        difficulty_frame.pack(pady=5)

        difficulty_label = Label(difficulty_frame, text="Difficulty: ", font=("Arial", 12),
              bg=self.color)
        difficulty_label.pack(side=LEFT, padx=2)

        difficulties = [("Easy (1-50)", "einfach"),
                         ("Medium (1-100)", "mittel"),
                         ("Hard (1-200)", "schwer")]

        for text, mode in difficulties:
            Radiobutton(difficulty_frame, text=text, variable=self.difficulty, indicatoron=0, selectcolor="#4CAF90",
                        value=mode, bg=self.color, fg="white", font=("Arial" , 10 , 'bold'), cursor="hand2",
                        command= lambda : self.change_difficulty()).pack(side=LEFT, padx=4)