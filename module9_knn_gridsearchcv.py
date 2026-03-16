import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score


class KNNGridSearch(object):
    def __init__(self):
        self.N = 0
        self.M = 0
        self.X_train = None
        self.Y_train = None
        self.X_test = None
        self.Y_test = None

    def load_training_data(self):
        self.N = int(input("Provide amount of training elements N: "))

        self.X_train = np.zeros(self.N)
        self.Y_train = np.zeros(self.N, dtype=int)

        print(f"Enter {self.N} training points:")
        for i in range(self.N):
            x = float(input(f"Enter x value for training point {i + 1}: "))
            y = int(
                input(
                    f"Enter y value for training point {i + 1} (non-negative integer): "
                )
            )
            self.X_train[i] = x
            self.Y_train[i] = y

    def load_test_data(self):
        self.M = int(input("Provide amount of test elements M: "))

        self.X_test = np.zeros(self.M)
        self.Y_test = np.zeros(self.M, dtype=int)

        print(f"Enter {self.M} test points:")
        for i in range(self.M):
            x = float(input(f"Enter x value for test point {i + 1}: "))
            y = int(
                input(f"Enter y value for test point {i + 1} (non-negative integer): ")
            )
            self.X_test[i] = x
            self.Y_test[i] = y

    def search_and_evaluate(self):
        X_train_reshaped = self.X_train.reshape(-1, 1)
        X_test_reshaped = self.X_test.reshape(-1, 1)

        knn = KNeighborsClassifier()

        max_k = self.N
        param_grid = {"n_neighbors": np.arange(1, max_k + 1)}

        cv_folds = min(5, self.N) if self.N > 1 else 1

        if cv_folds > 1:
            grid_search = GridSearchCV(knn, param_grid, cv=cv_folds, scoring="accuracy")
            grid_search.fit(X_train_reshaped, self.Y_train)

            best_k = grid_search.best_params_["n_neighbors"]
            best_model = grid_search.best_estimator_
        else:
            best_k = 1
            best_model = KNeighborsClassifier(n_neighbors=best_k)
            best_model.fit(X_train_reshaped, self.Y_train)

        predictions = best_model.predict(X_test_reshaped)

        accuracy = accuracy_score(self.Y_test, predictions)

        print("\n--- Results ---")
        print(f"Best k: {best_k}")
        print(f"Test accuracy: {accuracy}")


if __name__ == "__main__":
    m = KNNGridSearch()
    m.load_training_data()
    m.load_test_data()
    m.search_and_evaluate()
