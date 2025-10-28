import boto3
import json
import pandas as pd
from decimal import Decimal
import sys

# --- Configuration ---
REGION_NAME = 'eu-north-1'  # e.g., 'us-east-1'. MUST match your DynamoDB table region
TABLE_NAME = 'ecommerce-vm'
CSV_FILE_PATH = 'AWST1.csv'

# Initialize the DynamoDB resource
# Boto3 automatically uses the IAM role from the EC2 instance
try:
    dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
    table = dynamodb.Table(TABLE_NAME)
except Exception as e:
    print(f"Error initializing DynamoDB: {e}")
    sys.exit(1)

# Function to safely convert pandas object to DynamoDB-friendly dictionary
def convert_to_dynamodb_item(df_row):
    # Convert any numbers (like price) to Decimal, as float is not supported
    # Convert the pandas Series to a dict
    item = df_row.to_dict()
    
    # Iterate and convert numeric types to Decimal for DynamoDB compatibility
    for key, value in item.items():
        if pd.api.types.is_numeric_dtype(type(value)):
            # Handle float conversions by ensuring precision with Decimal
            item[key] = Decimal(str(value))
            
    return item

# --- Main Import Logic ---
def load_data_to_dynamodb():
    print(f"Starting data load for table: {TABLE_NAME}...")
    try:
        # 1. Read the CSV using pandas
        df = pd.read_csv(CSV_FILE_PATH)
        items_to_write = df.apply(convert_to_dynamodb_item, axis=1).tolist()
        
        # 2. Use batch_writer for efficient writing
        with table.batch_writer() as batch:
            for i, item in enumerate(items_to_write):
                batch.put_item(Item=item)
                if (i + 1) % 100 == 0:
                    print(f"Processed {i + 1} items...")
        
        print(f"\n--- SUCCESS ---")
        print(f"Total records imported: {len(items_to_write)}")
        
    except FileNotFoundError:
        print(f"\n--- ERROR ---")
        print(f"File not found: {CSV_FILE_PATH}")
    except Exception as e:
        print(f"\n--- FATAL ERROR DURING BATCH WRITE ---")
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    load_data_to_dynamodb()