import pandas as pd
from faker import Faker

# Create a Faker instance
fake = Faker()

# Define the number of rows in the DataFrame
num_rows = 10000

# Create a dictionary with the data
data = {
    "id": [i for i in range(num_rows)],
    "text": [fake.sentence() for _ in range(num_rows)],
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
df.to_csv("/scratchpad/data/dummy_data.csv", index=False)
