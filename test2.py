import sys
import random

class Question(object):
    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options

    def ask(self):
        print (self.question + "?")
        for n, option in enumerate(self.options):
            print ("%d) %s" % (n + 1, option))

        response = int(sys.stdin.readline().strip())   # answers are integers
        if response == self.answer:
            print ("CORRECT")
        else:
            print ("wrong")

questions = [
    Question("How many legs on a horse", 4, ["one", "two", "three", "four", "five"]),
    Question("How many wheels on a bicycle", 2, ["one", "two", "three", "twenty-six"]),

    # more verbose formatting
    Question(question="What colour is a swan in Australia",
             answer=1,
             options=["black", "white", "pink"]),    # the last one can have a comma, too
    ]

random.shuffle(questions)    # randomizes the order of the questions

for question in questions:
    question.ask()
