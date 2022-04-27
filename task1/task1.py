import json
from urllib.request import urlopen

with urlopen("https://openx.com/sellers.json") as response: #json file with buyers and sellers
    source = response.read()
    
data = json.loads(source)

count = 0

for value in data['sellers']:
    if value['seller_id']:
        count += 1
    domain = value['domain']
    name = value['name']
    seller_type = value['seller_type']
    print(name,'---',domain, '--- ', seller_type) #The name of company, domain and type of seller
print('The depth of Supply Chain: ', count, 'available sellers') #The amount of sellers that are in Supply Chain tree
    