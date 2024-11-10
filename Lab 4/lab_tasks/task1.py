import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB


data = {
    'weather': ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny',
                'rainy', 'sunny', 'overcast', 'overcast', 'rainy'],
    'temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'mild', 'mild', 'cool', 'mild', 'mild',
                    'hot', 'cool', 'mild'],
    'play': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

df = pd.DataFrame(data)

le_weather = LabelEncoder()
le_temperature = LabelEncoder()
le_play = LabelEncoder()

weather_encoded = le_weather.fit_transform(df['weather'])
temperature_encoded = le_temperature.fit_transform(df['temperature'])
play_encoded = le_play.fit_transform(df['play'])


features = list(zip(weather_encoded, temperature_encoded))
features_train, features_test, label_train, label_test = train_test_split(features, play_encoded,
                                                                          test_size=0.3, random_state=43)

model = GaussianNB()
model.fit(features_train, label_train)

input_data = pd.DataFrame({
    'weather': le_weather.transform(['overcast']),
    'temperature': le_temperature.transform(['mild'])
})

prediction = model.predict(input_data)

predicted_play = le_play.inverse_transform(prediction)

print(f"\nPrediction: Can players play? {predicted_play[0]}")

predicted_f = model.predict(features_test)
conf_mat = confusion_matrix(label_test, predicted_f)
print(f"\nConfusion Matrix: {conf_mat}")

accuracy = accuracy_score(label_test, predicted_f)
print("\nAccuracy: ", accuracy)
