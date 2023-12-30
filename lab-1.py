"""
#1
a=int(input('Enter a integer : '))
b=int(input('Enter a integer : '))
d=a+~b+1
print(d)
"""

"""
# 2
Num =int(input('Enter a integer: '))
sum=0

temp = Num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if Num == sum:
   print(Num,"is an Armstrong number")
else:
   print(Num,"is not an Armstrong number")
"""
num1=int(input('enter a number : '))
num2=int(input('enter a number : '))
num3=int(input('enter a number : '))
def find_product(num1,num2,num3):
    product=0
    if (num1 != 7 and num2 != 7 and num3 != 7):
        product = num1 * num2 * num3
    elif (num1 == 7):
        product = num2 * num3
    elif(num2 == 7):
        product = num3
    elif(num3 == 7):
        product = -1
    return product

product=find_product(num1,num2,num3)
print(product)