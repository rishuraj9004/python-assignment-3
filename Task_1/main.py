def factorial(n):
    if n < 0:
        print('Factorial of negative number is not defined')
        main()
    if n != 0 and n != 1:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    else:
        return 1
def main():
    while True:
        try:
            a = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a valid positive number (not letters or decimals or negetive numbers)")
    print(f"The factorial of {a} is {factorial(a)}")
main()