name = input("Name: ")
print("Hello {}".format(name))
print("We will begin the quiz. There will be 3 questions about capital cities around the world. Answer with 'Yes' or 'No' for the first two questions! Ready, set go!")
answer = input("Is Ottawa the capital of Canada?")
if answer == "Yes":
    print("Correct! Moving on...")
elif answer == "No":
    print("Sorry, that is incorrect. Moving on...")
else:
    print("We do not recognize your answer. Remember to only answer with 'Yes' or 'No.'")

answer_2 = input("Is Rio de Janeiro the capital of Brazil?")
if answer_2 == "No":
    print("Correct! The real capital of Brazil is Brasilia. Moving on...")
elif answer_2 == "Yes":
    print("Sorry, that is incorrect. The real capital of Brazil is Brasilia.")
else:
    print("We do not recognize your answer. Remember to only answer with 'Yes' or 'No.'")
    
answer_3 = input("Last question! What is the capital of Australia?")
if answer_3 == "Canberra":
    print("Correct!")
elif answer_3 == "Sydney":
    print("Sorry that is incorrect! Although many people think that the capital of Australia is Sydney, it is actually Canberra.")
else:
    print("Sorry that is incorrect!")
    
if answer == "Yes" and answer_2 == "No" and answer_3 =="Canberra":
    print("You have reached the end of the quiz. Your score is 100%! Good job {}!".format(name))
else:
    print("You have reached the end of the quiz. Although you did not receive 100%, you still tried and that's what matters.")
