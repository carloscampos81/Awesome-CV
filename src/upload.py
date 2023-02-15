import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

# Defina as credenciais do aplicativo
client_id = '7b1db933-1172-4a2a-b24a-012e7d47cd94'
client_secret = 'b8468386-27cd-4f38-b077-b73b1a74ef76'
redirect_uri = 'https://upload-onedrive-pythton'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

# Crie uma instância do SDK
client = onedrivesdk.get_default_client(
    client_id=client_id,
    scopes=scopes)

# Obtenha o token de acesso
auth_url = client.auth_provider.get_auth_url(redirect_uri)
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
client.auth_provider.authenticate(code, redirect_uri, client_secret)

# Faça upload do arquivo
filename = 'cv.pdf'
filepath = 'Teste'
item_name = 'cv.pdf'

returned_item = client.item(drive='me', path='/root:/' + item_name).children[filename].upload(filepath)
print('Arquivo carregado:', returned_item.id)