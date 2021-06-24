from eligibility import Eligibility

class Things_can_do():
    keep_going = True

    while keep_going:
        age = input("Enter your age or type 'EXIT' to quit: ")
        if age == "EXIT":
            keep_going = False
        Eligibility().check(age)

check_things_can_do = Things_can_do()
