import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1105105523 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t=5
    return 2*(  -1/2 - (-x).min() )/(t*t), \
           2*( -np.log(1-p)/(x.size) - 1/2 - (-x).min() )/(t*t)
