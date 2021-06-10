"""
This program creates random quiz questions by combinating keys(states) and values(capitals) from file
"""

import random
import os
import re

quiz = {'Austria': 'Vienna',
    'Belgium': 'Brussels',
    'Denmark': 'Copenhagen',
    'Finland': 'Helsinki',
    'France': 'Paris',
    'Hungary': 'Budapest',
    'Ireland': 'Dublin',
    'Italy': 'Rome',
    'Portugal': 'Lisbon',
    'Slovenia': 'Ljubljana',  }



working_dir = '04_quiz'
answers_total = 3


def create_questions():
    if not os.path.isdir(working_dir):
        os.mkdir(working_dir)
    path = os.path.join(os.getcwd(), working_dir)
    os.chdir(path)

    tmp_dict = quiz.copy()                                                  # using .copy to get a copy of dict instead of reference
    for quiz_index in range(len(quiz)):
        country = random.choice(list(tmp_dict.keys()))                      # get country
        correct_answer = tmp_dict.pop(country)                              # its capital is saved as correct answer

        quiz_answer_filename = 'quiz_answer_%s.txt' % (quiz_index + 1)               #
        answer_file = open(quiz_answer_filename, 'w')                                # add correct answer to file
        print(correct_answer, file = answer_file)                                #

        answers = [correct_answer]
        while len(answers) < answers_total:
            capital = random.choice(list(quiz.values()))                    #
            if capital not in answers:                                      # other possible answers are chosen from all countries capitals
                answers.append(capital)                                     #

        quiz_question_filename = 'quiz_question_%s.txt' % (quiz_index + 1)          #
        question_file = open(quiz_question_filename, 'w')                           #
        print ('The capital of ' + country + ' ?' , file = question_file)           # print question text into file
        for index in range(len(answers)):                                           #
            print(str(index + 1) + ') ' + answers.pop(random.randint(0, len(answers) - 1)), file = question_file, end='\n')

def ask_question(question_index):
#    question_index = random.randint(0, len(quiz)) + 1
    quiz_question_filename = 'quiz_question_%s.txt' % (question_index)
    question_file = open(quiz_question_filename, 'r')
    lines = question_file.read()
    question_file.close()
    print(lines)

    quiz_answer_filename = 'quiz_answer_%s.txt' % (question_index)
    answer_file = open(quiz_answer_filename, 'r')
    input_answer = ""
    while input_answer == "":
        input_answer = input("Please enter a number:")
    ansRegex = re.compile(rf'{input_answer}\)\s+(\w+)')
    input_answer = ansRegex.search(lines).group(1)
    correct_answer = answer_file.read().strip()

    if input_answer == correct_answer:
        print("You answered correct")
    else:
        print("You answered wrong")
    answer_file.close()

create_questions()
for question in range(len(quiz)):
    print(question)
    ask_question(question + 1)
ask_question(10)
