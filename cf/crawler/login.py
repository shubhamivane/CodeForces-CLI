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
    
def login(username, password):
    user_data['handleOrEmail'] = username
    user_data['password'] = password
    try:
        with requests.Session() as session:
            url = 'https://codeforces.com/enter'
            response = session.get(url, headers = headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            soup_result = soup.find('input', {'name' : 'csrf_token'})
            if not soup_result is None:
                user_data['csrf_token'] = soup_result['value']
                try:
                    response = session.post(url, data = urlencode(user_data), headers = headers)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    soup_result = soup.find('a', {'href': '/profile/{0}'.format(username)})
                    if not soup_result is None:
                        return session, ''
                    else:
                        return None, 'Invalid Credentials'
                except requests.exceptions.Timeout as error:
                    return None, error
                except requests.exceptions.TooManyRedirects as error:
                    return None, error
                except requests.exceptions.HTTPError as error:
                    return None, error
            else:
                return None, 'Couldn\'t get CSRF Token'
    except requests.exceptions.Timeout as error:
        return None, error
    except requests.exceptions.TooManyRedirects as error:
        return None, error
    except requests.exceptions.HTTPError as error:
        return None, error

def verify_credentials(username, password):
    session, error = login(username, password)
    if session is None:
        return False, error
    else:
        return True, ''

if __name__ == "__main__":
    print(login('ivane_shubham', 'shubham@22403354'))