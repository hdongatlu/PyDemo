from sympy import symbols, diff, sqrt

# Define symbolic variable and function
x = symbols('x')
f = sqrt(x**2 + 5)

# a) Determine f'(x)
f_prime = diff(f, x)

# b) Compute f'(2)
f_prime_at_2 = f_prime.subs(x, 2)

# Define the function for numerical evaluation
def f_num(x):
    return sqrt(x**2 + 5)

# c) Use the Central Difference Rule to approximate f'(2) for h=0.1
h = 0.1
f_prime_approx = (f_num(2 + h) - f_num(2 - h)) / (2 * h)

# d) Evaluate the absolute error
absolute_error = abs(f_prime_at_2 - f_prime_approx)

f_prime, f_prime_at_2, f_prime_approx, absolute_error
