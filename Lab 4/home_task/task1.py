import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv("C:\\Users\\Shaikh\\PycharmProjects\\Artificial_Intelligence_SE316L\\penguins.csv")
df = pd.DataFrame(dataset)

species = df["species"]
island = df["island"]
bill_length_mm = df["bill_length_mm"]
bill_depth_mm = df["bill_depth_mm"]
flipper_length_mm = df["flipper_length_mm"]
body_mass_g = df["body_mass_g"]
sex = df["sex"]
year = df["year"]

df.drop_duplicates(subset=['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
                           'body_mass_g', 'year'], keep='last')

le_species = LabelEncoder()
le_island = LabelEncoder()
le_bill_length_mm = LabelEncoder()
le_bill_depth_mm = LabelEncoder()
le_flipper_length_mm = LabelEncoder()
le_body_mass_g = LabelEncoder()
le_sex = LabelEncoder()
le_year = LabelEncoder()

species_encoded = le_species.fit_transform(species)
island_encoded = le_island.fit_transform(island)
bill_length_mm_encoded = le_bill_length_mm.fit_transform(bill_length_mm)
bill_depth_mm_encoded = le_bill_depth_mm.fit_transform(bill_depth_mm)
flipper_length_mm_encoded = le_flipper_length_mm.fit_transform(flipper_length_mm)
body_mass_g_encoded = le_body_mass_g.fit_transform(body_mass_g)
sex_encoded = le_sex.fit_transform(sex)
year_encoded = le_year.fit_transform(year)

features = list(zip(island_encoded, bill_length_mm_encoded, bill_depth_mm_encoded,
                    flipper_length_mm_encoded, body_mass_g_encoded, sex_encoded))
features_train, features_test, label_train, label_test = train_test_split(features, species_encoded,
                                                                          test_size=0.4, random_state=43)

model = GaussianNB()
model.fit(features_train, label_train)

# Chinstrap,Dream,50.2,18.7,198.0,3775.0,female,2009
input_data = pd.DataFrame({
    'island': le_island.transform(['Dream']),
    'bill_length_mm': le_bill_length_mm.transform([50.2]),
    'bill_depth_mm': le_bill_depth_mm.transform([18.7]),
    'flipper_length_mm': le_flipper_length_mm.transform([198.0]),
    'body_mass_g': le_body_mass_g.transform([3775.0]),
    'sex': le_sex.transform(['female'])
})

prediction = model.predict(input_data)

prediction_decoded = le_species.inverse_transform(prediction)
print(f"What is the Species of the given penguin based on prediction: {prediction_decoded[0]}")

predicted_f = model.predict(features_test)
conf_mat = confusion_matrix(label_test, predicted_f)
print(f"\nConfusion Matrix: {conf_mat}")

accuracy = accuracy_score(label_test, predicted_f)
print("\nAccuracy: ", accuracy)


# print(species)
