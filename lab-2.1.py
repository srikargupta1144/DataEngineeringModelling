# write a python program that takes a list of words(user input one by one) use space to stop and returns the length of the smallest one(hint: use isspace()) """
list_= []

while True:
    li= input("Enter a list: ")
    if li.isspace():
        break
    list_.append(li)
    sl = len(list[0])
for li in list_:
    if len(li) < sl:
        sl = len(li)
        print("The length of the smallest word is:", sl)