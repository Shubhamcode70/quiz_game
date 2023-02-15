from data2 import question_data
from question import Questions
from QuizBrain import QuizBrain


question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    #creating object of Questions class and passing the attributes to it
    new_questions = Questions(text, answer)
    #apending the value to blank question bank
    question_bank.append(new_questions)

quizb = QuizBrain(question_bank)
while quizb.still_has_questions():
    quizb.next_question()

print(f"You have completed the Quiz. \nYour final score is {quizb.score}/ {len(quizb.question_list)} :")

