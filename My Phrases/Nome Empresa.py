# Enter script code
# Enter script code
import requests 

url =  "https://api.invertexto.com/v1/faker?token=6070%7C1kUQFaU0SiJMqQa6oWGps81r2nfQ4Boy&fields=name&locale=pt_BR"

response = requests.get(url)
data = response.json() 

name = 'JHK ' + data['name'] + ' ME'

keyboard.send_keys(name)
keyboard.send_keys("<tab>")
keyboard.send_keys(name)
clipboard.fill_clipboard(name)