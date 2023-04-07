import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 681730925 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = np.std(x, ddof=1)
    n = len(x)

    scale = loc / np.sqrt(19*n)
    q1 = chi2.ppf(alpha / 2, df=n-1)
    q2 = chi2.ppf(1 - alpha / 2, df=n-1)
    lower = (n-1)*scale / q2
    upper = (n-1)*scale / q1

    return lower, upper
