---
layout: post
title: python quiz
type: tangibles
courses: {csp: {week: 3}}
permalink: /js-python-quiz
---

```python
import getpass, sys
def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg
questions = 3
correct = 0
print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_with_response("Are you ready to take a test?")
rsp = question_with_response("What is the best baby name?")
if rsp == "jayden":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")
rsp = question_with_response("Does Will smell?")
if rsp == "yes":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")
rsp = question_with_response("Who is the next president of the USA")
if rsp == "jayden chen":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")
print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))
```

## Code Explanation

This Python code is a simple quiz-like program that asks the user a series of questions and keeps track of how many questions they answered correctly. Here's how it works:

1. It imports two modules, `getpass` and `sys`.

2. It defines a function called `question_with_response(prompt)` that takes a single argument `prompt`, which is the question to be asked. Inside the function:
   - It prints the question with "Question: " prefix.
   - It uses the `input()` function to read the user's response and store it in the variable `msg`.
   - It returns the user's response (`msg`).

3. It initializes two variables, `questions` and `correct`. `questions` is set to 3, indicating that there will be 3 questions in the quiz, and `correct` is set to 0, indicating that the user has not answered any questions correctly yet.

4. It prints a welcome message that includes the username of the person running the script (retrieved using `getpass.getuser()`) and the path to the Python executable being used (retrieved using `sys.executable`).

5. It informs the user that they will be asked a specific number of questions, which is determined by the `questions` variable.

6. It calls the `question_with_response()` function to ask the user if they are ready to take the test and stores their response in the variable `rsp`.

7. It asks the first question: "What is the best baby name?" and stores the user's response in the variable `rsp`. It then checks if the response is equal to "jayden" and prints a corresponding message indicating whether it's correct or incorrect. If it's correct, it increments the `correct` variable.

8. It asks the second question: "Does Will smell?" and follows the same process as the previous question.

9. It asks the third question: "Who is the next president of the USA" and follows the same process.

10. Finally, it prints the user's username, the number of correct answers (`correct`), and the total number of questions (`questions`) to display the user's score.

So, when you run this code, it will ask the user three questions and provide feedback on whether each answer is correct or incorrect. It will also display the user's final score at the end of the quiz.  