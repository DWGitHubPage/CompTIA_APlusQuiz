# Python 3.7.4

import random
import time
from questions import questions 


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

input('This is a quiz that consists of 70 questions. Please press "enter" to start.\n')
print("\n")


def run_quiz(questions):
     random.shuffle(questions) 
     score = 0
     for question in questions:
          answer = input(question.prompt)
               
          if answer == question.answer:
               score += 1
               print('\nOh yeah!')
               time.sleep(1)
               
          if answer == question.answer.upper():
               score += 1
               print('\nYou got it!')
               time.sleep(1)
               continue
               
               if answer != question.answer.upper():
                    print('Does not work.')
                    time.sleep(1)
                     
          if answer != question.answer:
               print('\nIncorrect.')
               time.sleep(1)


     print('\nYou got', score, 'out of', len(questions))

run_quiz(questions)




