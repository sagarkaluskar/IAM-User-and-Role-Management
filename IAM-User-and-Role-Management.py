import boto3
from botocore.exceptions import ClientError

# Create an IAM client
iam_client = boto3.client('iam')

def create_iam_user(user_name):
    try:
        response = iam_client.create_user(UserName=user_name)
        print(f"User {user_name} created successfully.")
        return response
    except ClientError as e:
        print(f"Error creating user {user_name}: {e}")

def create_iam_role(role_name, assume_role_policy_document):
    try:
        response = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=assume_role_policy_document
        )
        print(f"Role {role_name} created successfully.")
        return response
    except ClientError as e:
        print(f"Error creating role {role_name}: {e}")

def attach_policy_to_user(user_name, policy_arn):
    try:
        response = iam_client.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
        print(f"Policy {policy_arn} attached to user {user_name}.")
        return response
    except ClientError as e:
        print(f"Error attaching policy to user {user_name}: {e}")

def attach_policy_to_role(role_name, policy_arn):
    try:
        response = iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        print(f"Policy {policy_arn} attached to role {role_name}.")
        return response
    except ClientError as e:
        print(f"Error attaching policy to role {role_name}: {e}")

def list_iam_users():
    try:
        response = iam_client.list_users()
        for user in response['Users']:
            print(f"User Name: {user['UserName']}")
    except ClientError as e:
        print(f"Error listing users: {e}")

def list_iam_roles():
    try:
        response = iam_client.list_roles()
        for role in response['Roles']:
            print(f"Role Name: {role['RoleName']}")
    except ClientError as e:
        print(f"Error listing roles: {e}")



