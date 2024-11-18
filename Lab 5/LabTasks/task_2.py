import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = {
    'gender': ["male", "male", "male", "male", "female", "female", "female", "female"],
    'height': [6.00, 5.92, 5.58, 5.98, 5.00, 5.50, 5.42, 5.75],
    'weight': [180, 190, 170, 165, 100, 150, 130, 150],
    'foot_size': [12, 11, 12, 10, 6, 8, 7, 9]
}

df = pd.DataFrame(data)


def update_dataset(new_entry, target):
    data['gender'].append(target[0])
    data['height'].append(new_entry[0][0])
    data['weight'].append(new_entry[0][1])
    data['foot_size'].append(new_entry[0][2])
    df = pd.DataFrame(data)
    return df


gender = df['gender']
height = df['height']
weight = df['height']
foot_size = df['foot_size']

le_gender = LabelEncoder()

gender_encoded = le_gender.fit_transform(df['gender'])

features = list(zip(height, weight, foot_size))
feature_train, feature_test, label_train, label_test = train_test_split(features, gender_encoded,
                                                                        test_size=0.4, random_state=60)

model = DecisionTreeClassifier()
model.fit(feature_train, label_train)

new_entry = [[6.00, 180, 12]]
prediction = model.predict(new_entry)

predicted = le_gender.inverse_transform(prediction)
print(update_dataset(new_entry, predicted))

print(f"The new person with {new_entry} is: {predicted}")

predicted_test = model.predict(feature_test)
conf_mat = confusion_matrix(label_test, predicted_test)
print(f"\nConfusion Matrix: {conf_mat}")

accuracy = accuracy_score(label_test, predicted_test)
print(f"\nAccuracy: {accuracy:.2f}")
