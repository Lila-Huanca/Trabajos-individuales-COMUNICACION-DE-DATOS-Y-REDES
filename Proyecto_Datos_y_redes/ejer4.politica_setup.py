import boto3
import json
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crear cliente IAM
iam_client = boto3.client('iam')

def create_policy(policy_name, policy_document):
    """
    Objetivo: Crear y aplicar políticas de IAM personalizadas que reflejen las necesidades específicas de
    seguridad de la aplicación.

    Descripción:
    • Diseña políticas de IAM que restrinjan el acceso a recursos específicos basados en roles y
      responsabilidades definidos.
    • Aplica estas políticas a grupos de usuarios y roles dentro de Amazon Cognito.
    • Realiza pruebas para asegurar que las políticas funcionan como se espera sin impedir la
      funcionalidad de la aplicación.
    """
    try:
        response = iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_document)
        )
        logger.info(f"Policy {policy_name} created successfully")
        return response['Policy']['Arn']
    except Exception as e:
        logger.error(f"Error creating policy: {e}")

def attach_policy_to_role(role_name, policy_arn):
    """
    Adjunta una política a un rol específico en IAM.
    """
    try:
        response = iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        logger.info(f"Policy {policy_arn} attached to role {role_name} successfully")
    except Exception as e:
        logger.error(f"Error attaching policy to role: {e}")

def main():
    policy_name = 'CustomSecurityPolicy'
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:ListBucket",
                    "s3:GetObject"
                ],
                "Resource": [
                    "arn:aws:s3:::example-bucket",
                    "arn:aws:s3:::example-bucket/*"
                ]
            }
        ]
    }
    
    # Crear una política personalizada IAM
    policy_arn = create_policy(policy_name, policy_document)
    if policy_arn:
        logger.info(f"Policy ARN: {policy_arn}")
        
        # Adjuntar la política a un rol específico
        role_name = 'ExampleRole'
        attach_policy_to_role(role_name, policy_arn)

if __name__ == '__main__':
    main()
