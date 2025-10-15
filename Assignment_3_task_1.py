# Task 1: Calculate Factorial Using a Function

n = int(input("Enter a number : "))

def cal_fact(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print(f"Factorial of {n} is :", fact)


cal_fact(n)

