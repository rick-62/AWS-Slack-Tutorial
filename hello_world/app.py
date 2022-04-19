import json

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

    url = "https://slack.com/api/chat.postMessage"

    headers = {}
    headers["Authorization"] = "Bearer xoxb-3386604110887-3424965232336-wfOVcKL86aV8cxNjxxuPgn2L"
    headers["Content-Type"] = "application/json"

    myMessage = """
    {"channel": "#using-slack-and-aws-eventbridge-to-automate-your-devops-tasks",
    "text": "Hello Again"}
    """

    try:
        resp = requests.put(url, headers=headers, json=myMessage)
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": resp.status_code,
        "body": json.dumps({
            "message": "hello rick",
            # "location": ip.text.replace("\n", "")
        }),
    }
