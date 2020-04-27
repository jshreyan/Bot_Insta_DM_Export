import json
from datetime import datetime
from datetime import timedelta
import traceback

f = open("C:/messages.json", "r", encoding="utf8")
txt = f.read()
y = json.loads(txt)
messages = y

personalchat = None#'iam_prerana'
chatmsg = ''
chat = []
participantstype = ''

for i in range(0,len(y)):
    if personalchat is not None:
        try:
            if personalchat in y[i]['participants'] and len(y[i]['participants'])==2:
                try:
                    username = y[i]['participants'].copy()
                    username.remove('shreyan_jadhav')
                    participantstype = username[0]#+'_'+str(i)       
                except:
                    participantstype = y[i]['participants'][1]
                participants = 'PARTICIPANTS: '+', '.join(y[i]['participants'])
                chat.append([participantstype,participants,[y[i]['conversation']]])                
        except:
            None
    else:
        try:
            if len(y[i]['participants'])>2:
                participantstype = 'GROUP_'+str(i)
            else:
                try:
                    username = y[i]['participants'].copy()
                    username.remove('shreyan_jadhav')
                    participantstype = username[0]#+'_'+str(i)       
                except:
                    participantstype = y[i]['participants'][1]
            
            participants = 'PARTICIPANTS: '+', '.join(y[i]['participants'])
            chat.append([participantstype,participants,[y[i]['conversation']]])
        except:
            None
            #print(y[i]['participants'])
            #traceback.print_exc()


for perchat in reversed(chat):
    chatmsg = perchat[1]+'\n\n'
    for x in range(0,len(perchat[2][0])):
        chatx = perchat[2][0]
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
            print(chatx[j])
            traceback.print_exc()
            
    if len(perchat[2][0]) > 5:
        f = open('instagram\INSTA_'+perchat[0]+'.txt', "a+", encoding="utf8")
        f.write(chatmsg)
        f.close()


