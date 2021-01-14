import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#ffffff"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", font=("Arial", 12, "normal"), fg=WHITE, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.q_num_label = tk.Label(text="", font=("Arial", 15, "bold"), fg=WHITE, bg=THEME_COLOR)
        self.q_num_label.grid(column=0, row=0, sticky=tk.S + tk.W)

        self.canvas = tk.Canvas(width=300, height=250, bg=WHITE)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question text",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(command=self.submit_true, image=true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(command=self.submit_false, image=false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Displays the next question or final results if there are no more questions."""
        self.canvas.config(bg=WHITE)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.q_num_label.config(text=f"Question: {self.quiz.question_number}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz. Your final score was: "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def submit_true(self):
        """Checks to see if True is the right answer"""
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def submit_false(self):
        """Checks to see if False is the right answer"""
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        """Flashes a green or red color on the canvas depending on right/wrong answer."""
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
