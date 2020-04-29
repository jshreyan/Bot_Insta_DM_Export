import json
from datetime import datetime
from datetime import timedelta
import traceback
import os

MYUSERNAME = 'shreyan_jadhavs'
PERSONAL_CHAT = None#'abc_official'
directory = 'instagram'

chatmsg = ''
chat = []
participantstype = ''


def load_file():
    messages_json = ''
    try:
        f = open("messages.json", "r", encoding="utf8")
        txt = f.read()
        messages_json = json.loads(txt)
    except:
        print('Error opening messages file. Please check file path.')

    return messages_json

def json_to_pylist(messages_json):    
    for i in range(0,len(messages_json)):
        if PERSONAL_CHAT is not None:
            try:
                if PERSONAL_CHAT in messages_json[i]['participants'] and len(messages_json[i]['participants'])==2:
                    try:
                        username = messages_json[i]['participants'].copy()
                        username.remove(MYUSERNAME)
                        participantstype = username[0]#+'_'+str(i)       
                    except:
                        participantstype = messages_json[i]['participants'][1]
                    participants = 'PARTICIPANTS: '+', '.join(messages_json[i]['participants'])
                    chat.append([participantstype,participants,[messages_json[i]['conversation']]])                
            except:
                print('Error in json_to_pylist function1:'+participants)
                #traceback.print_exc()
        else:
            try:
                if len(messages_json[i]['participants'])>2:
                    participantstype = 'GROUP_'+str(i)
                else:
                    try:
                        username = messages_json[i]['participants'].copy()
                        username.remove(MYUSERNAME)
                        participantstype = username[0]#+'_'+str(i)
                    except:
                        participantstype = messages_json[i]['participants'][1]
                
                participants = 'PARTICIPANTS: '+', '.join(messages_json[i]['participants'])
                chat.append([participantstype,participants,[messages_json[i]['conversation']]])
            except:
                print('Error in json_to_pylist function2:'+participants)
                #traceback.print_exc()
    return chat

def make_readable(chat):
    chat_data = []
    for perchat in reversed(chat):
        chatmsg = perchat[1]+'\n\n'
        chatx = perchat[2][0]
        for x in range(0,len(perchat[2][0])):
            j = len(chatx)-x-1
            chattext = ''
            try:
                if 'media_owner' in chatx[j]:
                    chattext = chatx[j]['media_owner']+' - '+chatx[j]['media_share_caption']+' - URL: '+chatx[j]['media_share_url']
                if 'story_share' in chatx[j]:
                    chattext = chatx[j]['story_share']+' - '+str(chatx[j]['text'])
                if 'media' in chatx[j]:
                    chattext = chatx[j]['media']
                if 'text' in chatx[j]:
                    chattext = chatx[j]['text']
                if 'heart' in chatx[j]:
                    chattext = chatx[j]['heart']
                    
                msgtime = datetime.strptime(chatx[j]['created_at'][:19].replace('T',' '), '%Y-%m-%d %H:%M:%S') + timedelta(hours=5.5)
                chatmsg =  chatmsg+'['+str(msgtime)+']'+' '+str(chatx[j]['sender'])+': '+str(chattext)+'\n'
                #print(chatx[j]['created_at'],(chattext))
            except:
                print('Error in make_readable function:'+chatx[j])
                #traceback.print_exc()
        export_to_file(perchat[2][0], perchat[0], chatmsg)

def export_to_file(chat_msg_lst, chat_name, chat_msg):
    try:
        if len(chat_msg_lst) > 5:
            if not os.path.exists(directory):
                os.makedirs(directory)
            f = open(directory+'\\'+chat_name+'.txt', "a+", encoding="utf8")
            f.write(chat_msg)
            f.close()
    except:
        print('Error in export_to_file function')
        
          
messages_json = load_file()
chat_pylist = json_to_pylist(messages_json)
make_readable(chat_pylist)

