# Megan Milarcik
# a quiz game

print("Welcome to my quizzes!")
print("This quiz is about Pop Culture, Animals, or Fun Facts!")
print("It is your choice which quiz you would like to take.")

pop_culture = 'Pop Culture'
animal_related = 'Animals'
fun_facts = 'Fun Facts'

questions = [pop_culture, animal_related, fun_facts]

quiz = {pop_culture: [("Beyonce sings the song, Drunk in Love", True),
                        ("According to Netflix, Is pink the new black?", False),
                        ("Selena Gomez swong on a wrecking ball for a music video", False)],

        animal_related: [("Rabits are born blind", True),
                         ("Pickles are known as a group of hedgehogs", True),
                         ("A buck is a female deer", False)],

        fun_facts: [("France invented pizza", False),
                     ("92% of a watermelon is water", True),
                     ("The CIA stands for Canada In America", False)]

}
result = {"Correct": 0, "Incorrect": 0}

def get_quiz_choice():
    while True:
        try:
            quiz_number = int(input(
                'Choose the quiz you like\n1 for {}\n2 for {}\n3 for {}\nYour choice:'.format(pop_culture,
                                                                                          animal_related,
                                                                                          fun_facts)))
        except ValueError:
            print("Not a number, please try again\n")
        else:
            if 0 >= quiz_number or quiz_number > len(quiz):
                print("Invalid value, please try again\n")
            else:
                return quiz_number

def get_answer(question, correct_answer):
    while True:
        try:
            print("Q: {}").format(question)
            answer = int(input("1 for True\n2 for False\nYour answer: "))
        except ValueError:
            print("Not a number, please try again\n")
        else:
            if answer is not 2 and answer is not 1:
                print("Invalid value, please try again\n")
            elif bool(answer) is correct_answer:
                result["Correct"] += 1
                return True
            else:
                result["Incorrect"] += 1
                return False

choice = get_quiz_choice()
quiz_name = questions[choice - 1]
print("\nYou chose the {}\n").format(quiz_name)
quiz_questions = quiz[quiz_name]
for q in quiz_questions:
    print("Your answer is: {}\n").format(str(get_answer(q[0], q[1])))



