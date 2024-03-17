#Maru Puran
#October 12
#In order to get familiar with functions and subroutines and how they're made, look at code written and predict what is going on and what'll happen when the code is run

# Example Code 1

def say_hi(): #creating a subroutine say_hi
  print("Why hello there!") #when subroutine called prints the words "Why hello there!"

def offer_drink(): #creating a subroutine offer_drink
  print("Would you care for a spot of tea?") #when subroutine called prints the question "Would you care for a spot of tea?"

def offer_food(): #creating a subroutine offer_food
  print("Biscuit?") #when subroutine called prints the question "Biscuit?"

def say_bye(): #creating a subroutine say_bye
  print("Cheerio then.") #when subroutine called prints the words "Cheerio then."


offer_drink() #call the subroutine offer_drink, printing the words "Would you care for a spot of tea?"
say_hi() #call the subroutine say_hi, printing out the words "Why hello there!"
offer_food() #call the subroutine offer_food, printing out the words "Biscuit?"

# Example code 2
def maths1(): #creating subroutine maths1
  num1 = 50 #assigning the value of 50 to created variable num1
  num2 = 5 #assigning the value of 5 to created variable num2
  return num1 + num2 #returns the sum of both numbers, 55

def maths2(): #creating subroutine maths1
  num1 = 50 #assigning the value of 50 to created variable num1
  num2 = 5 #assigning the value of 5 to created variable num2
  return num1 - num2 #returns the difference of num1 and num2, 45

def maths3(): #creating subroutine maths3
  num1 = 50 #assigning the value of 50 to created variable num1
  num2 = 5 #assigning the value of 5 to created variable num2
  return num1 * num2 #returns the product of both numbers, 250

outputNum = maths2() #assigns the maths2 subroutine to output num, or the value of 45
print(outputNum) #prints the value of 45 on the screen

# Example Code 3
def location(country): #create subroutine location alongside a parameter
  print("I am from " + country) #prints the words "I am from" and the value of the argument used in country upon being called

location("Brazil") #prints the words "I am from Brazil"

