from . import api
import datetime

def convert_sec_to_date(sec):
    """ Convert miliseconds in date i.e. Wednesday, 26 June 2019 08:05PM """
    return datetime.datetime.fromtimestamp(sec).strftime('%A, %d %B %Y %I:%M%p')


def upcoming_contest():
    """ Printing upcoming contests on Codeforces """
    end_point_url = 'https://codeforces.com/api/contest.list?gym=false'
    json_response, error = api.call_api(end_point_url)
    if not json_response is None:
        contest_list = []
        for contest in json_response:
            if contest['relativeTimeSeconds'] < 0:
                contest_list.append((contest['startTimeSeconds'], contest['name']))
            else:
                break
        if len(contest_list) > 1:
            contest_list.sort()
            contest_list = list(map(lambda contest: (contest[1], convert_sec_to_date(contest[0])), contest_list)) 
        else:
            contest_list[0][0], contest_list[0][1] = contest_list[0][1], convert_sec_to_date(contest_list[0][0])
        return contest_list, ''
    
    else:
        return None, error
    
def contest_history(username):
    end_point_url = 'https://codeforces.com/api/user.rating?handle={}'.format(username)
    json_response, error = api.call_api(end_point_url)
    if not json_response is None:
        length = len(json_response)
        contest_list = [] 
        if length == 0:
            return [], 'No contest history'
        else:
            for i in range(length-1, -1, -1):
                contest = dict()
                contest['id'] = json_response[i]['contestId']
                contest['name'] = json_response[i]['contestName']
                contest['rank'] = json_response[i]['rank']
                contest['new_rating'] = json_response[i]['newRating']
                contest['old_rating'] = json_response[i]['oldRating']
                contest_list.append(contest)
            return contest_list, ''
    else:
        return None, error

if __name__ == '__main__':
    #print(upcoming_contest())
    print(contest_history('ivane_shubham'))
    