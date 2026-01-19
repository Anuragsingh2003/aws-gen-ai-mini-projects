import json
#1. import boto3
import boto3
#2 create client connection with bedrock
client_bedrock_knowledgebase = boto3.client('bedrock-agent-runtime')
def lambda_handler(event, context):
    """
    AWS Lambda handler function that processes user prompts using Amazon Bedrock Knowledge Base.
    This function retrieves information from a knowledge base and generates responses using 
    Claude AI model through the Bedrock API.
    Parameters:
    -----------
    event : dict
        The event object passed to Lambda containing:
        - 'prompt' (str): The user's input question/prompt to be processed
    context : LambdaContext
        The Lambda context object containing metadata about the invocation.
        (Currently unused in this implementation)
    Returns:
    --------
    dict
        A response object containing:
        - 'statusCode' (int): HTTP status code (200 for success)
        - 'body' (str): The generated response text from the knowledge base
    Logic & Steps:
    ---------------
    1. Extract the user prompt from the event dictionary
    2. Log the prompt to CloudWatch for debugging
    3. Call Bedrock's retrieve_and_generate API with:
       - User prompt as input text
       - Knowledge Base ID: 'O41RCIQ46A' (configured knowledge base)
       - Model: Claude Instant v1 from us-west-2 region
    4. The API searches the knowledge base for relevant information
    5. Claude model generates a contextual response based on retrieved data
    6. Extract the generated text from the API response
    7. Return the response wrapped in HTTP 200 status with the generated text as body
    Dependencies:
    ---------------
    - client_bedrock_knowledgebase: Boto3 Bedrock client (must be initialized before calling)
    - AWS credentials with permissions for Bedrock and Knowledge Base access
    """
    #3 Store the user prompt
    print(event['prompt'])
    user_prompt=event['prompt']
    # 4. Use retrieve and generate API
    client_knowledgebase = client_bedrock_knowledgebase.retrieve_and_generate(
    input={
        'text': user_prompt
    },
    retrieveAndGenerateConfiguration={
        'type': 'KNOWLEDGE_BASE',
        'knowledgeBaseConfiguration': {
            'knowledgeBaseId': 'O41RCIQ46A',
            'modelArn': 'arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-instant-v1'
                }
            })
            
    # print(client_knowledgebase)     
    #print(client_knowledgebase['output']['text'])
    #print(client_knowledgebase['citations'][0]['generatedResponsePart']['textResponsePart'])
    response_kbase_final=client_knowledgebase['output']['text']
    return {
        'statusCode': 200,
        'body': response_kbase_final
    }
    