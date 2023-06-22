# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sc = []
    ln =[]
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for elem in student_marks:
        if elem == query_name:
            sc.append(sum(student_marks[elem]))
            ln.append(len(student_marks[elem]))

    answ = sc[0] / ln[0]
    print(f"{float(answ):.2f}")
