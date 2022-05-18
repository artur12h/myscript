# ----------------------------------------------
# Program by Arthur for study                                         
#                                               
#                                               
# Version         Date         lesson           
#  none           2022       'Internet part2'   
#                                               
#-----------------------------------------------
from urllib import request ,parse
import sys
myurl='http://www.google.com/search?'
value={'q':'ANDESA Soft'}

myheader={}
myheader["User-Agent"] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
try:
    mydata=parse.urlencode(value)
    print(mydata)
    myurl=myurl + mydata
    req = request.Request(myurl,headers=myheader)
    answer=request.urlopen(req)
    answer=answer.readlines()
    for line in answer:
        print(line)
except Exception:
    print("Error occuried during web request!")
    print(sys.exc_info()[1])