class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        self.tries = 0

    def next_question(self):
        current_question= self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer

        user_answer = input(f"Q.{self.question_number+1}: {current_question}. (True/False)? ")
        self.question_number += 1
        self.check_answer(user_answer,correct_answer)
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,u_answer, c_answer):
        self.tries += 1
        if u_answer == c_answer:
            self.score += 1
            print("You are correct.")
        else:
            print("You are wrong")
        print(f"Correct answer is {c_answer}.Your score is {self.score}/{self.tries}\n")





