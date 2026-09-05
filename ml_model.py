import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance.csv")

# Input features
X = df[
    [
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Internal_Marks"
    ]
]

# Target
y = df["Result"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# New student prediction
new_student = [[5, 85, 80, 78]]

prediction = model.predict(new_student)

print("Prediction:", prediction[0])