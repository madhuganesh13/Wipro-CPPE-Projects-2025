import pandas as pd

print("Data Processor 1 running...")
df = pd.read_csv('../etl/transformed_data.csv')
df['price_rank'] = df['adjusted_price'].rank()
df.to_csv('processed_data_1.csv', index=False)
print("Data Processor 1 completed.")
