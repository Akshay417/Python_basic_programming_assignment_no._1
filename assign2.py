#!/usr/bin/env python
# coding: utf-8
PYTHON PROGRAMMING ASSIGNMENT NO.2Q1. Write a python program to convert kilometer into miles ?
# In[2]:


kilometer = float(input("enter the value in kilometer : "))
miles = kilometer * 0.62137119
print("{0} kilometer = {1} miles".format(kilometer, miles))

Q2. Write a python program to convert celsius to fahrenheit ?
# In[14]:


Celsius = float(input("Enter the value in Celsius : "))
Fahrenheit = (Celsius * 1.8) +32
print("{0} Celsius = {1} Fahrenheit".format(Celsius, Fahrenheit))

Q3. Write a python program to display the calendar.
# In[6]:


import calendar
year = 2020
print(calendar.calendar(year))

Q4. Write a python program to solve quadratic equation.
# In[13]:


#for quadratic equation we have to import complex math module.
#formula (-b ± (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
# quadratic equation is ax**2 + b*x + c = 0
#to find the root of quadratic equation we have to calculate discriminant.
# disc = b**2 - 4*a*c

import cmath 
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
dis = b**2 - 4*a*c
x = -b - (cmath.sqrt(dis))/2*a
y = -b + (cmath.sqrt(dis))/2*a
print("The first solution is : {0}".format(x))
print("The second solution is : {0}".format(y))

Q5. Write a python program to swap two variable without using temp variable.
# In[12]:


a = 5
b = 10
print("Before the swaping, the vlaue of a = {0} and vlaue of b = {1}".format(a,b))
a = a + b
b = a - b
a = a - b
print("After the swaping, now the value of a = {0} and vlaue of b = {1}".format(a,b))


# In[ ]:




