#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Q1. Write a  python program to find LCM ?

def GCD(a,b):
    if b==0:
        return a;
    else:
        return GCD(b,a%b)
a = int(input("enter the value of n1 : "))
b = int(input("enter the value of n2 : "))
gcd = GCD (a, b)
print("\n GCD of {0} and {1} = {2}".format(a,b,gcd))

LCM = a * b /gcd
print("\n LCM of {0} and {1} = {2}".format(a,b,LCM))


# In[6]:


# Q2. program to find HCF:-

def HCF(a,b):
    if b==0:
        return a;
    else:
        return HCF(b,a%b)
a = int(input("enter the value of n1 : "))
b = int(input("enter the value of n2 : "))
hcf = HCF (a, b)
print("\n HCF of {0} and {1} = {2}".format(a,b,hcf))


# In[8]:


#Q3. write a program to covert deciaml to bianry, octal and hexadecimal?

#for this we have to use in build function bin(), oct(),hex().

decimal = int(input("Enter the decimal number : "))
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print(decimal, "Decimal = ",  binary, " Binary value")
print(decimal, "Decimal = " , octal , " Octal value")
print(decimal, "Decimal = "  ,hexadecimal, " Hexadecimal value")


# In[12]:


#Q4. Write a Python Program To Find ASCII value of a character?

# In this code we have to use ord() and chr() in build function to convert to an integer(ASCII value)

i = "b"
print("The ASCII value of 'i' is", ord (i))
print((chr(65),chr(66),chr(67)), end = " ")


# In[7]:


# Q5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b
    
print("SELECT OPERATION. ")
print("1. Add ")
print("2. Subtract ")
print("3. Multiply ")
print("4. Divide ")

while True:
    
    select = input("SELECT (1/2/3/4): ")
    
    if select in ('1','2','3','4'):
        n1 = float(input("Enter the first number : "))
        n2 = float(input("Enter the second number : "))
        
        if select == '1':
            print(n1,"+",n2, "=", add(n1,n2))
        elif select == '2':
            print(n1,"-",n2, "=", subtract(n1,n2))
        elif select == '3':
            print(n1,"*",n2, "=", multiply(n1,n2))
        elif select == '4':
            print(n1,"/",n2, "=", divide(n1,n2))
        break
    else:
        print("Input Invalid")
        
        

Thank you...!