import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1105105523 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = (x-0.5)*2/25
    alpha = 1 - p
    return a.mean() - np.sqrt(np.var(a)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(a)), \
           a.mean() - np.sqrt(np.var(a)) * norm.ppf(alpha / 2) / np.sqrt(len(a))
