def greeting():
    print("Hello!")

greeting()


# Return Function
def greeting2(name):
    print("Hello," + name)

guestname = input("What is your name?: ")
greeting2(guestname)

####################################

#def addNumbers(num1, num2):
   #return (num1 + num2)

#print(addNumbers(12, 34))
#sum = addNumbers(12, 34)
#print(sum)

####################################

# Challenge create 2 functions that take in 2 numbers from the user

# 1 function will be to find the difference between 2 numbers, and the other will find the product.

#step 1: use input to ask user for numbers
#step 2: convert numbers into intergers
#int(num1)
#step 3: create the functions
#step 4: print the return values of both functions
####################################

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

def difference(n1, n2):
    diff = n1 - n2
    print(f"The difference between these two numbers is: {diff}")

def product(n1, n2):
    prod = n1 * n2
    return prod

difference(num1, num2)

productNum = product(num1, num2)
print(f" The product of these two numbrrs is: {productNum}")



def subNumbers( num1, num2):
    return (num1 - num2)

print(subNumbers(51,19))


def divNumbers( num1, num2):
    return (num1 % num2)

print(divNumbers(7,6))
