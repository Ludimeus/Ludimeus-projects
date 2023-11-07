import csv
import random

print('Welcome to the IrregularVerbs flashcard game!')
with open('IrregularVerbs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    working_list = list(csv_reader)

while True:
    random_working_innerlist = working_list[random.randint(1, len(working_list)-1)]

    random_given = random_working_innerlist[random.randint(0, 3)]
    randint_question = random.randint(0, 3)
    random_question = random_working_innerlist[randint_question]
    random_question_name = None
    if randint_question == 0:
        random_question_name = 'Infinitive'
    elif randint_question == 1:
        random_question_name = 'Simple Past'
    elif randint_question == 2:
        random_question_name = 'Past Participle'
    elif randint_question == 3:
        random_question_name = 'Dutch'
    else:
        print(random_question)
        print('the number of random_question is weird and I am going to cry. For now, good bye')
        exit()
    awnser = random_working_innerlist[randint_question]
    inp = input(f'\nGive the {random_question_name} of {random_given}')
    print(f'The awnser is {awnser}')
