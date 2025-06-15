import numpy as np
import pandas as pd
import polars as pl
import csv

from pandas import DataFrame  as df

import pandas as pd

df = pd.read_csv('trading_data.csv')

# Расчёт средних значений
averages = df[['open', 'high', 'low', 'close', 'volume']].mean()

# Расчёт максимальных значений
max_values = df[['open', 'high', 'low', 'close', 'volume']].max()

print("Средние значения:")
print(averages)

print("\nМаксимальные значения:")
print(max_values)