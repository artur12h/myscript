# ----------------------------------------------
# Program by Arthur for study                                         
#                                               
#                                               
# Version         Date         lesson           
#  none           2022       'JSON on python'   
#                                               
#-----------------------------------------------
import json
filename='user_settings.txt'
myfile= open(filename, mode = 'w', encoding='utf_8')
player = {
    'name':'Mudilo' ,
    'score': 345 ,
    'awards':['AW','RE', 'BBC']
    }
player2 = {
        'name':'Mark',
        'score':100,
        'awards':['MS','ND','LS']
    
    }
myplayer=[]
myplayer.append(player)
myplayer.append(player2)
#--------------JSON save by file---------------------------
json.dump(myplayer,myfile)
myfile.close()
#--------Load Json------------
myfile=open(filename, mode='r', encoding='utf_8')
json_data= json.load(myfile)

for user in json_data:
    print('Player name is '+ str(user['name']))
    print('Player score is ' +str(user['score']))
    print('Player awards is ' + str(user['awards'][0]))