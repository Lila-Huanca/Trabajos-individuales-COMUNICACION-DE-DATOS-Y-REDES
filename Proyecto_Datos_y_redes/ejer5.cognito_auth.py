import boto3
from warrant import Cognito

USER_POOL_ID = 'your_user_pool_id'
CLIENT_ID = 'your_client_id'
REGION = 'your_region'

def authenticate_user(username, password):
    u = Cognito(USER_POOL_ID, CLIENT_ID, username=username, user_pool_region=REGION)
    u.authenticate(password=password)
    return u

def main():
    username = 'testuser'
    password = 'TestPassword123!'
    
    user = authenticate_user(username, password)
    
    print("Access Token:", user.access_token)
    print("ID Token:", user.id_token)
    print("Refresh Token:", user.refresh_token)

if __name__ == "__main__":
    main()
