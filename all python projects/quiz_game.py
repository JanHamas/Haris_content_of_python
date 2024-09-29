
quiz = {
    "question1":{
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    'question2':{
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    'question3':{
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    'question4':{
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    
    'question5':{
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer: " )
    
    
    if answer.lower() == value["answer"].lower():
        print("Correct")
        score +=1
        print("Your score is " + str(score))
        print()
        print()
    else:
        print("Wrong")
        print("The correct answer is " + value["answer"])
        print("your score is " + str(score))
        print()
        print()
print("you got " + str(score) + " out of 5 question ")
print("your persontage is: " + str(int(score/5*100)) )

open("score.txt","w").write(str(int(score/5*100))) and open("score.txt","w").write(str(int(score)))