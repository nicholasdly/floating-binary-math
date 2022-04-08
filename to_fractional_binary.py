
# The number of bits the final binary float value will have on both sides of its
# decimal point.
BIT_PRECISION = 8

def to_fractional_binary(s):

    num = float(s)
    bin = ""
    exp = BIT_PRECISION

    # While the specified precision of bits has not been reached, continue to
    # convert the inputted decimal float value into a binary float value.
    while exp >= -BIT_PRECISION:
        if exp == -1:
            bin += "."
        if (num - 2**exp) >= 0:
            bin += "1"
            num -= 2**exp
        else:
            bin += "0"
        exp -= 1

    # Removes leading zeros.
    while bin[0] == "0":
        bin = bin[1:]

    return bin

def main():

    while True:
        x = input("Enter a floating point value: ")
        if x == "Q" or x == "q":
            break
        print(to_fractional_binary(x))

if __name__ == "__main__":
    main()
