#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
x=int(input())
a=((x%10))%2
A=a*(x%10)
b=((x//10)%10)%2
B=b*(x//10)%10
c=((x//100)%10)%2
C=c*(x//100)%10
d=((x//1000))%2
D=d*(x//1000)
print(A+B+C+D)



