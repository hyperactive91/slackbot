from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os
import time
import slack
import json
import config



sc=(SlackClient('config.token'))


print(sc.api_call('users.list'))
#

if sc.rtm_connect():
        while True:   
            print (sc.rtm_read()[0].get('type'))
            time.sleep(1)

                
                # if (sc.rtm_read()).json['type']=='hi':
                #     sc.api_call(
                #     "chat.postMessage",
                #     channel="general",
                #     text="hello... such a nice day!!!"
                #     )
                
else:
    print ("Connection Failed, invalid token?")


# def getBotID():
#     api_call=sc.api_call("users.list")
#     users=api_call("members")
#     for user in users:
#         print(user)

        
# getBotID()
#print(sc.rtm_connect())
# constants