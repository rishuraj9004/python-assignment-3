import math

def operations():
    while True:
        try:
            a = float(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a valid number (not letters)")
    sqrt = math.sqrt(a)
    log = math.log(a)
    sin = math.sin(a)

    print(f"\nResults for {a}\n Square Root: {sqrt}\n Logarithm: {log}\n Sin: {sin}")


operations()