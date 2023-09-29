# a dictionary that stores questions and answers
# have a variable that tracks he score of the player
# loop through the dictionary using key value pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1": {
        "question": "What is the Capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the Capital of Nigeria?",
        "answer": "Abuja"
    },
    "question3": {
        "question": "Who is the  President of Nigeria?",
        "answer": "Bola Tinubu"
    },
        "question4": {
        "question": "Who is the  President of South Africa?",
        "answer": "Bola Tinubu"
    },
        "question5": {
        "question": "Who is the  President of Spain?",
        "answer": "Bola Tinubu"
    },  
        "question6": {
        "question": "Who is the  President of Singapore?",
        "answer": "Bola Tinubu"
    },
}

score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer? ')

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print("Your score is: " + str(score))
        print('')
        print('')

    else:
        print('Wrong')
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score))
        print('')
        print('')

print('You got ' + str(score) + "out of 6 correctly")
print('Your percentage is ' + str(int(score/6 * 100)) + '%')