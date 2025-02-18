import boto3
import json

#Import all the modules and libraries. boto3 is a module used to interact with AWS. 

from botocore.exceptions import ClientError

iam = boto3.client("iam")

#boto3.client() is a method provided by the Boto3 library (the AWS SDK for Python) that creates a client object for a specific AWS service. The client() method is used to interact with AWS services, allowing you to make API requests to the service. By passing "iam" to boto3.client(), you're specifying that you want to interact with IAM.

#1 CREATE AN IAM USER

# Initialize IAM client
#iam = boto3.client('iam')

# Create user
#response = iam.create_user(UserName='test-user')

# Print response
#print(response)
   
#1 CREATE AN IAM USER

#2 Attach a Policy to a User

#response = iam.attach_user_policy(
#    UserName='test-user',
#    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
#)

#print(response)

#Uses attach_user_policy() to attach an existing AWS-managed policy to a user.
#The PolicyArn is the Amazon Resource Name (ARN) for the predefined AmazonS3ReadOnlyAccess policy.

#2 Attach a Policy to a User

#3 Create an IAM Role

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"Service": "ec2.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
}

#Define trust policy (Allows EC2 to assume the role)

#response = iam.create_role(
#    RoleName='EC2_S3_Access_Role',
#    AssumeRolePolicyDocument=json.dumps(trust_policy)
#)

#print(response)

#Creates an IAM role with create_role()
#The AssumeRolePolicyDocument defines the trust relationship allowing EC2 instances to assume the role.

#3 Create an IAM Role

#4 Attach a Policy to a Role

response = iam.attach_role_policy(
    RoleName='EC2_S3_Access_Role',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess'
)

print(response)

#Uses attach_role_policy() to grant full S3 access to the IAM role.

#4 Attach a Policy to a Role

#5 PROGRAM TO GET LIST OF EXISTING IAM USERS

response = iam.list_users()

for user in response['Users']:
    print(user['UserName'])

#Calls list_users() to retrieve all IAM users.

#5 PROGRAM TO GET LIST OF EXISTING IAM USERS

#6 Delete an IAM User

#response = iam.delete_user(UserName='test-user')

#print(response)

#Uses delete_user() to remove the IAM user.

#6 Delete an IAM User

#7 Create an IAM Group

#response = iam.create_group(GroupName='Security_Engineers')

#print(response)

#Calls create_group() to create an IAM group named Software Engineers.

#7 Create an IAM Group

#8 Add a User to a Group

#response = iam.add_user_to_group(
#    GroupName='Security_Engineers',
#    UserName='test-user'
#)

#print(response)

#Calls add_user_to_group() to associate test-user with Security_Engineers.

#8 Add a User to a Group

#9 Attach a Policy to a Group

#response = iam.attach_group_policy(
#    GroupName='Security_Engineers',
#    PolicyArn='arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess'
#)

#print(response)

#Calls attach_group_policy() to allow all users in Developers to have read-only access to EC2.

#9 Attach a Policy to a Group

#10 Create an IAM Policy

#policy_document = {
#    "Version": "2012-10-17",
#    "Statement": [
#        {
#            "Effect": "Allow",
#            "Action": "s3:ListBucket",
#            "Resource": "arn:aws:s3:::my-bucket"
#        }
#    ]
#}

#response = iam.create_policy(
#    PolicyName='S3ReadOnlyPolicy',
#    PolicyDocument=json.dumps(policy_document)
#)

#print(response)

#Uses create_policy() to define a new policy with S3 ListBucket permissions.
#The policy applies to my-bucket.

#10 Create an IAM Policy

#11 Get IAM User Details

#response = iam.get_user(UserName='test-user')

#print(response)

#Calls get_user() to fetch IAM user details like ARN, creation date, and attached policies.

#11 Get IAM User Details

#12 List Attached Policies for a User

#response = iam.list_attached_user_policies(UserName='test-user')

#for policy in response['AttachedPolicies']:
#    print(policy['PolicyName'], policy['PolicyArn'])

#Uses list_attached_user_policies() to fetch all policies assigned to test-user.

#12 List Attached Policies for a User

#13 Detach a Policy from a User

#response = iam.detach_user_policy(
#    UserName='test-user',
#    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
#)

#print(response)

#Calls detach_user_policy() to remove an IAM policy from a user.

#13 Detach a Policy from a User

#14 Delete an IAM Group

#response = iam.delete_group(GroupName='Security_Engineers')

#print(response)

#Uses delete_group() to remove an IAM group.
#Ensure all users are removed before deleting.

#14 Delete an IAM Group

#15 List IAM Roles

response = iam.list_roles()

for role in response['Roles']:
    print(role['RoleName'])

#Calls list_roles() to get all IAM roles.
#Iterates and prints role names.

#15 List IAM Roles

#16 Delete an IAM Role

#response = iam.delete_role(RoleName='EC2_S3_Access_Role2')

#print(response)

#Calls delete_role() to remove an IAM role.
#Ensure no policies are attached before deleting.

#16 Delete an IAM Role

#17 Create an IAM Access Key

#response = iam.create_access_key(UserName='test-user')

#print(response['AccessKey'])

#Calls create_access_key() to generate credentials.
#Returns AccessKeyId and SecretAccessKey.

#17 Create an IAM Access Key

#18 Update an IAM User Name

#response = iam.update_user(
#    UserName='test-user',
#    NewUserName='new-user'
#)

#print(response)

#Calls update_user() to rename an existing IAM user.
#Ensure no active sessions for the old user before renaming

#18 Update an IAM User Name

#19 List IAM Group Members

response = iam.get_group(GroupName='Security_Engineers')

for user in response['Users']:
    print(user['UserName'])

#Uses get_group() to fetch all users belonging to the Developers IAM group.

#19 List IAM Group Members

#20 List All IAM Policies

response = iam.list_policies(Scope='Local')  # 'Local' for customer-managed policies

for policy in response['Policies']:
    print(policy['PolicyName'], policy['Arn'])

#Calls list_policies() with Scope='Local' to get only custom IAM policies.
#Use Scope='AWS' to fetch AWS-managed policies.

#20 List All IAM Policies

#21 List Inline Policies for a User

response = iam.list_user_policies(UserName='new-user')

for policy in response['PolicyNames']:
    print(policy)

#Calls list_user_policies() to retrieve inline policies attached to a user.

#21 List Inline Policies for a User

#22 Delete an Inline Policy from a User

#response = iam.delete_user_policy(
#    UserName='new-user',
#    PolicyName='S3ReadOnlyPolicy'
#)

#print(response)

#Calls delete_user_policy() to remove a custom inline policy from a user.
#Inline policies are embedded, unlike managed policies, which are reusable.

#22 Delete an Inline Policy from a User

#23 Get IAM Account Summary

response = iam.get_account_summary()

for key, value in response['SummaryMap'].items():
    print(f"{key}: {value}")

#Calls get_account_summary() to retrieve IAM limits and usage, such as: Number of users, Number of groups and Number of IAM roles

#23 Get IAM Account Summary

#24 Delete an IAM Policy

#response = iam.delete_policy(
#    PolicyArn='arn:aws:iam::084375561193:policy/S3ReadOnlyPolicy'
#)

#print(response)

#Calls delete_policy() to remove a customer-managed IAM policy.
#Ensure it's not attached to any user, role, or group before deletion.

#24 Delete an IAM Policy

#25 Get IAM Role Details

response = iam.get_role(RoleName='EC2_S3_Access_Role')

print(response['Role'])

#Calls get_role() to fetch details like trust policy, role ARN, and permissions

#25 Get IAM Role Details

#26 Get IAM Policy Details

response = iam.get_policy(
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)

print(response['Policy'])

#Calls get_policy() to fetch details about an IAM policy, such as ARN, Policy type (AWS-managed or customer-managed)

#26 Get IAM Policy Details

#27 Get IAM Policy Document (JSON Representation)

response = iam.get_policy_version(
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess',
    VersionId='v1'
)

print(response['PolicyVersion']['Document'])

#Calls get_policy_version() to get the JSON document of an IAM policy.
#Useful for auditing IAM permissions.

#27 Get IAM Policy Document (JSON Representation)

#28 Delete an IAM Login Profile

#response = iam.delete_login_profile(UserName='new-user')

#print(response)

#Calls delete_login_profile() to disable AWS Console login for a user.

#28 Delete an IAM Login Profile

#29 List IAM Account Alias

response = iam.list_account_aliases()

for alias in response['AccountAliases']:
    print(alias)

#Calls list_account_aliases() to retrieve human-readable AWS account aliases.
#Useful for branding (e.g., my-company-account).

#29 List IAM Account Alias

#30 Set IAM Account Alias

#response = iam.create_account_alias(AccountAlias='my-company-account')

#print(response)

#Calls create_account_alias() to set a human-friendly name for the AWS account.

#30 Set IAM Account Alias

#31 Remove IAM Account Alias

#response = iam.delete_account_alias(AccountAlias='my-company-account')

#print(response)

#Calls delete_account_alias() to remove an AWS friendly name.

#31 Remove IAM Account Alias

#32 Generate IAM Credential Report

response = iam.generate_credential_report()
print(response)

#Calls generate_credential_report() to audit IAM users and credentials.
#Useful for compliance checks.

#32 Generate IAM Credential Report

#33 Get IAM Credential Report

response = iam.get_credential_report()
print(response['Content'].decode('utf-8'))

#Calls get_credential_report() to fetch IAM security details.
#Report includes password age, MFA usage, and access key rotation.

#33 Get IAM Credential Report