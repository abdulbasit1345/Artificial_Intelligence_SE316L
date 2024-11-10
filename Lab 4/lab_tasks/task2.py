import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split


data = {
    'age': ['youth', 'youth', 'middle_aged', 'senior', 'senior', 'senior', 'middle_aged',
            'youth', 'youth', 'senior', 'youth', 'middle_aged', 'middle_aged', 'senior'],
    'income': ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low',
               'medium', 'medium', 'medium', 'high', 'medium'],
    'student': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes',
                'no', 'yes', 'no'],
    'credit_rating': ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent',
                      'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'excellent'],

    'class': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes',
              'yes', 'no']
    }

df = pd.DataFrame(data)

age = df['age']
income = df['income']
student = df['student']
credit_rating = df['credit_rating']
class_ = df['class']


encode_age = LabelEncoder()
encode_income = LabelEncoder()
encode_student = LabelEncoder()
encode_credit_rating = LabelEncoder()
encode_class_ = LabelEncoder()

le_age = encode_age.fit_transform(age)
le_income = encode_income.fit_transform(income)
le_student = encode_student.fit_transform(student)
le_credit_rating = encode_credit_rating.fit_transform(credit_rating)
le_class_ = encode_class_.fit_transform(class_)

features = list(zip(le_age, le_income, le_student, le_credit_rating))

features_train, features_test, label_train, label_test = train_test_split(features, le_class_,
                                                                          test_size=0.3, random_state=43)
model = CategoricalNB()
model.fit(features_train, label_train)


input_data = pd.DataFrame({
    'age': encode_age.fit_transform(['youth']),
    'income': encode_income.fit_transform(['medium']),
    'student': encode_student.fit_transform(['yes']),
    'credit_rating': encode_credit_rating.fit_transform(['fair'])
})

predicted = model.predict(input_data)
decoded = encode_class_.inverse_transform(predicted)

print(f"\n The classification (class) of given input using naive bayes algorithm is: {decoded[0]}")

predicted_f = model.predict(features_test)
conf_mat = confusion_matrix(label_test, predicted_f)
print(f"\nConfusion Matrix: {conf_mat}")

accuracy = accuracy_score(label_test, predicted_f)
print("\nAccuracy: ", accuracy)

