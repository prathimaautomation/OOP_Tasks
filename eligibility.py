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

