def palindrome():
    word=input("Enter Word:")
    forward=list()
    for letters in word:
        forward.append(letters)

    forward.reverse()
    backward="".join(forward)
    if backward==word:
        print(True)
    else:
        print(False)
    state=input("Continue? Y/N:")
    if state=="Y":
        palindrome()
    elif state=="N":
        print("Done")
palindrome()