import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get bucket and key from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download the JSON file to /tmp
    local_file = '/tmp/' + key.split('/')[-1]
    s3.download_file(bucket, key, local_file)

    # Process file
    with open(local_file, 'r') as f:
        data = json.load(f)

    processed_data = {
        "processed": True,
        "data": data
    }

    # Upload processed file back to S3
    output_key = "processed/" + key
    s3.put_object(Bucket=bucket, Key=output_key, Body=json.dumps(processed_data))

    return {
        "status": "success",
        "output_key": output_key
    }

