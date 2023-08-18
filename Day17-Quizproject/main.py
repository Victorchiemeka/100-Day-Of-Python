from data import question_data
from question_model import Question
from quiz_brain import Brain

question_bank = []
for all in question_data:
    question_text = all["question"]
    question_answer = all["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Brain(question_bank)
while quiz.stillquestion():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
