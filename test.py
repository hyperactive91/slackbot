from slackclient import SlackClient
import time
import json
import config

#slack_token = 'xoxb-1161223414533-1168798704756-zXsltsnI5Uza37P12wdLrFhi'

sc =  SlackClient(config.token)

time.sleep(1)



#Get bot id
def getBotID(botname):
    msg = sc.api_call("users.list").decode('utf-8')
    msg2=json.loads(msg)
    users=msg2['members']
    for user in users:
        if 'name' in user and user.get('deleted') == False and botname in user.get('name'):
            return user.get('id')
        # print(user)

#create read and write to slack methods
def postToSlack(channel, message):
    return sc.api_call("chat.postMessage", channel=channel, text=message, as_user=True)

def readAndReply(msg, botId):
    if('type' in msg[0] and msg[0].get('type') == 'message'):
        # print(msg[0].get('text'))
        channel = msg[0].get('channel')
        user = msg[0].get('user')
        if(user == botId):
            return ""
        rep = 'I got ' + msg[0].get('text')
        if(msg[0].get('text') == 'STOP'):
            rep = 'Goodbye'
        postToSlack(channel=channel , message = rep)
        return msg[0].get('text')
    else:
        return ""

botId = getBotID('bbcbot')

if sc.rtm_connect():
    message=''
    while message != 'STOP':
        msg = sc.rtm_read()
        print(msg)
        if(str(msg) != '[]' and str(msg) != "[{'type': 'hello'}]"):
            message = readAndReply(msg, botId)
            print(message)
        time.sleep(1)

# # postToSlack("bots", "hello world")