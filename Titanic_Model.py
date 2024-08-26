# Importing the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import tkinter as tk
from tkinter import messagebox

# Load the dataset
file_path = 'Titanic-Dataset.csv'
data = pd.read_csv(file_path)

# Handle missing values
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
data['HasCabin'] = data['Cabin'].notna().astype(int)
data.drop('Cabin', axis=1, inplace=True)

# Feature Engineering
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
data['IsAlone'] = (data['FamilySize'] == 1).astype(int)

# Extract Title from Name
data['Title'] = data['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
data['Title'] = data['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
data['Title'] = data['Title'].replace('Mlle', 'Miss')
data['Title'] = data['Title'].replace('Ms', 'Miss')
data['Title'] = data['Title'].replace('Mme', 'Mrs')
data = pd.get_dummies(data, columns=['Title', 'Sex', 'Embarked'], drop_first=True)

# Drop unnecessary columns
data.drop(['Name', 'Ticket'], axis=1, inplace=True)

# Prepare Features and Target
X = data.drop('Survived', axis=1)
y = data['Survived']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(report)

# Function to predict survival based on user input
def predict_survival():
    try:
        pclass = int(pclass_entry.get())
        age = float(age_entry.get())
        sibsp = int(sibsp_entry.get())
        parch = int(parch_entry.get())
        fare = float(fare_entry.get())
        has_cabin = has_cabin_var.get()
        sex_male = sex_var.get()
        embarked_q = embarked_q_var.get()
        embarked_s = embarked_s_var.get()

        # Create a DataFrame for the input data
        input_data = pd.DataFrame({
            'Pclass': [pclass],
            'Age': [age],
            'SibSp': [sibsp],
            'Parch': [parch],
            'Fare': [fare],
            'HasCabin': [has_cabin],
            'Sex_male': [sex_male],
            'Embarked_Q': [embarked_q],
            'Embarked_S': [embarked_s],
        })

        # Add FamilySize and IsAlone features
        input_data['FamilySize'] = input_data['SibSp'] + input_data['Parch'] + 1
        input_data['IsAlone'] = (input_data['FamilySize'] == 1).astype(int)

        # Ensure the input data has the same columns as the training data
        input_data = input_data.reindex(columns=X_train.columns, fill_value=0)

        # Make the prediction
        prediction = model.predict(input_data)
        result = "Survived" if prediction[0] == 1 else "Did not survive"
        messagebox.showinfo("Prediction Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid data")

# Create the main window
root = tk.Tk()
root.title("Titanic Survival Prediction")

# Styling
root.configure(bg="#f0f0f0")

# GUI layout with styling
tk.Label(root, text="Pclass (1, 2, or 3)", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
pclass_entry = tk.Entry(root, width=10)
pclass_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root, width=10)
age_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="SibSp (Siblings/Spouses aboard)", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10)
sibsp_entry = tk.Entry(root, width=10)
sibsp_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Parch (Parents/Children aboard)", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10)
parch_entry = tk.Entry(root, width=10)
parch_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Fare", bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=10)
fare_entry = tk.Entry(root, width=10)
fare_entry.grid(row=4, column=1, padx=10, pady=10)

has_cabin_var = tk.IntVar()
tk.Checkbutton(root, text="Has Cabin", variable=has_cabin_var, bg="#f0f0f0").grid(row=5, column=1, padx=10, pady=10)

sex_var = tk.IntVar()
tk.Radiobutton(root, text="Male", variable=sex_var, value=1, bg="#f0f0f0").grid(row=6, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Female", variable=sex_var, value=0, bg="#f0f0f0").grid(row=6, column=1, padx=10, pady=10)

embarked_q_var = tk.IntVar()
embarked_s_var = tk.IntVar()
tk.Checkbutton(root, text="Embarked Q", variable=embarked_q_var, bg="#f0f0f0").grid(row=7, column=0, padx=10, pady=10)
tk.Checkbutton(root, text="Embarked S", variable=embarked_s_var, bg="#f0f0f0").grid(row=7, column=1, padx=10, pady=10)

predict_button = tk.Button(root, text="Predict", command=predict_survival, bg="#4CAF50", fg="white")
predict_button.grid(row=8, column=1, padx=10, pady=10)

root.mainloop()
