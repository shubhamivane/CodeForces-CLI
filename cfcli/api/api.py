import requests
import json

def call_api(api_end_point):
    """ Request given API endpoint and return json result """
    try:
        response = requests.get(api_end_point)
        response_data = None
        if response.status_code == 200:
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
