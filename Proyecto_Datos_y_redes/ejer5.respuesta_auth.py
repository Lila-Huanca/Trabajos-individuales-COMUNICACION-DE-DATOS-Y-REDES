import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS Clients
region_name = 'us-west-2'  # Especifica la región adecuada aquí
s3_client = boto3.client('s3', region_name=region_name)
lambda_client = boto3.client('lambda', region_name=region_name)
cloudwatch_client = boto3.client('logs', region_name=region_name)

def create_lambda_function(function_name, role_arn, handler, code_zip_path):
    try:
        with open(code_zip_path, 'rb') as f:
            zipped_code = f.read()
        
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.8',
            Role=role_arn,
            Handler=handler,
            Code=dict(ZipFile=zipped_code),
            Timeout=300
        )
        
        logger.info(f"Lambda function {function_name} created successfully")
        return response['FunctionArn']
    except Exception as e:
        logger.error(f"Error creating Lambda function: {e}")

def create_cloudwatch_rule(rule_name, event_pattern):
    try:
        response = cloudwatch_client.put_rule(
            Name=rule_name,
            EventPattern=event_pattern,
            State='ENABLED'
        )
        
        logger.info(f"CloudWatch rule {rule_name} created successfully")
        return response['RuleArn']
    except Exception as e:
        logger.error(f"Error creating CloudWatch rule: {e}")

def add_lambda_permission(function_name, rule_arn):
    try:
        response = lambda_client.add_permission(
            FunctionName=function_name,
            StatementId=f'{function_name}-InvokePermission',
            Action='lambda:InvokeFunction',
            Principal='events.amazonaws.com',
            SourceArn=rule_arn
        )
        
        logger.info(f"Permission added to Lambda function {function_name}")
    except Exception as e:
        logger.error(f"Error adding permission to Lambda function: {e}")

def main():
    function_name = 'S3BackupCreator'
    role_arn = 'arn:aws:iam::account-id:role/lambda-execution-role'
    handler = 'backup.handler'
    code_zip_path = 'backup.zip'
    
    # Create Lambda function
    lambda_arn = create_lambda_function(function_name, role_arn, handler, code_zip_path)
    
    rule_name = 'S3BackupRule'
    event_pattern = {
        "source": ["aws.s3"],
        "detail-type": ["Object Created (All)"],
        "detail": {
            "bucket": {
                "name": ["my-bucket"]
            }
        }
    }
    
    # Create a CloudWatch rule
    rule_arn = create_cloudwatch_rule(rule_name, event_pattern)
    
    # Add permission to invoke the Lambda function
    add_lambda_permission(function_name, rule_arn)

if __name__ == '__main__':
    main()
