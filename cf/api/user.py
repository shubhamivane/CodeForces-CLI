import api

def user_profile(user_handle):
    """ Printing user profile from Codeforces """
    end_point_url = 'https://codeforces.com/api/user.info?handles={}'.format(user_handle)
    json_response, error = api.call_api(end_point_url)
    if not json_response :
        return None, error
    else:
        user = json_response[0]
        user['name'] = user['firstName'].title() + ' ' + user['lastName'].title()
        del user['firstName']
        del user['lastName']
        del user['registrationTimeSeconds']
        del user['lastOnlineTimeSeconds']
        del user['city']
        del user['avatar']
        del user['titlePhoto']
        return user, error

if __name__ == '__main__':
    print(user_profile('ivane_shubham'))
    