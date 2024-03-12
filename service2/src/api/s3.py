import boto3
import logging
from botocore.exceptions import ClientError


domain = 'https://s3.ir-thr-at1.arvanstorage.ir'
access_key = '24bafc43-0f00-4e8b-9ce5-6bc98a3a6fe7'
secret_key = '57eb6b58dfe991a47d9178ccf8862c1f2acdede2fd4bddb0712b75ff4eb4e9da'

logging.basicConfig(level=logging.INFO)

try:
   s3_resource = boto3.resource(
       's3',
       endpoint_url=domain,
       aws_access_key_id= access_key,
       aws_secret_access_key= secret_key
   )
except Exception as exc:
   logging.error(exc)
else:
       # bucket
    bucket = s3_resource.Bucket('songbox')


def download_file(object_name,download_path):
   try:
       bucket.download_file(
           object_name,
           download_path
       )
   except ClientError as e:
       logging.error(e)


# path = '/Users/sara/Desktop/amirkabir/spring02-03/Web server basics.pdf'
# name = 'Web server basics.pdf'

# download_file(name,path)