import requests

r = requests.get('http://localhost:5000/api?action=phone&name=Urban')
r.text

n = requests.get('http://localhost:5000/api?action=name&phone=0435-4355438')
n.text

def get_phone(name):
    if name == "Urban":
        return r.text

def get_name(phone):
    if phone == "0435-4355438":
        return n.text
