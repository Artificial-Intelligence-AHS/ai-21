"""
ALL WRONG
"""

"""
//sinle-line comment

//int
x = 5
//string
y = "five"
//boolean
z = true

//it is displaying the type of variable it is (int, string, boolean)
//will print int or integer
print(type(x))

//to name a variable us camelCase| first word is all lowercase, then the rest of the words are all first letter uppercase
carTypesNamed = ["Volvo", "Honda", "Toyota"]

//str; float; bool; int

//Arrays are a list of variables (1 or more) that are in a list
carTypesNamed = ["Volvo", "Honda", "Toyota"]
//^this is an array
numbers = [1, 2, 3, 4]
trueOrFalse = [true, false, true, false]
carTypesNamed.add("Hyundai")
//carTypesNamed is now ["Volvo", "Honda", "Toyota", "Hyundai"]
carTypesNamed.remove("Hyundai")
//with remove if Hyundai isn't there it will give an error
carTypesNamed.discard("Hyundai")
//with discard if Hyundai isn't there it will not give an error
carTypesNamed.pop()
//will remove the last value
del carTypesNamed
//removes the arrays

//printing
print("Hello World.")
x = "Hello World."
print(x)
print(1)

//Casting
x = 5
str(x)
x = str(5)
x = float(8)
//Changing the automatic variable type to a different variable type(integer to string)

//String are arrays of letters ("abc" = ["a", "b", "c"]), Special type of array
x = "Hello"
print(len(x))
//finds the length of the word (count of letters)

//to make all the letters in a string uppercase, use upper()
x = "Hello"
print(x.upper())
print(x.lower())

//string concatenation
x = "Hello"
y = "World."
//adding two strings together
print(x + " " + y)
//Hello World.
x = 5
y = "Worlds"
print(x + y)
//error, string concatenation can only be done through two strings, you can't concatenate a string and a integer (5)
print(str(x) + y)
//5Worlds

"""
""" +; -; *; /; %; **"""
"""
// + is addition
// - is subtraction
// * is multiplication
// / is division
// % is dividing and finding the remainder (5 % 2 = 1)

//incrementation
//to increment a variable
x = x + 1
x += 1
//decrementation
x = x - 1
x -= 1

//If you want a variable that cannot be changed (Constant)
import constant
//Import is a library(A large amount of code that somebody else already programmed, simplifies it (Random number generators, the print statement, opening up your webcam))
Pi = 3.14
constant.Pi

//Tuple is an array that can't be changed

tuple = ("Tuple1", "Tuple2", "Tuple3")

//sets are unordered and cannot be changed versions of an arrays
set = {"Apple", "Potato", "Banana"}
//every time you print it, it will likely be in a different order

//Inputs, Inputs take an input from the person and can store and/or use that value
input()
//just takes the input, doesn't store it or anything
x = input()
//this takes the input and stores it as x, u can use it afterwords
"""
"""The bigger stuff"""
"""
//If statements, if a condition is true then it will run
a = true
if a:
    print("a is true")
elif !a:
    print("a is false")
//If is checking if a is true (if nothing is specified than its checking if its true or false)
if a > b:
    print("a is greater than b")
if a == b:
    print("a is equal to b")
// == is what is used to find if something is equal because = is used to asign a variable
//elif stands for else if
//if this is true do this (if) but if it isn't true then check if this is correct (elif) and if none of these are true than do this (else)

//while loops say that as long as this is true, then do this
//as long as x is true do whats indented under while (change x to false), since it changes x to false, it will only run concatenate
x = true

while x:
    x = false

x = 1
while x < 5
    x++
//will run four times
//be careful can cause a infinite loop

y = 1
for x in range(6):
    print(y)
    y++
//This makes a for loop
//loops a certain amount of times, when you know how many times you want it to round
//will print 1, 2, 3, 4, 5, 6

print("How many numbers do you want to print")
user = input();
for x in range(user):
    x = 1
    print(x)
    x ++

//a function is like a library except you program a big thing and you can easily call it by the name of the function
//technically, this below code does nothing, you won't see anything

def theFunction():
    print("what is your name")
    name = userInput()
    print("HI " + name)

//this will call the function, a simple way to make  3 lines of code into 1, can be used to make code look a lot simpler
theFunction()

"""
"""try and except
the try will try a part or the entire code
the except will happen if it raises and error
if no error happens you can just pass it, or you can do something call else, which will do something if it works
finally can be used to do something even if it gets an error or not"""
"""
try:
    print(woah)
    //x is not defined so it should raise an error
except:
    print("An error was raised")
else:
    print("No error was raised")
finally:
    print("We finished the try and except portion")
//Could be used if a password was entered(a number only password and the password entered had a string, would be used to say that it doesn't contain a letter)
"""