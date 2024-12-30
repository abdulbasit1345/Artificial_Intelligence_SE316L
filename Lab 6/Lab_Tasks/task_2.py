import pandas as pd
from sklearn.cluster import KMeans

# Step 1: Define the dataset
data = {
    'Objects': ['OB-1', 'OB-2', 'OB-3', 'OB-4', 'OB-5', 'OB-6', 'OB-7', 'OB-8'],
    'X': [1, 1, 1, 2, 1, 2, 1, 2],
    'Y': [4, 2, 4, 1, 1, 4, 1, 1],
    'Z': [1, 2, 2, 2, 1, 2, 2, 1]
}

df = pd.DataFrame(data)

features = df[['X', 'Y', 'Z']]

# Step 3: Apply K-Means Clustering
km = KMeans(n_clusters=2, random_state=42)
df['Cluster'] = km.fit_predict(features)

print("Cluster Assignments:")
print(df[['Objects', 'Cluster']])

print("\nCluster Centers:")
print("\n", km.cluster_centers_)
