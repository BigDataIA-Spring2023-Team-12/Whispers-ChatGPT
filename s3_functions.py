import boto3
import os
def upload_audio_to_s3(audio_file_path, s3_bucket_name, s3_object_key):
    """
    Uploads an audio file to an S3 bucket.

    Args:
    - audio_file_path (str): The local file path to the audio file.
    - s3_bucket_name (str): The name of the S3 bucket to upload the file to.
    - s3_object_key (str): The object key (file name) to use for the uploaded file in the S3 bucket.

    Returns:
    - None
    """
    # Create an S3 client
    s3 = boto3.client('s3')

    # Upload the audio file to the S3 bucket
    with open(audio_file_path, "rb") as audio_file:
        s3.upload_fileobj(audio_file, s3_bucket_name, s3_object_key)

    print(f"File {audio_file_path} uploaded to S3 bucket {s3_bucket_name} with key {s3_object_key}")


def upload_text_file_to_s3(file_path, bucket_name, object_name):
    """
    Upload a text file to an S3 bucket.

    :param file_path: Path to the local file to upload.
    :param bucket_name: Name of the S3 bucket to upload to.
    :param object_name: Object name to use for the uploaded file.

    Exampe:
    upload_text_file_to_s3('path/to/local/file.txt', 'my-bucket', 'my-file.txt')

    """
    # Create an S3 client
    s3 = boto3.client('s3')

    # Upload the file
    with open(file_path, "rb") as f:
        s3.upload_fileobj(f, bucket_name, object_name)

def download_audio_file(bucket_name, file_key, local_path):
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(bucket_name).download_file(file_key, local_path)
        print(f"File {file_key} downloaded successfully from bucket {bucket_name} to {local_path}")
    except Exception as e:
        print(f"Error downloading file {file_key} from bucket {bucket_name}: {e}")



def download_all_files_from_s3_bucket(bucket_name, local_directory):
    # create the S3 resource
    s3 = boto3.resource('s3')

    # create the bucket object
    bucket = s3.Bucket(bucket_name)

    # create the local directory if it doesn't exist
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    # download each object in the bucket
    for obj in bucket.objects.all():
        # create the local file path
        local_file_path = os.path.join(local_directory, obj.key)

        # download the object
        bucket.download_file(obj.key, local_file_path)

        print(f"Downloaded {obj.key} to {local_file_path}")

download_all_files_from_s3_bucket("the-data-guys", "batch/")
# download_audio_file("the-data-guys", "adhoc/steve-jobs-think-different.mp3", 'sample.mp3')


# print(upload_audio_to_s3("steve-jobs-think-different.mp3","the-data-guys","adhoc/steve-jobs-think-different.mp3"))

# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)