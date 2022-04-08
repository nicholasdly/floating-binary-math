
def from_fractional_binary(s):
    
    num = 0
    exp = s.find(".") - 1

    # For every character/digit of the inputted binary float value, sum all
    # powers of two to find the decimal value.
    for c in s:
        if c == ".":
            continue
        num += int(c) * (2**exp)
        exp -= 1

    return num

def main():

    while True:
        x = input("Enter a fractional binary value: ")
        if x == "Q" or x == "q":
            break
        print(from_fractional_binary(x))

if __name__ == "__main__":
    main()
