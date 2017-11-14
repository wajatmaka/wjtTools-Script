import requests, json
from prettytable import PrettyTable


url = 'https://bitbucket.org/api/1.0/user/'
headers = {'Content-Type': 'application/json'}

r = requests.get(url, auth=('wajatmaka', '228844@galuh'), headers=headers)
print(r.status_code)


hasil = json.loads(r.text)
print(json.dumps(hasil, indent=4, sort_keys=True))

print("Print In Tables Repositories")

t = PrettyTable(['CREATED ON','OWNER','LOGO','STATE'])

for x in hasil['repositories']:
    a = x['created_on']
    b = x['owner']
    c = x['logo']
    d = x['state']
    t.add_row([a,b,c,d])
print(t)





