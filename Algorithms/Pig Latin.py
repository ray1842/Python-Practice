import re
def pigLatin():
    word=input("Enter word:")
    lst=list()
    for letter in word:
        lst.append(letter)
    consonants=list()
    i=0
    if bool(re.search("^[aeiou]",word))== True: 
        lst=lst+["w","a","y"]
    else:
        while i<len(lst):
            if bool(re.search("[^aeiou]",word[i]))==True:
                consonants.append(lst[i])    
            else:
                break
            i+=1
        lst=lst[i:]+consonants+["a","y"]
    output="".join(lst)
    print(output)
    state=input("Continue? Y/N:")
    if state=="Y":
        pigLatin()
    elif state=="N":
        print("Done")
pigLatin()
