import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Generate a small synthetic dataset of user ratings
np.random.seed(42)

# Users and movies
users = ["User1", "User2", "User3", "User4", "User5"]
movies = ["Movie1", "Movie2", "Movie3", "Movie4", "Movie5"]

# Create a ratings matrix with random ratings (1-5) and some NaN values
ratings_matrix = pd.DataFrame(
    np.random.choice([1, 2, 3, 4, 5, np.nan], size=(len(users), len(movies))),
    index=users,
    columns=movies
)


# Fill missing values with the mean rating of each user
ratings_filled = ratings_matrix.apply(lambda row: row.fillna(row.mean()), axis=1)

# Normalize the ratings for clustering
scaler = StandardScaler()
ratings_scaled = scaler.fit_transform(ratings_filled)

# Apply KMeans clustering
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
ratings_filled["Cluster"] = kmeans.fit_predict(ratings_scaled)

# Calculate similarity between users
user_similarity = cosine_similarity(ratings_scaled)

# Create a similarity DataFrame for easier lookup
user_similarity_df = pd.DataFrame(user_similarity, index=users, columns=users)



# Define a function to recommend movies for a user based on similar users in the same cluster
def recommend_movies(user, ratings_matrix, user_similarity_df, n_recommendations=2):
    if user not in ratings_matrix.index:
        print(f"User {user} not found in the dataset.")
        return []

    # Find the most similar users
    similar_users = user_similarity_df[user].sort_values(ascending=False).index[1:]

    similar_ratings = ratings_matrix.loc[similar_users].mean()


    user_ratings = ratings_matrix.loc[user]
    unrated_movies = user_ratings[user_ratings.isna()].index
    recommendations = similar_ratings[unrated_movies].sort_values(ascending=False).head(n_recommendations)
    return recommendations

# Get recommendations for a specific user
user_to_recommend = "User3"
recommended_movies = recommend_movies(user_to_recommend, ratings_matrix, user_similarity_df, n_recommendations=2)

print(f"\nRecommended movies for {user_to_recommend}:")
for movie, score in recommended_movies.items():
    print(f"{movie}: Predicted rating {score:.2f}")
