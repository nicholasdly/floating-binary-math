
def from_fractional_binary(s):
    
    n = 0
    p = s.find(".") - 1

    for d in s:
        if d == ".":
            continue
        n += int(d) * (2**p)
        p -= 1

    return n

def main():
    
    while True:
        x = input("Enter a fractional binary value: ")
        if x == "Q" or x == "q":
            break
        print(from_fractional_binary(x))

if __name__ == "__main__":
    main()
