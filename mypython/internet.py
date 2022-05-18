# ----------------------------------------------
# Program by Arthur for study                                         
#                                               
#                                               
# Version         Date         lesson           
#  none           2022       'Internet'   
#                                               
#-----------------------------------------------
from urllib import request
myurl='https://fbref.com/en/players/e16376a8/Nurgeldi-Astanow'
answer=request.urlopen(myurl)
mytext=answer.readlines()
mytext2=answer.read()

print(answer)
print(mytext2)
for line in mytext:
    print(line)
