import random

print("salam")
#put mark between items
def beetwixt(a , b ,c) :
    markList = ["!", "@", "#", "$", "%", "&", "*", "-", "_"]
    result = a + random.choice(markList) + b + random.choice(markList) + c
    if(len(result) < 8):
        result += str(random.randint(1950,2100))
    return result

#getting target information
firstName = input("Enter your target first name: ")
lastName = input("Enter your target last name: ")
birthDate = input("Enter your target birthDate name: ")

#make random list
randomList = [firstName, lastName, birthDate]
for i in range(100):
    firstItem = random.choice(randomList)
    secondItem = random.choice(randomList)   
    if(firstItem == secondItem):
        secondItem = ""
    thirdItem = random.choice(randomList)
    if(firstItem == thirdItem or secondItem == thirdItem):
        thirdItem = ""
    
    print(beetwixt(firstItem, secondItem , thirdItem))
