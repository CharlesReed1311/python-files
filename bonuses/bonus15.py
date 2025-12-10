import json 

with open(r"bonuses\questions.json",'r') as file:
    content = file.read()

data = json.loads(content)

score = 0

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1}.{alternative}")
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct!"
    else:
        result = "Wrong!"

for index, question in enumerate(data):
    message = f"{index + 1}.{result} Your answer:{question["user_choice"]}, Correct answer:{question["correct_answer"]}"
    print(message)

print("Your score:",score,"/ 2")