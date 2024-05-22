#!/usr/bin/env python3

def happy_new_year():
    counter=10
    while counter > 0:
        print(counter)
        counter -=1
    print("Happy New Year!")


def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
    
def square_integers(int_list):
    return [i**2 for i in int_list]
