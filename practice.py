#Write a program to check whether a number is even or odd.

# n= int(input("enter the number "))
# if n%2==0:
#     print("even")
# else:
#     print("odd")


#Find the largest of two numbers.
# n1= int(input("enter the first number "))
# n2= int(input("enter the second number "))
# if n1>n2:
#     print(n1 is greater)
# else :
#     print("n2 is largest")


#Check Positive, Negative or Zero
# n= int(input("enter the number "))
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")


#Print Numbers 1 to 10
# n=1
# while n<=10:
#     print(n)
#     n+=1


#Sum of First N Numbers
# n= int(input("enter the number "))
# i=1
# total=0
# while i<=n:
#     total+=i
#     i+=1
# print("sum",total)



# Reverse a Number
# n = int(input("Enter number: "))
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print("Reverse =", rev)

# a=10
# b=5
# print(a>b)

# a=7
# b=7
# print(a==b)

# a=8
# b=10
# print(a<b)



# a=15
# b=20
# c=15
# print(a>b,a==c)

# a=15
# b=10
# print((a>b)>(a*b))


# n=int(input("enter the value "))
# if n%2==0:
#     print("is even ")
# else:
#     print("is odd")

# n=int(input("enter the number"))
# if n%2==0:
#     print("is divide by 2")
# else:
#     print("not divided by 23")

# n=int(input("enter the value"))
# if n%2==0 and n%3==0:
#     print("is divisible by 2 and 3")
# else:
#     print("is not divisible by 2 and 3")

# n=int(input("enter the value"))
# if n%2!=0 and n>50: 
#     print("given number is odd")
# else:
#     print("given number is not odd")


# n=int(input("enter the value"))
# if n%2==0 and n>10 and n<50: 
#     print("given number is even ")
# else:
#     print("given number is not even ")



# age =int(input("enter the age"))
# if age >=18:
#     print("eligibal for votting ")
# elif age <18 :
#     print("not eligible for votting")

# n=1
# while n<=10: 
#     print(n)
#     n=n+1

# num =5
# i=1
# while i<=10:
#     print(num*i)
#     i=i+1

# n = 1
# while n < 100:
#     if n % 2==0:
#         print(n)
#     n=n+1

# n=1346
# sum=0
# while n>0:
#     r=n%10
#     sum =sum+r
#     n=n//10
# print(sum)


# n= int (input("enter the number"))
# rev=0
# m=n
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if rev==m:
#     print("palindrome")
# else:
#     print("not a palindrome")

# for i in range (1,4):
#     for j in range (1,4):
#         print(i,',',j)

# for i in range (1,101):
#     print(i)

# for num in range(1, 101):
#     count = 0
    
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1
    
#     if count == 2:
#         print(num)
     


# for i in range (1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print("")


# for i in range (1,6):
#     for j in range(1,6):
#         print("?",end=" ")
#     print("")



# for i in range (1,6):
#     for j in range(1,6):
#         if i>=j:
#             print("*",end=" ")
#     print("")


# for i in range (1,6):
#     for j in range(1,6):
#         if i<=j:
#             print("*",end=" ")
#     print("")


# for i in range(1, 6):
#     for j in range(1, 6):
#         if j >= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")

# n=10
# for i in range(n):
#     for j in range(n):
#         if i+j==n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")


# n=10
# for i in range(n):
#     for j in range(n):
#         if (j==0 or j==n-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")


# n = 11
# for i in range(n):
#     for j in range(n):
#         if i== n // 2 or j == n // 2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")


# n = 10
# for i in range(n):
#     for j in range(n):
#         if i== j or i+j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")


# n = 11
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")


# n = 11
# for i in range(n):
#     for j in range(n):
#         if i==n-1 or j==0 or i==j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")

# n = 11
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i+j==n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")


n = 11

for i in range(n):
    for j in range(2*n - 1):
        if j == n-1-i or j == n-1+i or i == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")