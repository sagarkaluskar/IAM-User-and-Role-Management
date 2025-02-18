import boto3
import json

#Import all the modules and libraries. boto3 is a module used to interact with AWS. 

from botocore.exceptions import ClientError

iam = boto3.client("iam")

#boto3.client() is a method provided by the Boto3 library (the AWS SDK for Python) that creates a client object for a specific AWS service. The client() method is used to interact with AWS services, allowing you to make API requests to the service. By passing "iam" to boto3.client(), you're specifying that you want to interact with IAM.

#1 CREATE AN IAM USER

#response = iam.create_user(UserName="test-user")

#iam.create_user(UserName=username) is a method call on the iam object, which is an instance of the Boto3 IAM client. UserName=username is a keyword argument that is passed to the create_user() function. The username variable holds the value of the name you want to assign to the new IAM user. response is a variable that stores the response object returned by the create_user() function.

#print(response)

#Initializes an IAM client.
#Calls create_user() to create a new IAM user named test-user.
   
#1 CREATE AN IAM USER

#2 Attach a Policy to a User

response = iam.attach_user_policy(
    UserName='test-user',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)

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

response = iam.create_group(GroupName='Security_Engineers')

print(response)

#Calls create_group() to create an IAM group named Software Engineers.

#7 Create an IAM Group

#8 Create an IAM Group