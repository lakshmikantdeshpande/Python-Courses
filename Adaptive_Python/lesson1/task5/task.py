# put your python code here
if __name__ == "__main__":
    n = int(input())
    numbers = list()
    for i in range(n):
        numbers.append(tuple(map(int, input().split())))
    numbers.sort(key=lambda x: round((x[0] ** (2) + x[1] ** (2)) ** (1.2)))
    for number in numbers:
        print("{0} {1}".format(number[0], number[1]))
