def factorial(number):
    val = 1
    for i in range(1, number + 1):
        val *= i
    return val

print(f'Factorial : {factorial(10)}')
