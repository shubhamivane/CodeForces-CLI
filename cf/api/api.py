import requests
import json

def call_api(api_end_point):
    """ Request given API endpoint and return json result """
    try:
        response = requests.get(api_end_point)
        response_data = None
        response_data = response.content.decode('utf-8')
        response_data = json.loads(response_data)
        if response_data['status'] == 'OK':
            return response_data['result'], 'Success'
        else:
            return None, response_data['comment']
    except requests.exceptions.Timeout as error:
        return None, error
    except requests.exceptions.TooManyRedirects as error:
        return None, error
    except requests.exceptions.HTTPError as error:
        return None, error

if __name__ == '__main__':
    end_point_url = 'https://codeforces.com/api/user.info?handles=ivane_shubha'
    print(call_api(end_point_url))