class MultipleFunctions():

    def subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    def oddeven():
        Number = int(input("Enter the number: "))

        if Number % 2 == 0:
            print(Number, "is an Even Number")
        else:
            print(Number, "is an Odd Number")

    def elligibility():
        gender = input("Enter your gender: ")
        age = int(input("Enter your age: "))

        if (gender == "Male" or gender == "M") and age >= 21:
            print("You are eligible for getting married")
        elif (gender == "Female" or gender == "F") and age >= 18:
            print("You are eligible for getting married")
        else:
            print("Not eligible for getting married")

    def percentage():
        print("Enter the 10th marks to calculate your percentage")

        Subject1 = int(input("Subject1: "))
        Subject2 = int(input("Subject2: "))
        Subject3 = int(input("Subject3: "))
        Subject4 = int(input("Subject4: "))
        Subject5 = int(input("Subject5: "))

        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        percentage = Total / 5

        print("Your total mark is:", Total)
        print("Your percentage is:", percentage)
    