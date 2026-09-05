import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

plt.bar(df["Name"], df["Final_Marks"])

plt.xlabel("Student")
plt.ylabel("Final Marks")
plt.title("Student Final Marks")

plt.xticks(rotation=45)

plt.show()
plt.scatter(df["Study_Hours"], df["Final_Marks"])

plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")

plt.show()
result = df["Result"].value_counts()

plt.pie(
    result,
    labels=result.index,
    autopct="%1.1f%%"
)

plt.title("Pass vs Fail")
plt.show()