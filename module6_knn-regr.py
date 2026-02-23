import numpy as np


class Module6(object):
    def __init__(self):
        self.N = 0
        self.k = 0
        self.X_data = None
        self.Y_data = None

    def get_element(self):
        self.N = int(input("Provide amount of elements N: "))
        self.k = int(input("Provide k (positive integer): "))

        self.X_data = np.zeros(self.N)
        self.Y_data = np.zeros(self.N)

    def input_range(self):
        for i in range(self.N):
            x = float(input(f"Enter x value for point {i + 1}: "))
            y = float(input(f"Enter y value for point {i + 1}: "))

            self.X_data[i] = x
            self.Y_data[i] = y

    def search(self):
        target_x = float(input("Enter X value to predict Y: "))

        if self.k > self.N:
            print(
                "Error: k cannot be strictly greater than the number of available points N."
            )
            return

        distances = np.abs(self.X_data - target_x)

        k_nearest_indices = np.argsort(distances)[: self.k]

        nearest_y_values = self.Y_data[k_nearest_indices]

        predicted_y = np.mean(nearest_y_values)

        print(f"Result (Y): {predicted_y}")


if __name__ == "__main__":
    m = Module6()
    m.get_element()
    m.input_range()
    m.search()
