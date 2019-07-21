# 1.Estimate your age!
age = int(input("Please enter your age:"))
if 0 <= age <= 120:
    print("value age!")
else:
    print("invalue age!")

# 2.Estimate your scores!
python_score = int(input("Please enter a int variable:"))
c_score = int(input("Please enter another int variale:"))
if python_score > 60 or c_score > 60:
    print("You are eligible!")
else:
    print("Sorry for you!")

