# ============================================================
# IRIS FLOWER CLASSIFICATION - PYTHON SCRIPT
# Author: Anshuman Agrawal
# ============================================================

import pandas as pd
import numpy as np
import kagglehub
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# ============================================================
# DOWNLOAD DATASET
# ============================================================

path = kagglehub.dataset_download("saurabh00007/iriscsv")
print("Dataset downloaded to:", path)
print("Files:", os.listdir(path))

df = pd.read_csv(path + "/IRIS.csv")

# ============================================================
# SPLIT DATA
# ============================================================

X = df.iloc[:, :-1]
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ============================================================
# SCALE FEATURES
# ============================================================

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ============================================================
# TRAIN MODEL (SVM)
# ============================================================

model = SVC(kernel="linear")
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, pred))

# ============================================================
# SAVE MODEL
# ============================================================

pickle.dump(model, open("iris_model.pkl", "wb"))
print("Model saved as iris_model.pkl")
