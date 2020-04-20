#!/usr/bin/env python
# coding: utf-8

# 1. Write a program to Add, Subtract, Multiply, and Divide 2 numbers

# In[10]:


x=int(input('Write 1st Input:'))
y=int(input('Write 2nd Input:'))
print('Sum :',x+y)
print('Multiple :',(x*y))
if x>y:
    print('Division: ',x/y)
else:
    print('Division: ',y/x)


# 2. Write a program to find the biggest of 3 numbers 

# In[17]:


x=int(input('Write 1st Input:'))
y=int(input('Write 2nd Input:'))
z=int(input('Write 3rd Input:'))
if x>=y and x>=z:
    print(x ,'is the biggest of 3 number')
elif y>=x  and y>=z:
    print(y,'is the biggest of 3 number')
else:
    print(z,'is the biggest of 3 number')


# 3. Write a program to find given number is odd or Even

# In[18]:


x=int(input('Write 1st Input:'))
if x%2==0:
    print(x,'is Even number')
else:
    print(x,'is odd number')


# 4.Write a program to find the number is Prime or not.

# In[31]:


x=int(input('Write the number to find if it is Prime or not'))
if x > 1:
   for i in range(2,x):
    if (x % i) == 0:
        print(x,"is not a prime number")
        print(i,"times",x//i,"is",x)
        break
    else:
        print(x,"is a prime number")
        break
else:
    print(x,"is not a prime number")


# 5. Write a program to receive 5 command line arguments and print each argument separately.
# 
# Example: >> python test.py arg1 arg2 arg3 arg4 arg5
# 
# a) From the above statement your program should receive arguments and print them each of them.
# 
# b) Find the biggest of three numbers, where three numbers are passed as command line arguments.
# 

# In[19]:


#please copy the code and create a file.py then pass the argument in cmd as i'm using jupyter it won't show result in here

import sys 

n = len(sys.argv)
z=[]
print("Total arguments passed:", n) 

print("\nName of Python script:", sys.argv[0]) 

print("\nArguments passed:") 
for i in range(1, n): 
    print(sys.argv[i])
    z.append(sys.argv[i])
print('Maxiumum Number of the arg passed ' ,max(z))	


# 6. Write a program to read string and print each character separately.
# 
# a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
# 
# b) Repeat the string 100 times using repeat operator *
# 
# c) Read string 2 and concatenate with other string using + operator.
# 

# In[3]:


x=str(input('Write the input in string'))
print(x[:])
print(x[:].split())
print(x*100)
y=str(input('Write the second string'))
print(x+y)


# 7.Create a list with at least 10 elements having integer values in it
# 
# a) Print all elements
# 
# b) Perform slicing operations
# 
# c) Perform repetition with * operator
# 
# d) Perform concatenation with other list.
# 

# In[17]:


import numpy
x=numpy.arange(1,11)
print(x)
print(x[1:4])
print(x*2)
y=numpy.arange(12,22)
print(y)
print(x+y)


# 8.Repeat program 7 with Tuples (Take example from Tutorial)

# In[20]:



b=(10,20,30,40,50) #taken from example shown in tutorial
print(b)
print(b[1:4])
print(b*2)
c=(11,22,33,44,55)
print(b+c)


# 9.Write program to Add, Subtract, Multiply, Divide 2 Complex numbers.

# In[22]:


x=complex(input('Write 1st Complex number:'))
y=complex(input('Write 2nd complex number:'))
print('Sum :',x+y)
print('Multiple :',(x*y))
print('Division: ',x/y)


# 10.Using assignment operators, perform following operations
# 
# Addition, Substation, Multiplication, Division, Modulus, Exponent and Floor division operations
# 

# In[23]:


x=int(input('Write 1st Input:'))
y=1
y+=x
print('Adding using assignement operator:',y)
y-=x
print('Substation using assignement operator:',y)
y*=x
print('Multiplication using assignement operator:',y)
y/=x
print('Division using assignement operator:',y)
y%=x
print('Modulus using assignement operator:',y)
y**=x
print('Exponent using assignement operator:',y)
y//=x
print('Floor division using assignement operator:',y)


# 11.Read 2 numbers to variable a and b and perform all bitwise operations on that numbers.

# In[27]:


x=int(input('Write 1st Input:'))
y=int(input('Write 2 st Input:'))
print('Bitwise AND operator:',x&y)
print('Bitwise OR operator:',x|y)
print('Bitwise NOT operator:',~y)
print('Bitwise XOR operator:',x^y)
print('Bitwise Right Shift operator:',x>>y)
print('Bitwise Left Shift operator:',x<<y)


# 12.Read 10 numbers from user and find the average of all.
# 
# a) Use comparison operator to check how many numbers are less than average and print them
# 
# b) Check how many numbers are more than average.
# 
# c) How many are equal to average
# 

# In[4]:


a=[]
t,avg=0,0
for i in range(1,11):
    a.insert(i-1,int(input("Enter numbers \n")))
    t+=a[i-1]
avg=t/len(a)
print("less than average")
for i in a:
    if i<avg:
        print(i)
print("greater than average")
for i in a:
    if i>avg:
        print(i)
print("equal to average")
for i in a:
    if i==avg:
        print(i)


# 13.Write a program to find the biggest of 4 numbers.
# 
# a) Read 4 numbers from user using Input statement.
# 
# b) extend the above program to find the biggest of 5 numbers.
# 
# (PS: Use IF and IF & Else, If and ELIf, and Nested IF)
# 

# In[9]:


a = int(input("Enter number1:"))
b = int(input("Enter number2:"))
c = int(input("Enter number3:"))
d = int(input("Enter number4:"))
e = int(input("Enter number5:"))
if a > b and a > c and a > d and a > e:
    print("Max is :", a)
elif b > a and b > c and b > d and b > e:
    print("Max is :", b)
elif c > a and c > b and c > d and c > e:
    print("Max is :", c)
elif d > a and d > b and d > c and d > e:
    print("Max is :", d)
else:
    print ("Max is:", e)


# 14.Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list & perform following operation
# 
# a) Print all names on to screen
# 
# b) Read the index from the  user and print the corresponding name from both list.
# 
# c) Print the names from 4th position to 9th position
# 
# d) Print all names from 3rd position till end of the list
# 
# e) Repeat list elements by specified number of times (N- times, where N is entered by user)
# 
# f)  Concatenate two lists and print the output.
# 
# g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )
# 

# In[11]:


A = ['01','02','03','04','05','06','07','08','09','10']
B = ["vikash", "akash", "rahul", "gourav", "sudi", "praveen", "sudhanshu", "shivam", "nidhi", "shital"]


print(B)


i = int(input("Enter the index:"))
print(A[i], B[i])


print(B[4:9])


print(B[3:])


N = int(input("Enter number of times you wanna print list:"))
for i in range(0,N):
    print(A)


C = A + B
print(C)


D = []
for x in range(0,len(A)):
    D.append(A[x])
    D.append(B[x])
print(D)


# 15.Create a list of 5 names and check given name exist in the List.
# 
# a) Use membership operator (IN) to check the presence of an element.
# 
# b) Perform above task without using membership operator.
# 
# c) Print the elements of the list in reverse direction.
# 

# In[12]:


B = ["vikash", "akash", "rahul", "gourav", "sudi"]

for i in B:
    if i in B:
        print(i," is present in the list")

for i in B:
    for j in B:
        if j==i:
            print(j," is present in the list")
B.reverse()
print(B)


# 16.Write program to perform following:
#     
# i) Check whether given number is prime or not.
# 
# ii) Generate all the prime numbers between 1 to N where N is given number.
# 

# In[15]:


x=int(input('Write the number to find if it is Prime or not'))
if x > 1:
   for i in range(2,x):
    if (x % i) == 0:
        print(x,"is not a prime number")
        print(i,"times",x//i,"is",x)
        break
    else:
        print(x,"is a prime number")
        break
else:
    print(x,"is not a prime number")

    
for i in range(1,x+1):
    if i > 1: 
       for n in range(2, i): 
           if (i % n) == 0: 
               break
       else: 
           print(i)


# 17.Write program to find the biggest and Smallest of N numbers.
# 
# PS: Use the functions to find biggest and smallest numbers. 
# 

# In[18]:


x=int(input('Enter the number to create list from 1 to N:'))
N=list(range(1,x+1))
print(N)
print('Min of the number:',min(N))
print('Max of the number:',max(N))


# 18.Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)
# 
# a) By using For loop
# 
# b) By using while loop
# 
# c) Let mystring ="Hello world"
# 
# print each character of mystring in to separate line using appropriate loop structure.
# 

# In[21]:


x=0
for x in range(1,101):
    print(x)
    
x=0
for x in range(100):
    print(100-x)
    
x=1
while(x<=100):
    print(x)
    x += 1
    
x=0
while(x<100):
    print(100-x)
    x += 1
    
mystring ="Hello world"
for i in mystring:
    print(i)


# 19.Using loop structures print even numbers between 1 to 100.
# 
# a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
#     
#     i) Break the loop if the value is 50
#     
#     ii) Use continue for the values 10,20,30,40,50
#     
# b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
#       
#       i) Break the loop if the value is 90
#       
#       ii) Use continue for the values 60,70,80,90
# 

# In[ ]:


x=int(input('Enter number till where you wanna find even number:'))
y=[10,20,30,40,50]
z=[60,70,80,90]

for i in range(x):
    if(i%2==0):
        print(i)

i=0
for i in range(x+1):
    if(i%2!=0):
        continue

    if(i==50):
        break

    if i in y:
        continue

i=0
while(i<=x):
    if(i%2!=0):
        continue

    if(i==90):
        break

    if i in z:
        continue

    i += 1
    


# 20.Write a program to generate a Fibonacci series of numbers.
# 
# Starting numbers are 0 and 1,  new number in the series is generated by adding previous two numbers in the series.
# 
# Example : 0, 1, 1, 2, 3, 5, 8,13,21,.....
# 
#    a) Number of elements printed in the series should be N numbers, Where N is any +ve integer.
#    
#    b) Generate the series until the element in the series is less than Max number.
# 

# In[1]:


a=0
b=1
x=int(input("Input for number needed: "))

L = [a,b]

while(x-2):
    c=a+b
    a=b
    b=c
    L.append(c)
    x=x-1


for i in L:
    print(i)

y=int(input("Enter the number until series is printed: "))
a=0
b=1

L = [a,b]

while(y-2):
    c=a+b
    if(c>y):
        break
    a=b
    b=c
    L.append(c)
    y=y-1

for i in L:
    print(i)


# In[ ]:




