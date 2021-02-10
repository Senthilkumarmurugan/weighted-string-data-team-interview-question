def getAccessToken(tokenUrl: str, clientId: str, clientSecret: str , data: dict) -> dict:
    """ Function to get accesstoken """
    
    access_token_response = requests.post(tokenUrl, data=data, verify=True, allow_redirects=False, auth=(clientId, clientSecret))
    tokens = json.loads(access_token_response.text)
    api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
    api_call_headers['Content-Type']='application/json'
    return api_call_headers
