import pandas as pd

df = pd.read_csv('dz.csv')

df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Группировка по городу и вычисление средней зарплаты
average_salary = df.groupby('City')['Salary'].mean()

# Вывод результата
print("Средняя зарплата по городам:")
print(average_salary)