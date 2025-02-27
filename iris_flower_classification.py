###Step 1: Import necessary libraries
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

"""
### Step 2: Load the Iris dataset"""

from sklearn.datasets import load_iris
iris = load_iris()

"""### Create a DataFrame from the Iris dataset"""

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species'] = df['species'].map(species_map)

"""### Step 3: Preprocess the data
###  No missing values check required for the Iris dataset from sklearn
### Split the data into features and target
"""

X = df.drop('species', axis=1)  # Features
y = df['species']               # Target

"""### Split the data into training and testing sets"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""### Standardize the features"""

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""### Step 4: Train a machine learning model"""

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

"""
### Step 5: Evaluate the model"""

y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

"""### Step 6: Visualize the results"""

sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

"""### Making predictions on new data
### Example: new data with measurements [sepal length, sepal width, petal length, petal width]
new_data = [[5.1, 3.5, 1.4, 0.2]]  # Example new data
"""

new_data = [[5.1, 3.5, 1.4, 0.2]]  # Example new data
new_data_scaled = scaler.transform(new_data)
prediction = model.predict(new_data_scaled)
print(f'Predicted species: {prediction[0]}')
