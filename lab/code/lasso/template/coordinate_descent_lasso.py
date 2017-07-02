# Code by Anastasiia Koloskova, MLO lab, EPFL

from collections import defaultdict
import numpy as np
import scipy
import scipy.sparse as sps
import math
import matplotlib.pyplot as plt
import time
from utils import *

def lasso_function(A, b, reg_coef, x):
    Ax = A.dot(x)
    return 0.5 * np.linalg.norm(Ax - b) ** 2 + reg_coef * np.sum(np.abs(x))

def coordinate_descent_lasso(A, b, reg_coef, max_iter=1000, trace=False, is_check=False,
                             check_epsilon=1e-1):
    history = defaultdict(list) if trace else None

    num_features = np.shape(A)[1]
    x_t = np.zeros(num_features)
    residual = np.copy(b)

    start_time = time.time()

    for current_iter in range(0, max_iter):
        if trace:
            history['time'].append(time.time() - start_time)
            history['residual_norm'].append(np.linalg.norm(residual))
            history['objective_function'].append(lasso_function(A, b, reg_coef, x_t))
        i = np.random.randint(0, num_features)
        if sps.issparse(A):
            current_feature = np.array(A[:, i].todense())
        else:
            current_feature = np.array(A[:, i])

        current_feature_norm = np.linalg.norm(current_feature)
        if current_feature_norm == 0:
            x_t[i] = 0
            continue
        
        ...
        
        new_value = soft_threshold( ... , reg_coef, current_feature_norm)
        residual += (current_feature * (x_t[i] - new_value)).reshape(residual.shape)
        x_t[i] = np.copy(new_value)

        if is_check:  # implement an optional check if a slightly smaller or larger step on the current coordinate would indeed make the function value worse
        
    return x_t, residual, history