import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales.csv")  # Open the data

print("Total Revenue:", data["revenue"].sum())  # Add it up

data.groupby("product")["revenue"].sum().plot(kind="bar")  # Make a chart
plt.title("Revenue by Product")
plt.show()