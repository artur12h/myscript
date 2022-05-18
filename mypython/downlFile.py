# ----------------------------------------------
# Program by Arthur for study                                         
#                                               
#                                               
# Version         Date         lesson           
#  none           2022       'Download file from Internet'   
#                                               
#-----------------------------------------------
from urllib import request
import sys
myUrl='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dreamstime.com%2Fd-hacking-code-data-flow-stream-green-screen-typing-coding-symbols-computer-encrypted-fast-network-security-programming-image150730668&psig=AOvVaw3l7VKQWMTkhtQRF0zO8Ky3&ust=1651657115691000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCNDojrOEw_cCFQAAAAAdAAAAABAD'
myFile='/home/mylinuxserverforweb/Документы/my_script_python'
try:
    print("Start download file from" + myUrl)
    request.urlretrieve(myUrl,myFile)
except Exception:
    print('AHTUNG!!!!!!')
    print(sys.exc_info())
    exit
print("File Download and saved " + myFile)
