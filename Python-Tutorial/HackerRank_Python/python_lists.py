if __name__ == '__main__':
    N = int(input())
    List = []
    for i in range(0, N):
        choice = input().split()
        if choice[0] == "insert":
            List.insert(int(choice[1]), int(choice[2]))
        elif choice[0] == "print":
            print(List)
        elif choice[0] == "remove":
            List.remove(int(choice[1]))
        elif choice[0] == "append":
            List.append(int(choice[1]))
        elif choice[0] == "sort":
            List.sort()
        elif choice[0] == "pop":
            List.pop()
        elif choice[0] == "reverse":
            List.reverse()
