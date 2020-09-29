def nums():
    firstNum=input("Enter 1st Number:")
    secondNum=input("Enter 2nd Number:")
    try:
        firstNum=int(firstNum)
        secondNum=int(secondNum)
        if firstNum<secondNum:
            lb=firstNum
            ub=secondNum
        else:
            lb=secondNum
            ub=firstNum
        sum=0
        for i in range(lb,ub+1,1):
            sum+=i
        print(sum)
    except:
        print("ERROR!")
        print("RESTART PROGRAM")
    state=input("Continue? Y/N:")
    if state=="Y":
        nums()
    elif state=="N":
        print("Done")
nums()
