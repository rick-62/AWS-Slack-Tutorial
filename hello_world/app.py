import json

import boto3
import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """



    # Create our SSM Client.
    aws_client = boto3.client('ssm')


    url = "https://slack.com/api/chat.postMessage"

    headers = {}
    headers["Authorization"] = f"{aws_client.get_parameter(Name='slack-api', WithDecryption=True)['Parameter']['Value']}"
    headers["Content-Type"] = "application/json"

    myMessage = {
        "channel": "#using-slack-and-aws-eventbridge-to-automate-your-devops-tasks",
        "text": "Hello from lambda"}

    try:
        resp = requests.post(url, headers=headers, data=json.dumps(myMessage))
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": resp.status_code,
        "body": json.dumps({
            "message": f"hello from lambda: {resp.text}",
            # "location": ip.text.replace("\n", "")
        }),
    }
