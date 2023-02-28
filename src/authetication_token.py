import msal
import webbrowser
import  requests 
from msal import PublicClientApplication

APPLICATION_ID = 'b3a1fdb1-bc01-44e3-8919-6024c6a15da9'
CLIENT_SECRET = 'VE.8Q~cdOoGhvM7WT22Qau5GTBoJ050LoanUzay-'
authority_url = 'https://login.microsoftonline.com/consumers/'
base_url = 'https://graph.microsoft.com/v1.0/'
SCOPES  = ['User.Read']

app = PublicClientApplication (
    APPLICATION_ID,
    authority=authority_url
)

# accounts = app.get_accounts()
# if accounts: 
#     app.acquire_token_silent(scopes=SCOPES, account=accounts)

flow = app.initiate_device_flow(scopes=SCOPES)
print(flow)
print(flow['message'])
webbrowser.open(flow['verification_uri'])

