
#Function definition(prompt, answer): this function asks question and checks useranswer is correct and returns a point if answer is correct
def question (prompt, answer):
    point=0
    useranswer=input(prompt)
    print(f'{useranswer}')
    if useranswer.casefold() == answer.casefold():
        print ('Great Job! Thats Correct time for the next question!')
        point= point + 1
    else:
        print('Sorry that is incorrect.')
    return point

#Asking name before quiz
name=input("What is your name?")
print(f'Hi {name}! Are you ready for the quiz!')
score=0



#Question 1 sequence
score=score+question('How many planets are in the solar system?', '8')

#Question 2 sequence
score=score+question('What sport does Lionel Messi play?', 'soccer')

#Question 3 sequence
score=score+question('How many continents are there?','7')
     


#Score/percentage calculation
percentage = (score/3)*100

print (f'Your score is {percentage:.2f}%')






