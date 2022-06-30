import requests



def get_phone(get_phone):
    phone = requests.get(f'http://localhost:5000/api?action=phone&name={get_phone}')
    return phone.text

def get_name(get_name):
    name = requests.get(f'http://localhost:5000/api?action=name&phone={get_name}')
    return name.text
