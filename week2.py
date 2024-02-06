import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
t = pd.read_csv("canada_per_capita_income.csv")
x = t.year
y = t.per_capita_income
plt.title("canada Per Capita Income")
plt.xlabel("Year")
plt.ylabel("per_capita_income.csv")
plt.scatter(x,y)
plt.plot(x,y)
plt.show()


#

x =  [1, 2, 3, 4]
y1 = [2, 3, 5, 7]
y2 = [1, 4, 9, 16]
y3 = [3, 6, 9, 12]

plt.plot(x,y1,color='red',label='line1')
plt.plot(x,y2,color='blue',label='line2')
plt.plot(x,y3,color='green',label="line3")
plt.legend()
plt.show()   


#

x = np.random.randint(low=1,high=30,size=10)
y = np.random.randint(low=1,high=20,size=10)

plt.scatter(x,y,marker="+")
plt.show()

#

df = pd.read_csv("cereal.csv")

plt.hist(df.calories)
plt.show()

#

df = pd.read_csv("cereal.csv")

df = df.head(5)
plt.figure(figsize=(8, 5))
plt.bar(df.name,df.calories)
plt.show()


#

categories = ['Apple', 'MI', 'Samsung', 'Oneplus', 'Iqoo', 'poco']
expenses = [1500, 300, 800, 600, 400, 200]

plt.figure(figsize=(8,5))
plt.title("Expense")
print(plt.pie(expenses, labels=categories))
plt.show()


#

x_positions = [1, 2, 3, 4]
y_positions = [5, 4, 3, 2]
quantities = [10, 20, 30, 40]

plt.figure(figsize=(8, 6))
plt.scatter(x_positions, y_positions, s=quantities, alpha=0.5,marker="+",c='red')

plt.title('Quantities with X and Y Positions')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()

#

data = np.random.normal(170, 10, 1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
plt.show()
