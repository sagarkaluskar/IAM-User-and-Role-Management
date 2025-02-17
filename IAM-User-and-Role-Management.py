import boto3

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


