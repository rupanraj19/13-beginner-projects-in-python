# a dictionary containing questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key value pairs
# display each qns to the user and allow them to answer
# tell them right or wrong 
# show the final score

quiz = {
    "q1": {
        "question": "What is the capital of Singapore?",
        "answer": "Singapore"
    },
    "q2": {
        "question": "What is the capital of India?",
        "answer": "New Delhi"
    },
    "q3": {
        "question": "What is the capital of Australia?",
        "answer": "Canberra"
    },
    "q4": {
        "question": "What is the capital of China?",
        "answer": "Beijing"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'] )
    answer = input("Answer: ")
   
    if answer.lower() == value['answer'].lower():
        print("correct")
        score += 1
        print(f"your score is {score}" + "\n")
    else:
        print("wrong")
        print("The correct answer is " + value['answer'])
        score = score

print("Total score " + str(score))