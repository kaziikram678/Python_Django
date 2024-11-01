#A function to implement FizzBuzz game
def fizzbuzz(n):
    if n%3==0 and n%5==0: #checking if the number is divisible by both 3 and 5
        return print("FizzBuzz") #returning FizzBuzz
    if n%3==0: #checking if the number is divisible by 3
        return print("Fizz") #returning FizzBuzz
    elif n%5==0: #checking if the number is divisible by 5
        return print("BUZZ") #returning FizzBuzz
    

number = int(input("Enter a Number: ")) #taking input of number

fizzbuzz(number) #callling FizzBuzz
    