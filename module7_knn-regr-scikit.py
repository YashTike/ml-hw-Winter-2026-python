import numpy as np
from sklearn.neighbors import KNeighborsRegressor


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
        print(f"Enter {self.N} points")
        for i in range(self.N):
            x = float(input(f"Enter x value for point {i + 1}: "))
            y = float(input(f"Enter y value for point {i + 1}: "))

            self.X_data[i] = x
            self.Y_data[i] = y

    def search(self):
        target_x = float(input("Enter X value to predict Y: "))

        X_train = self.X_data.reshape(-1, 1)
        Y_train = self.Y_data

        knn = KNeighborsRegressor(n_neighbors=self.k)

        knn.fit(X_train, Y_train)

        prediction = knn.predict(np.array([[target_x]]))

        variance = np.var(Y_train)

        print(f"Result (Y): {prediction[0]}")
        print(f"Variance of training labels: {variance}")


if __name__ == "__main__":
    m = Module6()
    m.get_element()
    m.input_range()
    m.search()
