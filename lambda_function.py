import requests
import requests.auth

def lambda_handler(event, context):   
   
    response = get_token(event["queryStringParameters"]["code"])
    return response


def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth("YOUR_CLIENT_ID", "YOUR_CLIENT_Secret")
    post_data = {"grant_type": "authorization_code",
                "code": code,
                "redirect_uri": "YOUR_AWS_FUNCTION_URI"}

    response = requests.post("https://zoom.us/oauth/token",
                            auth=client_auth,
                            data=post_data)
    token_json = response.json()
    
    return token_json['access_token']
