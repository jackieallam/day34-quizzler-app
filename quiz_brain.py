import html


class QuizBrain:

    def __init__(self, q_list: list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """Checks to see if any questions remain and returns boolean"""
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """Gets the next question from the list and formats it (unescaping HTML Entities)"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        ques_text = html.unescape(self.current_question.text)
        return f"{ques_text}"

    def check_answer(self, user_answer: str) -> bool:
        """If user's answer is correct, returns True. If their answer was wrong, returns False."""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
