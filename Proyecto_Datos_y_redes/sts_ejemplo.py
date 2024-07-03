import boto3

def assume_role(role_arn, role_session_name):
    client = boto3.client('sts')
    response = client.assume_role(
        RoleArn=role_arn,
        RoleSessionName=role_session_name
    )
    return response['Credentials']

def main():
    role_arn = 'arn:aws:iam::123456789012:role/MyRole'
    role_session_name = 'MySession'
    
    credentials = assume_role(role_arn, role_session_name)
    
    print("Access Key:", credentials['AccessKeyId'])
    print("Secret Access Key:", credentials['SecretAccessKey'])
    print("Session Token:", credentials['SessionToken'])

if __name__ == "__main__":
    main()
