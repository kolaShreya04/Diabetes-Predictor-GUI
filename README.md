# Diabetes Risk Prediction System

Machine learning models for non-invasive diabetes prediction using the Framingham dataset, with an interactive GUI.

## Models Used
- Random Forest
- XGBoost  
- SVM
- SGD Classifier
- Linear Regression
- Decision Tree

## Tech Stack
- Python, Pandas, NumPy
- Scikit-learn, XGBoost
- Tkinter (GUI)
- Pickle (model saving)

## Project Structure
```
├── framingham.csv          # Dataset
├── main.py                 # Random Forest model
├── Main2.py                # Model comparison (SVM, SGD, LR)
├── ML_V2.py                # XGBoost model
├── gui.py                  # Tkinter GUI
└── requirements.txt        # Dependencies
```

## Installation
```bash
pip install -r requirements.txt
```

## Run
```bash
# GUI
python gui.py

# Train models
python main.py
python ML_V2.py
python Main2.py
```

## Results
Random Forest achieved ~98% accuracy on test data.

## Team
Christina, Karina, Paola, Shreya
