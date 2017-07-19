if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    second_max = sorted(set(list(arr)))[-2]
    print(second_max)
