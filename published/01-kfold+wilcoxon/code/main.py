#!/usr/bin/python3

import numpy as np
from scipy import stats

A = np.array([0.82, 0.79, 0.83, 0.81, 0.80])
B = np.array([0.80, 0.76, 0.81, 0.78, 0.78])

stat, p = stats.wilcoxon(A, B, alternative="greater")

if p < 0.05:
    print("A performs significantly better than B")
