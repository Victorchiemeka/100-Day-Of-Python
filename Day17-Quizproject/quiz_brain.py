class Brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list
        self.score = 0

    def stillquestion(self):
        return self.question_number < len(self.list)

    def next_question(self):
        current_question = self.list[self.question_number]
        self.question_number += 1
        useranswer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False):"
        )
        self.checkanswer(useranswer, current_question.answer)

    def checkanswer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("You got it wrong")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
