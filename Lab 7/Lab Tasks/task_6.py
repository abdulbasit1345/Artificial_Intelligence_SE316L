import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Example: CSV file containing data
data = pd.read_csv('C:\\Users\\Shaikh\\PycharmProjects\\Artificial_Intelligence_SE316L\\Lab 7\\home.csv')

# Inspect the dataset
print(data.head())

# Drop missing values
data = data.dropna()

# Convert categorical columns to numeric using one-hot encoding
data = pd.get_dummies(data, columns=['location', 'type'], drop_first=True)

# Separate features and target
X = data.drop('price', axis=1)  # Features
y = data['price']              # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Prediction: ", y_pred, "\n")

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-Squared Value: {r2}")



plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()

