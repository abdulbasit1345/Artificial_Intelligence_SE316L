import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

data = pd.DataFrame(pd.read_csv('C:\\Users\\Shaikh\\PycharmProjects\\'
                                'Artificial_Intelligence_SE316L\\Advertising.csv'))

A = data[['TV']]
Y = data[['Sales']]

A_train, A_test, y_train, y_test = train_test_split(A, Y, test_size=0.2, random_state=42)

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
plt.xlabel('TV')
plt.ylabel('Sales')
plt.legend()
plt.show()
