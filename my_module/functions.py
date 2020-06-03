#A function named max_score that takes in an integer score as input and gives a unique (and possibly sassy) message depending on how many questions you've got correct!
def max_score(score):            
    
    # using if statement to display unique message bellow if score is equal to 0.
    if score == 0:               
        print("You need to go read those books... like right freaking now.")
    
    # using if statement to display unique message bellow if score is equal to 1.
    elif score == 1:             
        print("I'm betting the only other thing you know about LOTR is 'There's a Wizard named Gandalf', huh?")
    
    # using if statement to display unique message bellow if score is equal to 2.
    elif score == 2:             
        print("Don't beat yourself up! At least your score matches the amount of times Hobbits eat breakfast!")
    
    # using if statement to display unique message bellow if score is equal to 3
    elif score == 3:             
        print("Don't give up! The Elves only had 3 kingdoms left and they beat back Sauron's forces. Play again!")
    
    # using if statement to display unique message bellow if score is equal to 4.
    elif score == 4:           
        print("The Fourth Age was an age of renewal, and self betterment for the Race of Men. I suggest you follow in their  example.") 
    
    # using if statement to display unique message bellow if score is equal to 5.
    elif score == 5:             
        print("You're halfway there, Frodo didn't give up when things got tough, and neither should you! Try again!")
    
    # using if statement to display unique message bellow if score is equal to 6.
    elif score == 6:             
        print("Whelp, you're as well versed in LOTR lore as the average person.")
    
    # using if statement to display unique message bellow if score is equal to 7.
    elif score == 7:             
        print("The same as the number of Rings the Dwarves got!")
    
    # using if statement to display unique message bellow if score is equal to 8.
    elif score == 8:             
        print("The Kingdom of Gondor will be proud to call you an ally with intellect like that!")
    
    # using if statement to display unique message bellow if score is equal to 9.
    elif score == 9:             
        print("OOF! You were so close to achieving your goal, just like the Race of Man was at the foot of Mount Doom... until a certain some one decided to keep a certain Ring...")
    
    # using if statement to display unique message bellow if score is equal to 10.
    elif score == 10:            
        print("You got everything correct! Your knowledge is envied by the great Wizards themselves!")
        
        
        
# Making a function, called "run_test" that takes "questions" from above as an input.
def run_test(questions):
    
    # Assigning base value of 0 to Score.
    score = 0
    
    # Using for loop to loop through q in questions.
    for q in questions:
        
        # Stating that answer is equal to the input of q in prompt.
        answer = input(q.prompt)
       
        # Using if statement to show if user's answer is equal to the chosen answer in questions above:
        if answer == q.answer:
            
            # If answer is correct, it adds 1 to total score value. 
            score = score + 1
            
            
    #Then we print a statement at the end of the quiz, displaying total number of correct score over total score value!
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!") 
    
    # Finally, it runs max_score function with score as input to display unique message.
    max_score(score)             