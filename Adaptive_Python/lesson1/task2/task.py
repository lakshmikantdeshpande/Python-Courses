# put your python code here
def convert(temp):
    print(temp.upper() if temp.islower() else (temp.lower() if temp.isupper() else temp))


if __name__ == "__main__":
    temp = input()
    convert(temp)
