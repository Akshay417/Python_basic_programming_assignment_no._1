#!/usr/bin/env python
# coding: utf-8
Q1. What are the two values of boolean data type ? How do you write them ?

Ans: Two values of boolean data type that is : True and false, True is denoted by 1 and False is denoted by 0.Q2. what are the three different types of boolean operators?

Ans: Three types of boolean operators: AND operator, OR operator, NOT operator.Q3. Make a list of each boolean operators truth's table.(i.e. every possible combination of boolean values for the operators and what it evaluate ?  

Ans: Boolean Operators are : [AND, OR, NOT, NOT-OR, NOT-AND] [boolean value:(True:1, False:0)]
  1.(AND Operator):   Result                     
    True AND False  = False
    True AND True   = True
    False AND False = False
    False AND True  = False
    
  2.(OR Operator):   Result
    True OR False  = True
    True OR True   = True
    False OR False = False
    False OR True  = True
    
  3.(NOT Operator):   Result
    NOT False       = True
    NOT True        = False
    
  4.(NOT-OR Operator):    Result
    NOT(True OR False)  = False
    NOT(True OR True)   = False
    NOT(False OR False) = True
    NOT(False OR True)  = False
    
  5.(NOT-AND Operator):    Result                     
    NOT(True AND False)  = True
    NOT(True AND True)   = False
    NOT(False AND False) = True
    NOT(False AND True)  = True
    Q4. What are the values of following expressions ?
   1. (5 > 4) and (3 == 5)
   2. not (5 > 4)
   3. (5 > 4) or (3 == 5)
   4. not ((5 > 4) or (3 == 5))
   5. (True and True) and (True == False)
   6. (not False) or (not True)
   
Ans: 1. False (0)
     2. False (0)
     3. True  (1)
     4. False (0)
     5. False (0)
     6. True  (1)Q5. What are six comparison operators ?

Ans: six comparison operators:
     1. Greater than >
     2. Less than <
     3. Greather than equal to  >=
     4. Less than equal to <=
     5. Equal to ==
     6. Not equal to !=Q6. How do you tell the difference between the equal to and assignment operators ? Describe a condition and when you would be use ? 

Ans:  '='  this is a symbol of assignment operator. And it is use for assign the value in the                variable.
          eg. ( a=10) this means that 10 value is assign in the variable 'a'.
       
     '==' this is a symbol of equal to. this symbol is use for the comparison and to show relation            between two values.
          eg. (a==b) this means that 'a' and 'b' both are equal.
      
      
      Q7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Ans: three blocks are indentations. above code should be as like bellow;
     spam = 0
     if spam == 10:
         print('eggs')
     if spam > 5:
         print('bacon')
     else:
         print('ham')
         print('spam')
         print('spam')

    
# In[5]:


spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')

Q8. write a code that print Hallo if one is stored in spam, Print Howdy if 2 is stored in spam, and print Greetings!if anything else stored in spam.

Ans: spam == int(input("The value is: "))
     if spam == 1:
         print ("Hello")
     elif spam == 2:
             print ("Howdy")
     else:
         print("Greeting!")
        
# In[36]:


spam = int(input("The value is : "))
if spam == 1:
    print ("Hello")
elif spam == 2:
        print ("Howdy")
else:
    print("Greetings!")


# In[37]:


spam = int(input("The value is : "))
if spam == 1:
    print ("Hello")
elif spam == 2:
        print ("Howdy")
else:
    print("Greetings!")


# In[38]:


spam = int(input("The value is : "))
if spam == 1:
    print ("Hello")
elif spam == 2:
        print ("Howdy")
else:
    print("Greetings!")

Q9. if your programme is stuck in endless loop,what keys you will press?

Ans:i will press ctrl+Z or ctrl+C.
Q10. how can you tell the difference between break and continue ?

Ans: break statment is use to immidiate ternination of the loop. and continue statment is use for the terminate current iteration and resume the control to next iteration of the loop.  Q11. In for loop, what is the difference between range(10), range(0,10), range(0,10,1)?

Ans: There is no difference between all above three conditions. All are same.Q12. write a short program that print the number between 1 to 10 using for loop.Then write a equivalent program  that prints the number between 1 to 10 using while loop.
Ans:
# In[51]:


for i in range (1,11):
    print(i, end =" ")
print()


# In[54]:


i = 1
while (i<=10):
    print(i, end = " ")
    i += 1

Q13. If you have the function name bacon() inside the module name spam, how would you call it after importing spam ?

Ans: i would be call it as spam.bacon() Thank You..!