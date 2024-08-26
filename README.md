
# Titanic Survival Prediction

## Project Overview
This project is focused on predicting the survival of passengers on the Titanic using a machine learning model. The dataset used is the Titanic dataset, which contains various details about the passengers. The project involves data preprocessing, feature engineering, model building, and the development of a simple GUI for user interaction.

## Key Aspects of the Project
1. **Data Preprocessing**: 
   - Handled missing values in the `Age` and `Embarked` columns.
   - Created new features like `FamilySize`, `IsAlone`, and `HasCabin` to enhance model performance.
   - Extracted the `Title` from the `Name` column and performed one-hot encoding on categorical variables (`Title`, `Sex`, `Embarked`).
   - Dropped irrelevant columns such as `Name`, `Ticket`, and `Cabin`.

2. **Model Building**:
   - Implemented a Random Forest Classifier to predict the survival of passengers.
   - The model was trained and evaluated using an 80-20 train-test split.
   
3. **Model Evaluation**:
   - The model's performance was assessed using metrics like accuracy and a classification report.
   
4. **Graphical User Interface (GUI)**:
   - A simple GUI was developed using `tkinter` to allow users to input passenger details and predict survival.

## Getting Started
To get started with this project, ensure you have Python installed on your system along with the following libraries:
- `pandas`
- `scikit-learn`
- `tkinter`

You can run the script directly to use the GUI for making predictions based on user inputs.

## Usage
1. Clone the repository.
2. Ensure the Titanic dataset (`Titanic-Dataset.csv`) is in the same directory as the script.
3. Run the script `Titanic_Model.py` to launch the GUI and start making predictions.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
