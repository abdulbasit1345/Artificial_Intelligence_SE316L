import pandas as pd
from sklearn import preprocessing
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

print(species)
