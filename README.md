# Titanic Survival Prediction 🚢

A beginner Machine Learning project that predicts whether a passenger survived the Titanic disaster using a **Decision Tree Classifier** built with Scikit-learn.

---

## 📌 Project Overview

This project uses the Titanic dataset to train a Machine Learning model that predicts whether a passenger survived based on the following features:

- Passenger Class (Pclass)
- Sex
- Age
- Fare

The project includes data preprocessing, model training, prediction, and evaluation using a Decision Tree Classifier.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn

---

## 📂 Project Structure

```
titanic-survival-prediction/
│
├── main.py
├── Titanic-Dataset.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Data Preprocessing

Before training the model:

- Selected relevant features:
  - Pclass
  - Sex
  - Age
  - Fare
- Filled missing values in the **Age** column using the mean age.
- Converted the **Sex** column into numerical values:
  - Male → 0
  - Female → 1

---

## 🤖 Machine Learning Model

**Algorithm Used:**

- Decision Tree Classifier

The dataset is divided into:

- **80% Training Data**
- **20% Testing Data**

The model is trained using the training dataset and evaluated on the testing dataset.

---

## 📊 Evaluation

The model's performance is measured using:

- Accuracy Score

Example output:

```
Training samples: 712
Testing samples: 179
Accuracy: 0.82
```

*(The accuracy may vary slightly due to train-test splitting.)*

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/mannshah-codes/titanic-survival-prediction.git
```

### Navigate to the project

```bash
cd titanic-survival-prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python main.py
```

---

## 📈 Future Improvements

- Add more features such as:
  - SibSp
  - Parch
  - Embarked
- Perform feature engineering.
- Compare multiple Machine Learning algorithms.
- Improve accuracy using Random Forest and Gradient Boosting.
- Perform hyperparameter tuning.

---

## 👨‍💻 Author

**Mann Shah**

- AI/ML Intern
- Computer Vision Enthusiast
- Python Developer

GitHub: https://github.com/mannshah-codes

---

⭐ If you found this project useful, consider giving it a star!