#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    counter = len(sys.argv)
    if counter != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(args[1])
    b = int(args[3])
    opera = args[2]

    if opera == "+":
        resultat = add(a, b)
    elif opera == "-":
        resultat = sub(a, b)
    elif opera == "*":
        resultat = mul(a, b)
    elif opera == "/":
        resultat = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, opera, b, resultat))
