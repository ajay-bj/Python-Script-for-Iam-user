import boto3

# Initialize the IAM client
iam = boto3.client('iam')

# Define the IAM user's username
user_name = 'youtube_test'

# Create the IAM user
iam.create_user(UserName=user_name)

# Print the user's details
user = iam.get_user(UserName=user_name)
print(f"User Name: {user['User']['UserName']}")
print(f"User ARN: {user['User']['Arn']}")