# put your python code here
def compare(A, B):
    return A >= B


def romanToDecimal(str, values):
    i = 0
    result = 0

    while (i < len(str)):
        digit1 = values[str[i]]

        if (i + 1 < len(str)):
            digit2 = values[str[i + 1]]
            if compare(digit1, digit2):
                # digit1 >= digit2
                result = result + digit1
                i = i + 1
            else:
                result = result + digit2 - digit1
                i = i + 2
        else:
            result = result + digit1
            i = i + 1

    return result


if __name__ == "__main__":
    values = {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000}
    string = input().strip()
    print(str(romanToDecimal(string, values)))
