from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizGui():

    def __init__(self, quiz: QuizBrain):

        self.quiz_logic = quiz
        self.root = Tk()
        self.root.title("Quiz")
        self.root.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text="Score:0", bg=THEME_COLOR,fg="white", font=("Arial", 15, "italic"))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150,125, width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_photo = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_photo, highlightthickness=0, bd=0, command=self.true_button)
        self.right_button.grid(column=0, row=2)

        wrong_photo = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_photo, highlightthickness=0, bd=0, command=self.wrong_button)
        self.wrong_button.grid(column=1, row=2)

        self.button_disabled()
        self.timer = self.root.after(1000, self.get_next_question)

        self.root.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz_logic.score}")
        if self.quiz_logic.still_has_questions():
            q_text = self.quiz_logic.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
            self.button_enabled()

        else:
            self.canvas.itemconfig(self.canvas_text, text = f"You finish the quiz! \n "
                                                            f"Your score is {self.quiz_logic.score}/{self.quiz_logic.question_number}")
            self.button_disabled()

    def true_button(self):
        self.give_feedback(self.quiz_logic.check_answer("True"))

    def wrong_button(self):
        self.give_feedback(self.quiz_logic.check_answer("False"))

    def give_feedback(self, is_right):
        self.button_disabled()
        self.root.after_cancel(self.timer)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.update()
        self.timer = self.root.after(1000, self.get_next_question)

    def button_enabled(self):
        self.right_button.config(state="active")
        self.wrong_button.config(state="active")


    def button_disabled(self):
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")


    # def score_update



