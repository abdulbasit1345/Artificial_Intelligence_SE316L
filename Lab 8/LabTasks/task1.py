import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.impute import SimpleImputer
import numpy as np

# Define the dataset
ratings_dict = {
    "item": [1, 2, 1, 2, 1, 2, 1, 2, 1],
    "user": ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
    "rating": [1, 2, 2, 4, 2.5, 4, 4.5, 5, 3],
}
df = pd.DataFrame(ratings_dict)

# Create a user-item matrix
user_item_matrix = df.pivot(index="user", columns="item", values="rating")

# Fill missing values with the mean rating for each user
imputer = SimpleImputer(strategy="mean")
user_item_matrix_filled = imputer.fit_transform(user_item_matrix)

# Compute cosine similarity between items
item_similarity = cosine_similarity(user_item_matrix_filled.T)

# Convert to DataFrame for easier manipulation
item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)


# Define a function to recommend items for a given user
def recommend_items(user_id, user_item_matrix, item_similarity_df, n_recommendations=2):
    user_ratings = user_item_matrix.loc[user_id]
    scores = item_similarity_df.dot(user_ratings.fillna(0))  # Weighted sum of item similarities
    scores = scores[user_ratings.isna()]  # Consider only items not yet rated by the user
    recommendations = scores.sort_values(ascending=False).head(n_recommendations)
    return recommendations


# Get recommendations for user 'E'
user_item_matrix = user_item_matrix.fillna(np.nan)  # Recreate the matrix with NaN for better indexing
recommended_items = recommend_items("E", user_item_matrix, item_similarity_df, n_recommendations=2)

print("Recommended movies for user 'E':")
for item_id, score in recommended_items.items():
    print(f"Movie {item_id}: Predicted score {score:.2f}")
