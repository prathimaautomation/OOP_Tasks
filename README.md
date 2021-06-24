#### Create a class and function to achieve this.
# Control Flow Age and Permission

## Timings

30 Minutes

## Summary

Simple program to use control flow!

## Tasks

* rules of what the program to do are followed, see bellow

Starter code
```
age = 19
driver_licence = True


# - You can vote and drive
# - You can vote
# - You can driver
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


 #  as a user I should be able to keep being prompted for input until I say 'exit'

```

## Acceptance Criteria
* class created with required function/s 
* is a program that run continuously
* handles strings and integers
* has exist condition
* all business logic works

### Solution to the above Task:
- Let's create a class to see things_can_do
- create a help method to see what is the exit criteria
- prompt the user to input the age 
```python
step 1: created an Eligibility class to check the age related stuff
class Eligibility:
    driver_licence = True
    
    def check(self, age):
            try:
                self.age = int(age)
                if self.age >= 19 and self.driver_licence == True:
                    print("You can drive and vote")
                elif self.age >= 18:
                    print("You can vote!")
                elif self.age >= 16:
                    print("you can't legally drink but your mates/uncles might have your back")
                else:
                    print("You are too young, go back to school.")
            except:
                print("That's not valid input. Please enter either age as 'int' or 'EXIT'")
step 2: create things_can_do class to prompt the user continuously and check eligibility by importing Eligibility class 
class Things_can_do():
    keep_going = True
    
    while keep_going:
        age = input("Enter your age or type 'EXIT' to quit: ")
        if age == "EXIT":
            keep_going = False
        Eligibility().check(age)
#Finally create an object of the Things_can_do class        
check_things_can_do = Things_can_do()

```