import string

str=input("Enter string:")
count1=0
count2=0
count3=0

for i in str:
    if i in string.ascii_letters:
        count1=count1+1
    if i in string.digits:
        count2=count2+1
    if i in string.punctuation:
        count3=count3+1
        
print("letters:",count1)
print("digits:",count2)
print("punctuations:",count3)