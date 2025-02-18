import boto3
import json

#Import all the modules and libraries. boto3 is a module used to interact with AWS. 

from botocore.exceptions import ClientError

#1 PROGRAM TO GET LIST OF EXISTING IAM USERS

aws_management_console = boto3.session.Session(profile_name="default")

#Open management console. It's a variable. Using AWS config default profile was created. 

iam_console = aws_management_console.resource('iam')

#Opening iam console from management console. Resource IAM. 

for each_user in iam_console.users.all():

    #accessing all users from IAM console

    print (each_user.name)

    #printing all the users name

#1 PROGRAM TO GET LIST OF EXISTING IAM USERS

#2 IAM USERS LIST WITH RESOURCE OBJECTS

iam_console_resource = aws_management_console.resource ('iam') #resource object

for each_user in iam_console_resource.users.all():
    print (each_user.name)

#2 IAM USERS LIST WITH RESOURCE OBJECTS

#3 IAM USERS LIST WITH CLIENT OBJECTS

iam_console_client = aws_management_console.client('iam') #client object

for user in iam_console_client.list_users()['Users']:
    print(user['UserName'])

#3 IAM USERS LIST WITH CLIENT OBJECTS

#3 CREATE AN IAM USER

iam = boto3.client("iam")

#boto3.client() is a method provided by the Boto3 library (the AWS SDK for Python) that creates a client object for a specific AWS service. The client() method is used to interact with AWS services, allowing you to make API requests to the service. By passing "iam" to boto3.client(), you're specifying that you want to interact with IAM.

#response = iam.create_user(UserName="sskaluskar")

#iam.create_user(UserName=username) is a method call on the iam object, which is an instance of the Boto3 IAM client. UserName=username is a keyword argument that is passed to the create_user() function. The username variable holds the value of the name you want to assign to the new IAM user. response is a variable that stores the response object returned by the create_user() function.

#print(response)
   
#3 CREATE AN IAM USER

#4 Attach a Policy to a User

response = iam.attach_user_policy(
    UserName='sskaluskar',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)

#print(response)

#4 Attach a Policy to a User

#4 Create an IAM Role

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

response = iam.create_role(
    RoleName='EC2_S3_Access_Role',
    AssumeRolePolicyDocument=json.dumps(trust_policy)
)

print(response)

#4 Create an IAM Role
