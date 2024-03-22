#import random
import random

# we need two variables the computer score and your scope

#initliaze both score to zero cause yk we starting off at zero
my_win = 0 
computer_win = 0
options = ["rock", "paper", "scissors"]# this is our rock paper scissors

#starting off our input
#also if they want to quit
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()#we made it .lower so its easier to track
    if user_input == "q":#since we had .lower it will go straight to q
        break# we want to quit if they type in q
    
    if user_input not in options:#we are checking if the user input is inside this list which has rock paper scissors
        continue#continue will basically loop and have them keep asking the same question 

    random_number = random.randint(0,2)# if we got here that means they have a valid input and now we need to make sure rock pape scissors equals a value
    # rock = 0, paper = 1, scissors = 2
    #we can do 3 if statements to assign each one but we will use the list
    computer_pick = options[random_number]#so now our computer pick will equal a random index value and it will go take the index value from our options list 
    print("Computer picked:", computer_pick + ".")
# now we are doing our win conditions
    if user_input == "rock" and computer_pick == "scissors":# you have to pick rock and comptuer has scissors then you win cause rock beats scissors
        print("You won!")
        my_win += 1
        
    elif user_input == "paper" and computer_pick == "rock":# you have to pick paper and comptuer has rock then you win cause paper beats rock
        print("You won!")
        my_win += 1
        
    elif user_input == "scissors" and computer_pick == "paper":# you have to pick scissors and comptuer has paper then you win cause scissors beats paper
        print("You won!")
        my_win += 1 
    elif user_input == "rock" and computer_pick == "rock":# if you both pick the same thing
        print("It's a tie")
        my_win += 0
        computer_win += 0
    elif user_input == "paper" and computer_pick == "paper": #if you both pick the same thing
        print("It's a tie")
        my_win += 0
        computer_win += 0
    elif user_input == "scissors" and computer_pick == "scissors":# if you both pick the same thing
        print("It's a tie")
        my_win += 0
        computer_win += 0
    else:# now if you fail then it will print you fail and give the computer a point
        #we dont need to check the computer ones because it will automatically be a lose
        print("You lost!")
        computer_win += 1

#if computer won more than you have a little funny moment
if computer_win > my_win:
    print('you suck lol')
elif computer_win == my_win:# if you and the computer both have same amount of wins
    print("You a bot just like the bot")
else:# if you beat the bot
    print("Good job you beat a bot")

print(f"You won {my_win} times!") #this is my wins
print(f"Computer won {computer_win} times!")  #this is computer wins     
print("Goodbye!")#this is for when they decide to leave the game





