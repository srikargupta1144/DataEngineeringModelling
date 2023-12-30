# write a program that accepts a sentence and calculate the number of letters and digits.take a user a input
def letter_digit_count():
    string = input("Enter a sentence of digits and numbers:");
    count = {'letter':0 , 'number':0}
    for letter in string:
        if letter.isalpha():
            count['letter'] += 1
        elif letter.isdigit():
            count['number'] += 1
    print("LETTERS:" + str(count['letter']) + "\nNUMBERS:" + str(count['number']))
