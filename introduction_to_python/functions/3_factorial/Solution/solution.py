# Code your solution here
def fact(n):
    if n == 0:
        data=1
    else:
        data=n * fact(n-1)
    return data 
# added this line to test
n=int(input())
result=fact(n)
print(result)
