'''Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
contains the word ‘twinkleʼ.'''

f = open("problem.txt")
content = f.read()

if("twinkle" in content):
    print("the word twinkle is present in the content")

else:
    print("the word twinkle is not present in the content")


f.close()    