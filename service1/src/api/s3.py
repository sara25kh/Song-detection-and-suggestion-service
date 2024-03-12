import sys
import boto3
import logging
from botocore.exceptions import ClientError

domain = 'https://s3.ir-thr-at1.arvanstorage.ir'
access_key = '24bafc43-0f00-4e8b-9ce5-6bc98a3a6fe7'
secret_key = '57eb6b58dfe991a47d9178ccf8862c1f2acdede2fd4bddb0712b75ff4eb4e9da'

logging.basicConfig(level=logging.INFO)

s3_resource = None
try:
    s3_resource = boto3.resource(
        's3',
        endpoint_url=domain,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

except Exception as exc:
   logging.error(exc)
else:
    bucket = s3_resource.Bucket('bucket-name')


def upload_file(object_name , file_path):
    global s3_resource
    try:
        bucket = s3_resource.Bucket('songbox')

        with open(file_path, "rb") as file:
            res = bucket.put_object(
                ACL='private',
                Body=file,
                Key=object_name
            )
    except ClientError as e:
        logging.error(e)

    logging.info(f'File-{object_name} uploaded successfully')
    logging.info(f'res is: {res}')


# path = '/Users/sara/Desktop/amirkabir/spring02-03/cloud computing/Web server basics.pdf'
# name = 'Web server basics.pdf'

# upload_file(name , path)