import pandas as pd
import numpy as np


chat_id = 1371486987 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
  t = 10
  v_mean = x.mean()
  a = v_mean / t
  return a # Ваш ответ
