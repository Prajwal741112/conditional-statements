# s1 ='software'
# s2='hardware'
# print(s1<s2)

# s1 ='Manu '
# s2='sanju'
# print(s1<s2)

#is and is not 
# a="hello"
# b="hello"
# print(a is b)


# n=5
# while n>0:
#     print(n)
#     n=n-1

# n=3
# i=0
# while i<10:
#     i=i+1
#     print(n*i)
#     print(n,'X',i,'=',n*i)


# n=4365
# while n>0:
#     r=n%10
#     print(r)
#     n=n//10

# n = int(input("Enter the number: "))
# sum= 0

# while n > 0:
#     r = n % 10
#     sum = sum + r
#     n = n // 10

# print("Sum of digits =", sum)

# n = int(input("Enter the number: "))
# rev= 0

# while n > 0:
#     r = n % 10
#     rev=rev*10+r
#     n = n // 10

# print("rev of digits =", rev)

# n=int(input("Enter the number"))
# rev =0
# m=n
# while n>0:
#     r=n%10
#     rev =rev *10+r
#     n=n//10
# if rev==m:
#     print("palindrom")
# else:
#     print("not a palindrome")


# n=5
# i=0
# sum=0
# while i<n:
#  i=i+1
#  sum+=i
#  print(sum)


# n = 5
# print("Enter the", n, "numbers")

# i = 0
# max_val = 0   # don't use 'max'

# while i < n:
#     i = i + 1
#     x = int(input())
    
#     if x > max_val:
#         max_val = x

# print("Maximum number is:", max_val)

n = 5
print("Enter the", n, "numbers")

i = 1
x = int(input())      # take first number
max_val = x
min_val = x

while i < n:
    x = int(input())
    
    if x > max_val:
        max_val = x
        
    if x < min_val:
        min_val = x
        
    i = i + 1

print("Maximum number is:", max_val)
print("Minimum number is:", min_val)