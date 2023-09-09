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

        # Create a canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some questions here",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.window.mainloop()
