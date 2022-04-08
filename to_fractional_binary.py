
BIT_PRECISION = 8

def to_fractional_binary(s):

    n = float(s)
    b = ""
    p = BIT_PRECISION

    while p >= -BIT_PRECISION:
        if p == -1:
            b += "."
        if (n - 2**p) >= 0:
            b += "1"
            n -= 2**p
        else:
            b += "0"
        p -= 1

    while b[0] == "0":
        b = b[1:]

    return b

def main():

    while True:
        x = input("Enter a floating point value: ")
        if x == "Q" or x == "q":
            break
        print(to_fractional_binary(x))

if __name__ == "__main__":
    main()
