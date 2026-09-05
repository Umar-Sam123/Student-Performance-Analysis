import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("student_performance.csv")
st.title("🎓 Student Performance Dashboard")
st.subheader("Student Data")
st.dataframe(df)
st.subheader("Statistics")
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Students",
    len(df)
)

col2.metric(
    "Average Marks",
    round(df["Final_Marks"].mean(), 2)
)

col3.metric(
    "Average Attendance",
    round(df["Attendance"].mean(), 2)
)
st.subheader("Final Marks")
fig, ax = plt.subplots()
ax.bar(
    df["Name"],
    df["Final_Marks"]
)
ax.set_xlabel("Student")
ax.set_ylabel("Final Marks")
plt.xticks(rotation=45)
st.pyplot(fig)
st.subheader("Result")
st.bar_chart(
    df["Result"].value_counts()
)