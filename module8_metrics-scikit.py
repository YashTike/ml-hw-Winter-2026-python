import numpy as np
from sklearn.metrics import precision_score, recall_score


class Module8(object):
    def __init__(self):
        self.N = 0
        self.X_data = None
        self.Y_data = None

    def get_element(self):
        self.N = int(input("Provide amount of elements N: "))

        self.X_data = np.zeros(self.N, dtype=int)
        self.Y_data = np.zeros(self.N, dtype=int)

    def input_range(self):
        for i in range(self.N):
            x = int(input(f"Enter x value for point {i + 1}: "))
            y = int(input(f"Enter y value for point {i + 1}: "))

            self.X_data[i] = x
            self.Y_data[i] = y

    def calculate_metrics(self):
        precision = precision_score(self.X_data, self.Y_data, zero_division=0)
        recall = recall_score(self.X_data, self.Y_data, zero_division=0)

        print(f"Precision: {precision}")
        print(f"Recall: {recall}")


if __name__ == "__main__":
    m = Module8()
    m.get_element()
    m.input_range()
    m.calculate_metrics()
