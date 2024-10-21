from config import aws_config, database_config
import boto3
from botocore.exceptions import NoCredentialsError


def upload_to_s3(object_name, data_for_s3):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_config.aws_access_key_id,
        aws_secret_access_key=aws_config.aws_secret_access_key,
        region_name=aws_config.region_name,
    )

    try:
        s3_client.put_object(
            Bucket=aws_config.s3_bucket_name, Key=object_name, Body=data_for_s3, ACL="public-read"
        )

    except NoCredentialsError:
        raise Exception("AWS credentials could not be provided or are invalid.")

    try:
        response = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": aws_config.s3_bucket_name, "Key": object_name},
            ExpiresIn=3600,
        )
        return response

    except NoCredentialsError:
        raise Exception(
            "Credentials could not be provided or are invalid when creating the presigned URL."
        )