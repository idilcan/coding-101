"""
Hello new programmer!
This is the very first code intoduction for Python. We're visiting some key points.

Topics:
    1) Interreacting with the program
    2) Data Types
    3) Variables
    4) Frequently used operators

"""

#ITEREACTING WITH THE PROGRAM

print("Hello, Programmer!") #this will write the "Hello, Programmer!" text to the screen using the command line
whatup = input("How are you?") #this will write "How are you?" to the command line and wait for you to respond
#when you complete your response just press enter so that the program can understand you're done!
print(whatup) #this will print what you entered the screen to the question.

#DATA TYPES#

someInteger = 14 #creating a variable named 'someInteger' and assigning it the integer value of 14
print(someInteger) # printing the value of 'someInteger' to the console > '14'

someInteger = 15 # chanhin the value of the variable 'someInteger' to 15
print(someInteger) # > '15'

f = 3.14 #creating a variable f(loat) and assigning it the float value of 3.14

c = 'i' #creating a variable c(har) and assigning it the character 'i'

s = "Hello, World!" #creating a variable s(tring) and assigning it the string "Hello, World!"

b = True #creating a variable b(oolean) and assigning it the boolean value TRUE
b = False #reassigning the variable b with the boolean value FALSE

#OPERATORS

i = 7 #creating a variable i and assigning it the integer value of 7
print(i) # > '7'
i = 2 + 3 #changing the value of variable i to 2 + 3 
print(i) # > '5'
i = 8 - 2 #changing the value again, but this time we're using substraction: 8 - 2 = 6
print(i) # > '6'
i = someInteger - 10 # changing the value of i once again, but this time we're using the previously declared variable 'someInteger' ans substraction
#since the last value of 'someInteger' is 15, 15 - 10 = 5
print(i) # > '5'

x = 6 #creating a new variable x and assigning it the value 6

x = x-5 #this will substract the value of 5 from the value of x and it will write the value to x
# ps. think of variables like placeholders they are not math's x's they do not have a fixed value and they are not unknowns 
# in a mathmatical equation. The given equation is actually x = 6 - 5 
x -= 5 #this is a shprtcut for the above equation. There is no need for confusion. 
#This is simply the same thing with x = x - 5 

x += 5 # x = x + 5
x *= 5 # x = x * 5
x /= 5 # x = x / 5

y = i // x #this is not the same thing with the i / x. This operator is called "Integer division". By nature, when doing a division
# python translates the value to float even if the result is an integer. If we are sure that we want an Integer as a result of division,
#we use this operator.

z = x % i # this is a mode operator. This calculates the reamin part from x // i
# in short z + (y * i ) = x in a mathmatical language

k = x < i # this is our well known smaller operator, this can also be '>' as a greater operator
# if we put '=' operator to their right hand side ('<=' or '>=') they will become 'smaller or equals to' or 
# 'greater or equals to' operators. The output of these operators are always boolean.

k = x == i #this operator is called 'comperative equals'. this is not the same with the 'assigning equals'('=').
# if one is used for others' place it may create a mess which is hard to catch. this operator compraes the two datas given on its two sides. 
# the output is always boolean

b = x != i # this is the 'not equals' operator which is pretty self explainatory


k = k and b #this is how we handle logical AND operation (1 AND 1 = 1 and everything else is 0)
k = k or b #logical OR (0 OR 0 = 0 and everything else is 1)
k = not k #logical NOT (NOT 1 = 0 and NOT 0 = 1)
k = k ^ b #logical XOR (1 XOR 0 and 0 XOR 1 are 1 and others are 0)

# ps. when talking logic 1 means TRUE and 0 means FALSE in Python. 

"""
This is the end of the first code explaination. I hope this was helpful.
If you have any feedback, question or idea, don't hesidate to contact me.

@idilcan at github
"""
