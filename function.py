def student(name,marks):
    le = len(marks)
    s = sum(marks)/le
    print(name)
    print(marks)
    print(s)
    if s >= 90 and s < 100:
        print("A+")
    elif s >= 80 and s < 90:
        print("A")
    elif s >= 70 and s < 80:
        print("B")
    elif s >= 60 and s < 70:
        print("c")
    elif s >= 50 and s < 60:
        print("D")
    else:
        print("sidara fail chi")