import numpy as np

def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    X = np.asarray(X)
    y = np.asarray(y)
    
    n_features = X.shape[1]
    
    w = np.linalg.inv(X.T @ X + lam * np.eye(n_features)) @ X.T @ y
    
    return w