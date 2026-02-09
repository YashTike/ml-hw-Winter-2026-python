def index():
    n = int(input("Provide amount of elements N:"))

    l = []

    for i in range(n):
        m = int(input(f"Enter element {i + 1}:"))
        l.append(m)

    x = int(input("Enter number to search X:"))

    flag = False
    for i, val in enumerate(l):
        if val == x:
            print(f"Index: {i + 1}")
            flag = True
            break

    if not flag:
        print(-1)


if __name__ == "__main__":
    index()
