# put your python code here
def compare(A, B, values):
    if values[A] >= values[B]:
        return 0
    else:
        return -1


if __name__ == "__main__":
    values = {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000}
    string = input().strip()

    i = 0
    temp = 0
    found = False
    while i < len(string) - 1:
        diff = compare(string[i], string[i + 1], values)
        if diff is 0:
            temp += values[string[i]]
        else:
            found = True
            temp += values[string[i + 1]] - values[string[i]]
            i += 1
        i += 1
    if not found:
        temp += values[string[len(string) - 1]]
    print(temp)
