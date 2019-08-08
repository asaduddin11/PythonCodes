def print_rangoli(size):
    items = size*4 - 3
    print("Range: ", items)
    for i in range(items):
        for j in range(items):
            if j == (items//2):
                print(chr(64+size), end="")
            else:
                print(chr(45), end="")
        print("\n")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)