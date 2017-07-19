if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    temp = student_marks[query_name]
    sum = 0.00
    for marks in temp:
        sum += marks
    sum /= len(temp)
    print("%.2f" % sum)
