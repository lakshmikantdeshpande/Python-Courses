def fib(n):
    # put your code here
    if n is 0:
        return 0
    elif n is 1:
        return 1
    else:
        a = 0
        b = 1

        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
