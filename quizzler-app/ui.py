from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)

        self.score = 0
        self.score_text = Label(text=f"Score: {self.score}", bg= THEME_COLOR, fg="white")
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="ew", padx=50, pady=50)

        self.true_button = Button()
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button.config(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button()
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button.config(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # burada beyaz yapıyoruz
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_text.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)