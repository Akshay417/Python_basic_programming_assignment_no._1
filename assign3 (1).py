#!/usr/bin/env python
# coding: utf-8
Assignment No.3Q1. Write a python program to check if a number is positive,negative or zero ?
# In[4]:


number = int(input("Enter the value : "))
if number>0:
    print("The given number {0} is positive number".format(number))
elif number<0:
    print("The given number{0} is negative number".format(number))
else:
    print("Given number is Zero")

Q2. Write a python program to check if a number is odd or even?
# In[10]:


number = int(input("Enter the value :"))
if number%2==0:
    print("Given number {0} is a even number".format(number))
elif number%2!=0:
    print("Given number {0} is a odd number".format(number))

Q3. Write a python program to check leap Year?
# In[17]:


a = int(input("Year : "))
if a%4==0:
    print("The Year {0} is a leap Year".format(a))
elif a%100==0:
    print("The Year {0} is a leap Year".format(a))
elif a%400==0:
    print("The Year {0} is a leap Year".format(a))
else:
    print("The Year {0} is not a leap Year".format(a))
    

Q4. Write a python program to check prime number.
# In[11]:


number =int(input("Number : "))
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print(number,"is not a prime number")
            break
    else:
            print(number," is a prime number")
else:
    print("The input number is not a prime number")
            
            

Q5. write a python program to print all prime number in an interval of 1-10000?
# In[30]:


starting_number = int(input("Starting_number : "))
last_number     = int(input("Last_number     : "))
for i in range(starting_number,last_number + 1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i, end = " ")
               

thank you..!