
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

class LinearRegressionModel:

    def __init__(self, X, y):
        """
        X : list of numbers (single feature)
        y : list of numbers
        """
        if len(X) != len(y):
            raise ValueError("X and y must have the same length")

        self.X = list(X)  # store as list
        self.y = list(y)

        self.model = LinearRegression()
        self.coef_ = None
        self.intercept_ = None
        self.r2_ = None
        self.trained = False

    def go(self):
        """Train the model using sklearn"""
        X_np = np.array(self.X).reshape(-1, 1)
        y_np = np.array(self.y)

        self.model.fit(X_np, y_np)

        self.coef_ = float(self.model.coef_[0])
        self.intercept_ = float(self.model.intercept_)

        y_pred = self.model.predict(X_np)
        self.r2_ = float(r2_score(y_np, y_pred))

        self.trained = True

    def predict(self, X):
        if not self.trained:
            raise RuntimeError("Model is not trained. Call go() first")

        X_np = np.array(X).reshape(-1, 1)
        return self.model.predict(X_np)

    def __len__(self):
        return len(self.X)

    def __str__(self):
        if not self.trained:
            return f"LinearRegressionModel with {len(self)} observations (not trained)"
        return (
            f"LinearRegressionModel | n={len(self)} | "
            f"R^2={self.r2_:.3f} | y={self.coef_:.3f}x + {self.intercept_:.3f}"
        )

    def require_trained(self):
        if not self.trained:
            raise RuntimeError("Model is not trained yet")

    def __gt__(self, other):
        self.require_trained()
        if isinstance(other, (int, float)):
            return self.r2_ > other
        if isinstance(other, LinearRegressionModel):
            other.require_trained()
            return self.r2_ > other.r2_
        return NotImplemented

    def __add__(self, new_data):
        """
        Usage:
            model + (x_new, y_new)

        x_new, y_new can be single values or lists
        """
        if not (isinstance(new_data, tuple) and len(new_data) == 2):
            raise TypeError("Use: model + (x_new, y_new)")

        x_new, y_new = new_data

        if isinstance(x_new, list):
            if len(x_new) != len(y_new):
                raise ValueError("x_new and y_new must have same length")
            self.X.extend(x_new)
            self.y.extend(y_new)
        else:
            self.X.append(x_new)
            self.y.append(y_new)

        self.trained = False  # data changed → model must retrain
        self.r2_ = None

        return self

    def __getitem__(self, item):
        return self.predict(item)

X = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

model = LinearRegressionModel(X, y)
print(model)
print(len(model))

model.go()
print(model)

if model.r2_ > 0.8:
    print('Good model!')

if model > 0.8:
    print('Good model!')


model + (6, 12)
model + ([7, 8], [14, 16])

model.go()
print(model)

print(model.predict(6))
print(model[6])
