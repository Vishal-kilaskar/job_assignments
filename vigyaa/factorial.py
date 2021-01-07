"""
The factorial of the integer n, written n!, is defined as:
    n! = n*(n-1)*(n-2)*....*3*2*1
calculate and print the factorial of the given integer.

"""
"""
solution to this is,
step 1) we have to multiply the number in the N*(N-1)*(N-2)...so on till 1
we can do it in recursive as well as iterative method.
"""


# using recursive method

def fact(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fact(number - 1)


print(fact(3))