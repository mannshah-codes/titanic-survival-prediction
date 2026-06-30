import pandas as pd

# Load dataset
df = pd.read_csv("projects/Titanic-Dataset.csv")

# Features
X = df[["Pclass", "Age", "Fare", "Sex"]].copy()

# Target
y = df["Survived"]

# Fill missing Age values
X["Age"] = X["Age"].fillna(X["Age"].mean())

# Convert Sex to numbers
X["Sex"] = X["Sex"].map({
    "male": 0,
    "female": 1
})

print(X.head())
print(y.head())

# Split dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# Train model
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("Model trained successfully")

# Predict
predictions = model.predict(X_test)

# Accuracy
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)