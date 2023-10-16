import evadb 
import boto3

from botocore.exceptions import ClientError
from datetime import datetime

bucket = "evadblambda"
now = datetime.now().strftime("%Y_%m_%d_%H:%M:%S")
# Connect to EvaDB and get a database cursor for running queries
cursor = evadb.connect().cursor()
    
filename = "eva_query_output_" + now + ".txt"
with open(filename, 'w') as f:
    # List all the built-in functions in EvaDB
    f.write(cursor.query("SELECT 2 > 1;").df().to_string())
    f.write('\n')
    f.write(cursor.query("SHOW FUNCTIONS;").df().to_string())
    
# Upload the file
s3_client = boto3.client('s3')

try:
    response = s3_client.upload_file(filename, bucket, filename)
except ClientError as e:
    print(e)




