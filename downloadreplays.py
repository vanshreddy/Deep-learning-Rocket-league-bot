import requests
import os
from configparser import ConfigParser, ExtendedInterpolation
import pandas as pd
from limit import limit

API_BASE = 'https://ballchasing.com/api'
API_KEY = 'API KEY'
FILTERS = {'playlist': 'ranked-duels',
           'season': 10,
           'min-rank':'gold-3',
           'max-rank': 'platinum-3',
           'sort-by': 'replay-date',
            }


config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('PATH TO CONFIG')
paths = config['PATHS']

mode_tuple = config['VARS']['MODE'].split(',')


PAGES = 100
REPLAY_PATH = "PATH TO SAVE"
OS_PATH=paths['replay_path']
ONE_MINUTE = 3600



if not os.path.exists(OS_PATH):
    os.makedirs(OS_PATH)
    print("Created directories in replay_path")

existing = os.listdir(OS_PATH)

@limit(1,1)
def list_replays(filters):
    r = requests.get(API_BASE+'/replays', params=filters,
                     headers={'Authorization': API_KEY})
    if r.status_code != 200:
        print("FAILED")
        raise Exception('API response: {}'.format(r.status_code))

    return r.json()

def get_replay(id):
    r = requests.get(API_BASE+'/replays/'+id,
                     headers={'Authorization': API_KEY})
    return r.json()


def get_replaylist():
    id_lst = []
    page = list_replays(FILTERS)
    for r in page['list']:
        replay = get_replay(r['id'])
        print(replay['id'], " ::::::::::",len(id_lst))
        id_lst.append(replay['id'])

    print("len:", len(id_lst))
    return id_lst

def download(lst):
    for i in range(len(lst)):
        url = API_BASE+"/replays/"+lst[i]+"/file"
        r = requests.get(url, headers={'Authorization': API_KEY})
        print("downloading:",lst[i] )
        open(OS_PATH + lst[i] + '.replay', 'wb').write(r.content)
    return
@limit(1,1)
def download_v1(max_download):
    replay_log = paths['replay_log']
    replay_path = paths['replay_path']
    mode = int(mode_tuple[0])
    num_players = int(mode_tuple[1])
    data_cols = ['hash', 'download', 'map', 'match_date', 'upload_date', 'team_blue_score', 'team_orange_score'] + [
        f'p_{x}' for x in range(num_players * 2)] + [f'mmr_{x}' for x in range(num_players * 2)]
    if not os.path.exists(replay_log):
        log = pd.DataFrame(columns=data_cols)
        log.to_csv(replay_log)
        print("Created replay log")

    log = pd.read_csv(replay_log, index_col=0)
    logged = log['hash'].values
    old = 0
    new = 0
    logs = []



    flag = True
    page = list_replays(FILTERS)
    downloaded = 0
    while page['next']:
        if downloaded == max_download:
            break
        page = requests.get(page['next'], headers={'Authorization': API_KEY}).json()
        print("Page count:",page["count"])
        for r in page['list']:
            replay_name = get_replay(r['id'])
            url = API_BASE + "/replays/"+replay_name['id']+"/file"
            re = requests.get(url,headers={'Authorization': API_KEY})
            if replay_name['id'] + '.replay' not in existing:
                open(OS_PATH + replay_name['id'] + '.replay', 'wb').write(re.content)
                downloaded += 1
                print("downloading:", replay_name['id'], ":::::::::", downloaded, "::::::::::::::")

        flag = False


if __name__ == "__main__":
    download_v1(1000)
