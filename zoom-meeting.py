# -*- coding: utf-8 -*-
# Module: Zoom-Meeting
# Created on: 04-04-2022
# Authors: -∞WKS∞-
# Version: 1.8.0

import jwt
import requests
import json
import logging
logging.basicConfig(level=logging.DEBUG)
from time import time
 

API_KEY = 'xxxxxxxx-Your API key'
API_SEC = 'xxxxxxxx-Your API secret'
 
def generateToken():
    token = jwt.encode(
 

        {'iss': API_KEY, 'exp': time() + 5000},
 
        API_SEC,
 
        algorithm='HS256'
    )
    return token.decode('utf-8')
 

meetingdetails = {"topic": "The title of your zoom meeting",
                  "type": 2,
                  "start_time": "20xx-0x-xxTxx: xx: xx",
                  "duration": "xx",
                  "timezone": "xxx",
                  "agenda": "xxx",
 
                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }
 
 
 
def createMeeting():
    headers = {'authorization': 'Bearer ' + generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))
 
    print("\n creating zoom meeting ... \n")
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]
 
    print(
        f'\n here is your zoom meeting link {join_URL} and your \
        password: "{meetingPassword}"\n')
 
 
createMeeting()