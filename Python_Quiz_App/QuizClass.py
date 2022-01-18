import os,time
from termcolor import colored

class Questions:
    def __init__(self,question,option):
        self.questions=question
        self.options=option

    def new_game(self):
        guesses = []  # stor user input
        correct_guesses = 0
        question_num = 0  # index of question
        counter = 0  # question counter

        for key in self.questions:  # Print Questions one by one
            print("------------------------")
            counter += 1
            print(counter, ".", key)
            for i in self.options[question_num]:  # Print all answer of the question
                print(i)
            quess = input("Enter (A, B, C, or D): ")
            guess = quess.upper()
            guesses.append(quess.upper())  # Append user guess to the guesses list

            correct_guesses += self.check_answer(self.questions.get(key), guess)  # count number of correct answer

            question_num += 1

        self.display_score(correct_guesses, guesses)

    def check_answer(self,answer, guess):  # check answer true or false
        if answer == guess:
            print(colored("Correct!", 'green'))
            return 1
        else:
            print(colored("Wrong!", 'red'))
            return 0

    def display_score(self,correct_guesses, guesses):
        print("------------------------")
        print("Results")
        print("------------------------")

        lst = []  # store correct answer of all questions
        for i in self.questions:
            lst.append(self.questions.get(i))

        print("Correct Answer", "      ", "Your Guess")        #print correct answers and user guesses
        for i, (correct, answer) in enumerate(zip(lst, guesses)):
            if correct == answer:
                print("   ", correct, "                   ", answer)
            else:
                print("   ", correct, "                   ", colored(answer, 'red'))


        print()

        score = int(correct_guesses / len(self.questions) * 100)  # calculate user score
        print("Your score is: " + str(score) + "%")

    def play_again(self):  # repeate the game more and more
        again = input("Do you want to play again? (yes or no): ")
        again = again.upper()
        if again == "YES":
            return True
        else:
            return False


