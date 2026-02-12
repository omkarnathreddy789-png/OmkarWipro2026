import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

df = pd.DataFrame({"Month": months, "Sales": sales})

plt.figure()
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

plt.figure()
sns.barplot(data=df, x="Month", y="Sales")
plt.title("Monthly Sales Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
