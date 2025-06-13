def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()


def pattern3(n):
    for i in range(n):
        for j in range(1, i+2):
            print(j, end="")
        print()


def pattern4(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end="")
        print()


def pattern5(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        print()


def pattern6(n):
    for i in range(n):
        for j in range(1, (n+1)-i):
            print(j, end="")
        print()


def pattern7(n):
    for i in range(n):
        # space
        for j in range(n-i-1):
            print(" ", end="")
        
        # star
        for j in range(2*i+1):
            print("*", end="")

        # space
        for j in range(n-i-1):
            print(" ", end="")
        print()


def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(2*n-(2*i+1)):
            print("*", end="")
        for j in range(i):
            print(" ", end="")
        print()


def pattern9(n):
    pattern7(n)
    pattern8(n)


def pattern10(n):
    for i in range(n*2-1):
        stars = i
        if stars > n:
            stars = 2*n - i
        for j in range(stars):
            print("*", end="")
        print()


def pattern11(n):
    start = 1
    for i in range(n):
        if (i % 2 == 0):
            start = 1
        else:
            start = 0
        for j in range(i+1):
            print(start, end="")
            start = 1 - start
        print()


def pattern12(n):
    space = 2 * (n-1)
    for i in range(1, n+1):
        # numbers
        for j in range(1, i+1):
            print(j, end="")

        # space
        for j in range(space):
            print(" ", end="")

        # numbers
        for j in range(i, 0, -1):
            print(j, end="")

        print()
        space = space - 2


def pattern13(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end=" ")
            num = num + 1
        print()


def pattern14(n):
    for i in range(n):
        for j in range(ord('A'), ord('A') + i + 1):
            print(chr(j), end=" ")
        print()


def pattern15(n):
    for i in range(n):
        for j in range(ord('A'), ord('A') + (n - i)):
            print(chr(j), end=" ")
        print()


def pattern16(n):
    for i in range(n):
        num = ord('A') + i
        char = chr(num)

        for j in range(i+1):
            print(char, end=" ")
        
        print()


def pattern17(n):
    for i in range(n):
        # space
        for j in range(n - i - 1):
            print(" ", end="")
        
        # char
        int = ord('A')
        breakpoint = (2*i+1) / 2
        for j in range(1, 2 * i + 2):
            char = chr(int)
            print(char, end="")
            if j <= breakpoint:
                int += 1
            else:
                int -= 1

        # space
        for j in range(n - i - 1):
            print(" ", end="")
        print()


def pattern18(n):
    for i in range(n):
        start_char = ord('A') + n - i - 1
        for j in range(i + 1):
            char = chr(start_char + j)
            print(char, end=" ")
        print()


def pattern19(n):
    int_space = 0
    for i in range(n):
        # star
        for j in range(n - i):
            print('*', end='')
        # space
        for j in range(int_space):
            print(' ', end='')
        # star
        for j in range(n - i):
            print('*', end='')
        int_space += 2
        print()
    int_space = (n*2) - 2
    for i in range(n):
        # star
        for j in range(i+1):
            print('*', end='')
        # space
        for j in range(int_space):
            print(' ', end='')
        # star
        for j in range(i+1):
            print('*', end='')
        int_space -= 2
        print()




pattern19(5)
