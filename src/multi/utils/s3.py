from botocore.exceptions import ClientError
from urllib.parse import urlparse

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
 

import boto3
 
S3 = 's3'
# bucket name
# note - we are considering that the bucket already exists in the aws environment.
# we can have a check_bucket function() to check whether the bucket exists or not
BUCKET = getenv("BUCKET_NAME")
BUCKET_IP = getenv("BUCKET_IP")

session = boto3.Session(
    aws_access_key_id=getenv("aws_access_key_id"),
    aws_secret_access_key=getenv("aws_secret_access_key")
)
s3_client = session.resource(S3)

the_bucket = s3_client.Bucket(BUCKET)
the_bucket_ip = s3_client.Bucket(BUCKET_IP)


class ServiceS3:

    # Delete s3 file
    def delete_file(file_name):

        try:
            delete = s3_client.meta.client.delete_object(Bucket=BUCKET, Key='multi/{}.json'.format(file_name))
        except ClientError as e:
            print(e)
        
        return delete


    # get the list of files from s3 bucket
    def list_files():
        contents = []
        try:
            for obj in the_bucket.objects.all():
                contents.append(obj)
        except ClientError as e:
            print(e)
    
        return contents
    
    # upload a file to s3 bucket
    def upload_file(file_name):
        try:
            data_file_folder = os.path.join(os.getcwd(), 'src/manage/temp')
            
            #dir_name = file_name
            file_name = file_name + '.json'

            if not file_name in os.listdir(data_file_folder):
                return False

            s3_client.meta.client.upload_file(
                os.path.join(data_file_folder, file_name),
                BUCKET,
                "multi/{}".format(file_name)
            )
            return True
        except ClientError as e:
            print(e)

    def upload_file_ip(file_name):
        try:
            data_file_folder = os.path.join(os.getcwd(), 'src/manage/temp')
            
            file_name_temp = file_name + '.txt'

            if not file_name_temp in os.listdir(data_file_folder):
                return False

            s3_client.meta.client.upload_file(
                os.path.join(data_file_folder, file_name_temp),
                BUCKET_IP,
                "{}".format(file_name)
            )
            return True
        except ClientError as e:
            print(e)
    
    
    # download a file from s3 bucket
    def download_file(file_name):
        destination = f'download/{file_name}'
        try:
            s3_client.download_file(BUCKET, file_name, destination)
            print('File downloaded successfully')
        except ClientError as e:
            print(e)


    