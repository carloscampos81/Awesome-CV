import msal
import webbrowser
import  requests 
from msal import PublicClientApplication

APPLICATION_ID = 'b3a1fdb1-bc01-44e3-8919-6024c6a15da9'
CLIENT_SECRET = 'VE.8Q~cdOoGhvM7WT22Qau5GTBoJ050LoanUzay-'
authority_url = 'https://login.microsoftonline.com/consumers/'
base_url = 'https://graph.microsoft.com/v1.0/'


SCOPES  = ['User.Read', 'User.Export.All']

client_instance = msal.ConfidentialClientApplication(
    client_id=APPLICATION_ID,
    client_credential=CLIENT_SECRET,
    authority=authority_url
)

authorization_request_url = client_instance.get_authorization_request_url(SCOPES)
print(authorization_request_url)
webbrowser.open(authorization_request_url, new=True)

authorization_code = 'M.R3_BAY.0753bc4b-5eec-fcf1-fa6f-4821b68ada87'

access_token = client_instance.acquire_token_by_authorization_code(
    code=authorization_code,
    scopes=SCOPES
)

access_token_id = access_token['access_token']
headers = {'Autorization': 'Bearer' + access_token_id}

endpoint = base_url + 'me'
response = requests.get(endpoint, headers=headers)
print(response)
print(response.json())