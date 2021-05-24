#!/usr/bin/env python
# coding: utf-8
Python_Basic_Programming_Assignment_No.1Q1. Write a Python program to print "Hello Python" ?
# In[4]:


a="Hello python"


# In[5]:


print(a)

Q2. write a python program to do arithimatical operations adding and division ?
# In[16]:


a = 50
b = 50
add = a+b


# In[17]:


print(add)


# In[18]:


a = 40
b = 5
div = a//b


# In[19]:


print(div)

Q3. Write a python program to find area of a triangle ?
Ans: here, to find area of triangle we need to find first perimeter of triangle and semiperimeter of triangle.
perimeter = a+b+c
semiperimeter (s) = a+b+c/2
Area of triangle = s*(s-a)*(s-b)*(s-c)**0.5
# In[25]:


a = float(input("enter the first side of a triangle = "))
b = float(input("enter the second side of a triangle = "))
c = float(input("enter the third side of a trinagle = "))
p = a+b+c
s = a+b+c/2
area = s*(s-a)*(s-b)*(s-c)**0.5
print("\n perimeter of triangle  = %.2f "  %p);
print(" the semi perimeter of triangle = %.2f "  %s);
print(" Area of triangle = %.2f "  %area)

OR
# In[14]:


import math


# In[15]:


def Area_of_Triangle(a,b,c):
    perimeter = a+b+c
    s = a+b+c/2
    area = s*(s-a)*(s-b)*(s-c)**0.5
    print(" the perimeter of a triangle = %.2f" %perimeter);
    print(" the semi perimeter of a triangle = %.2f" %s);
    print(" the area of a triangle = %.2f " %area )
    


# In[16]:


Area_of_Triangle(30,40,50)


# In[17]:


Area_of_Triangle(34,78,90)

Q4. Write a python program to swap two variables ?
# In[9]:


a = float(input("enter the first variable "))
b = float(input("enter the second variable "))
print(" Before swap two numbers : a = {0} and b = {1}".format(a,b))
x = a
a = b
b = x
print("\n After swap two numbers : a ={0} and b = {1}".format(a,b))

Q5. Write a python program to generate random no.?Ans: To generate random no. we have to import random module and use randint() function.
# In[22]:


import random


# In[24]:


print(" Generate random number : ", random.randint(0,20))

Thank you..!