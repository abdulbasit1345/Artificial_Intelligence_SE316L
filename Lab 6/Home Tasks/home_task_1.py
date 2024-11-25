import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

data = pd.DataFrame(pd.read_csv('C:\\Users\\Shaikh\\PycharmProjects\\'
                                'Artificial_Intelligence_SE316L\\Advertising.csv'))

A = data[['TV']]
B = data[['Radio']]
C = data[['Newspaper']]
Y = data[['Sales']]

A_train, A_test, y_train, y_test = train_test_split(A, Y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(A_train, y_train)

y_pred = model.predict(A_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Visualize the results
plt.scatter(A_test, y_test, color='blue', label='Actual Prices')
plt.scatter(A_test, y_pred, color='red', label='Predicted Prices')
plt.plot(A_test, y_pred, color='green', linewidth=2, label='Regression Line')
plt.title('TV sales Prediction')
plt.xlabel('TV Advertisement Cost')
plt.ylabel('TV Sales')
plt.legend()
plt.show()

# Predict sales when TV is 275
ad_cost = [[275]]
predicted_sales = model.predict(ad_cost)
print(f'Predicted sales when TV is 400: {predicted_sales[0][0]: .2f}')

# Visualize the prediction for TV = 400
plt.scatter(ad_cost, predicted_sales, color='orange', s=100, label='Prediction for TV=400')

# Adding labels and title
plt.title('TV Sales Prediction')
plt.xlabel('TV Advertising Budget')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
