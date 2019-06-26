import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

user_data = {
        'action'          : 'enter',
        'ftaa'            : 'ew6y8twoe3rumayx14',
        'bfaa'            : '705d779aedd5ebd90b3e6609bc76c1ffi',
        'remember'        : 'on',
        '_tta'            : '376'
}

headers = {
        'Connection'  : 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host'        : 'codeforces.com',
        'Origin'      : 'https://codeforces.com',
        'Referer'     : 'https://codeforces.com/enter',
        'User-Agent'  : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'        
}

with requests.Session() as session:
    url = 'https://codeforces.com/enter'
    response = session.get(url, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    user_data['csrf_token'] = soup.find('input', {'name' : 'csrf_token'})['value']
    response = session.post(url, data = urlencode(user_data), headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    response = session.get('https://codeforces.com/profile/ivane_shubham')
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())    

def get_CSRF_token(url, headers):
	try:
		response = requests.get(url, headers)
		soup = BeautifulSoup(response.content, 'html.parser')
		csrf_token = soup.find('input', {'name': 'csrf_token'})
		if csrf_token == None:
			return False, "Could not get token"
		else:
			return True, csrf_token['value']
	except 

def verify_user_credentials(username, password):
    user_data['handleOrEmail'] = username
    user_data['password'] = password
    with requests.Session() as session:
        url = 'https://codeforces.com/enter'
        user_data['csrf_token'] = get_CSRF_token(url, headers)