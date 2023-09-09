from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create a label on the top
        self.score_label = Label(text="Score: 0", fg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.window.mainloop()
