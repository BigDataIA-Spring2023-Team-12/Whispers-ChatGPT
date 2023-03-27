import boto3

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

