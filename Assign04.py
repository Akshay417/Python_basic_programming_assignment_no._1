#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Q.01 find the factorial of a number:-

def factorial(num):
    Num = 1
    for i in range(1,num+1):
        Num = Num *i
    return Num
num = int(input("enter the value of n : "))
a = factorial(num)
print("the factorial of number {0} is {1}".format(num,a))


# In[6]:


#Q.02 Disply the multiplication of table:-

num1 = int(input("enter the vlaue of num1 : "))
num2 = int(input("enter the value of num2 : "))
for i in range(num1,num2):
    for j in range(1, 11):
        print("{0} * {1} = {2}".format(i,j,i*j))
    print("---------")
        
   


# In[13]:


#Q3. febonacci sequence:-

def fibonacci_series(num):
        if num==0:
            return 0
        elif num ==1:
            return 1
        
        else:
            return(fibonacci_series(num-2) + fibonacci_series(num-1))
num = int(input("enter the number: "))
s = fibonacci_series(num)
print("the fibonacci series of number {0} is : {1} ".format(num,s))


# In[16]:


#Q.04 check amstrong_number:-

def amstrong_number(num):
    sum = 0
    time = 0
    
    s = num
    while s>0:
        time = time+1
        s=s//10
        
    s = num
    for i in range(1,s+1):
        reminder = s%10
        sum = sum + (reminder ** time)
        s = s//10
    return sum
num = int(input("enter the number : "))
if num == amstrong_number(num):
    print("\n {0} is amstrong number".format(num))
else:
    print("\n {0} is not amstrong number".format(num))


# In[23]:


#Q.05 amstrong number in an interval:-

x=int(input("lower limit: "))
y=int(input("upper limit: "))
print("Armstrong Numbers are: ")
for Number in range(x,y):
    digits=0
    temp=Number
    
    while temp>0: 
        digits=digits+1
        temp=temp//10
        sum=0
    
    temp=Number
    while temp>0: 
        last_digit=temp%10
        sum=sum+(last_digit**digits)
        temp=temp//10
    
    if Number == sum:
        print(Number)



# In[3]:


#Q.06 find the sum of natural number:-

def Natural_number(num):
    if num == 0:
        return num
    else:
        return(num + Natural_number(num-1))
num = int(input("enter the value of n : "))
s = Natural_number(num)
print("the sum of natural number {0} is {1}".format(num,s))

Thank You......