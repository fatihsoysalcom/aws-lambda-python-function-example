import json

def lambda_handler(event, context):
    """
    This is a simple AWS Lambda function written in Python.
    It demonstrates a basic handler that processes an incoming event.
    In the context of the DVA-C03 exam, understanding Lambda functions,
    their event structures, and how to write handler logic is crucial.
    """

    # The 'event' object contains data passed to the Lambda function.
    # The structure of 'event' depends on the trigger (e.g., API Gateway, S3).
    print(f"Received event: {json.dumps(event)}")

    # Example: Extracting a value from the event if it exists.
    # This is a common pattern for processing input data.
    name = event.get('name', 'World')

    # Constructing a response object.
    # For API Gateway integrations, this response format is expected.
    response_body = {
        'message': f'Hello, {name} from AWS Lambda!',
        'input_event': event
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response_body)
    }

# Example of how to test this locally (optional, for development)
if __name__ == '__main__':
    # Simulate an API Gateway event
    test_event = {
        'httpMethod': 'GET',
        'path': '/hello',
        'queryStringParameters': {
            'name': 'Developer'
        },
        'body': None,
        'requestContext': {},
        'headers': {},
        'stageVariables': {}
    }
    result = lambda_handler(test_event, None)
    print("\n--- Local Test Output ---")
    print(json.dumps(result, indent=2))

    # Simulate a different event structure
    test_event_2 = {
        'name': 'Tester',
        'data': [1, 2, 3]
    }
    result_2 = lambda_handler(test_event_2, None)
    print("\n--- Another Local Test Output ---")
    print(json.dumps(result_2, indent=2))
