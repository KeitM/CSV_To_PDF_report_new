import aspose.pdf as ap
import pandas as pd
import random
from datetime import datetime, timedelta

# Функция для генерации случайной даты в диапазоне
def random_date(start, end):
    """Генерирует случайную дату между start и end"""
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))  

# Параметры генерации данных
num_rows = random.randint(1,10)  
date_start = datetime(2020, 1, 1)  
date_end = datetime(2024, 12, 31)  

# Генерация случайных дат
dates = [random_date(date_start, date_end).strftime('%Y-%m-%d') for _ in range(num_rows)]  

# Генерация реалистичных числовых данных (open, high, low, close, volume)
numeric_data = []
for _ in range(num_rows):
    # Генерация open-цены в диапазоне 10-20
    open_price = random.uniform(10, 20)  
    
    # High = open + рандомное положительное отклонение
    high = open_price + random.uniform(0, 5)  
    # Low = open - рандомное положительное отклонение
    low = open_price - random.uniform(0, 5)  
    
    # Close = значение между low и high
    close = random.uniform(low, high)  
    
    # Volume = целое число в диапазоне 100-10,000
    volume = random.randint(100, 10000)  
    
    numeric_data.append([open_price, high, low, close, volume])

# Создание DataFrame
columns = ['open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(numeric_data, columns=columns)  
df.insert(0, 'date', dates)  # Добавление даты как первого столбца

# Сохранение в CSV
df.to_csv('trading_data.csv', index=False, float_format='%.2f')  # Форматирование чисел
print("Сгенерирован CSV-файл со случайными данными и датами")

# Чтение данных
df = pd.read_csv('trading_data.csv')

# Расчёт статистики
avg = df[['open', 'high', 'low', 'close', 'volume']].mean()
max_val = df[['open', 'high', 'low', 'close', 'volume']].max()

# Вывод в консоль
print("Средние значения:\n", avg)
print("\nМаксимальные значения:\n", max_val)

# Создать документ
document = ap.Document()
page = document.pages.add()

# Добавить текст в документ
def add_text_to_pdf(page, text):
    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 14
    page.paragraphs.add(text_fragment)

# Заголовок
add_text_to_pdf(page, "Расчёт трейдинговых данных\n")

# Средние значения
add_text_to_pdf(page, f"Средние значения:\n{str(avg)}\n")

# Максимальные значения
add_text_to_pdf(page, f"Максимальные значения:\n{str(max_val)}")

# Сохранить PDF
document.save("trading_data_calculation.pdf")