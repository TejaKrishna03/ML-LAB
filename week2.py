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

data = np.random.normal(170, 10, 1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
plt.show()




# 


np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].scatter(x, y, color='blue', alpha=0.5)
axs[0, 0].set_title('Scatter Plot')
axs[0, 0].set_xlabel('X')
axs[0, 0].set_ylabel('Y')

axs[0, 1].hist(x, bins=20, color='green', alpha=0.7)
axs[0, 1].set_title('Histogram')
axs[0, 1].set_xlabel('Value')
axs[0, 1].set_ylabel('Frequency')

plt.tight_layout()

plt.show()
