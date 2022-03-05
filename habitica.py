import os,json
import requests
from requests.auth import HTTPDigestAuth
login=open("acesso.json", "r")
lg=login.read()
login.close()
acesso=json.loads(lg)
exportar="https://habitica.com/export/userdata.json"
auth_headers = {'x-api-user': acesso['ID_Do_Usuario'], 'x-api-key':acesso['API_Token']}
r = requests.get(exportar, headers=auth_headers)
f=open(acesso['diretorio'],'w')
f.write(json.dumps(r.json(),indent=4, sort_keys=False))
f.close()
