#!/usr/bin/env python3

 # here we print the value of i inside the loop which prints from 10-1
# After the loop is done it we print this message
def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print('Happy New Year!')

     
    
# defines a function with and argument of integer list(int_list)
# num variable iterates over each element in the int_list
# the expression num ** 2 calculates the squre of the number  
def square_integers(int_list):
    return [num ** 2 for num in int_list]

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)