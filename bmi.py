choice='y'
while(choice=='y'):
    weight=float(input("Enter your age in kgs...:"))
    height=float(input("Enter your height in cms...:"))
    bmi=weight/(height*height)*10000
    if(bmi<=18.4):
        print("You are underweight!!!")
    elif(bmi>18.4 and bmi<25):
        print("You have a normal weight!!!")
    elif(bmi>24.9 and bmi<40):
        print("You are overweight!!!")
    elif(bmi>=40):
        print("You are obese!!!")
    else:
        print("Invalid Input!!!")
    choice=input("Do you want to continue:(y/n)...:")
    if(choice=='y'):
        continue
    else:
        break