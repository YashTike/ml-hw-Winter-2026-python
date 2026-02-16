class Module5(object):
    def __init__(self):
        self.l = []
        self.n = 0

    def get_element(self):
        self.n = int(input("Provide amount of elements N:"))

    def input_range(self):
        for i in range(self.n):
            m = int(input(f"Enter element {i + 1}:"))
            self.l.append(m)

    def search(self):
        x = int(input("Enter number to search X:"))

        flag = False
        for i, val in enumerate(self.l):
            if val == x:
                print(f"Index: {i + 1}")
                flag = True
                break

        if not flag:
            print(-1)
