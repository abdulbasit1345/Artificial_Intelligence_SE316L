import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
data_size = 100
income_data = {
    'Income': np.random.randint(20000, 120000, data_size),
    'Age': np.random.randint(18, 70, data_size)
}

# Create a DataFrame
income_df = pd.DataFrame(income_data)

# Save to CSV
income_df.to_csv('income.csv', index=False)
print("Generated income.csv with synthetic data.")
income_df

