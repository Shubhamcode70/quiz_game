class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print(f"You are right, Your score is {self.score}")
        else:
             print("You are wrong")
        print(f"Correct answer is {correct_ans}\nYour Current score is {self.score}/ {len(self.question_list)}")

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no} {current_question.text} (True/False) : ")
        self.check_answer(user_ans, current_question.answer)
        print("\n")





