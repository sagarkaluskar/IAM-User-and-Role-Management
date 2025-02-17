import boto3

#boto3 is a module used to interact with AWS. 

from botocore.exceptions import ClientError

#1 program to check existing IAM users

aws_management_console = boto3.session.Session(profile_name="default")

#Opening management console. It's a variable. Using AWS config default profile was created. 

iam_console = aws_management_console.resource('iam')

#Opening iam console from management console. Resource IAM. 

for each_user in iam_console.users.all():

    #accessing all users from IAM console

    print (each_user.name)

    #printing all the users name

#1 program to check existing IAM users





