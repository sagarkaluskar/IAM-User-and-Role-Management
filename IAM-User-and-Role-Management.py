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

#3 CREATE AN IAM USER

iam = boto3.client("iam")

#boto3.client() is a method provided by the Boto3 library (the AWS SDK for Python) that creates a client object for a specific AWS service. The client() method is used to interact with AWS services, allowing you to make API requests to the service. By passing "iam" to boto3.client(), you're specifying that you want to interact with IAM.

def create_iam_user(username):
    
    #def is a keyword used to define a function in Python. create_iam_user is the name of the function. username is a parameter of the function. It represents the input that the function requires when it is called. In this case, the function expects a string value to represent the IAM user’s name. 
    
    response = iam.create_user(UserName="skaluskar")

    #iam.create_user(UserName=username) is a method call on the iam object, which is an instance of the Boto3 IAM client. UserName=username is a keyword argument that is passed to the create_user() function. The username variable holds the value of the name you want to assign to the new IAM user. response is a variable that stores the response object returned by the create_user() function.

    print(f"User {username} created successfully: {response}")

    #It is an example of an f-string (formatted string) in Python. An f-string is a feature introduced in Python 3.6 to embed expressions inside string literals. The syntax for an f-string is to prefix the string with the letter f and use curly braces {} to include expressions whose results will be evaluated and inserted into the string at runtime. {expression}: Any valid Python expression inside the curly braces is evaluated at runtime, and its value is inserted into the string.

#3 CREATE AN IAM USER

