import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0.0

    for _ in range(steps):
        linear_preds = np.dot(X, weights) + bias
        predictions = _sigmoid(linear_preds)

        dw = (1 / n_samples) * np.dot(X.T, (predictions - y))
        db = (1 /  n_samples) * np.sum(predictions - y)

        weights = weights - lr * dw
        bias = bias - lr * db

    return weights, bias