import boto3

def create_user_pool(client_name):
    client = boto3.client('cognito-idp')
    response = client.create_user_pool(
        PoolName=client_name,
        AutoVerifiedAttributes=[
            'email'
        ]
    )
    return response['UserPool']['Id']

def create_user_pool_client(user_pool_id, client_name):
    client = boto3.client('cognito-idp')
    response = client.create_user_pool_client(
        UserPoolId=user_pool_id,
        ClientName=client_name,
        GenerateSecret=False
    )
    return response['UserPoolClient']['ClientId']

def main():
    user_pool_id = create_user_pool('MyUserPool')
    user_pool_client_id = create_user_pool_client(user_pool_id, 'MyUserPoolClient')
    
    print("User Pool ID:", user_pool_id)
    print("User Pool Client ID:", user_pool_client_id)

if __name__ == "__main__":
    main()
