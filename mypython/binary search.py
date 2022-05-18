mylist=[10,12,13,15,20,24,27,33,42,51,56,58,60]
def binarsrch(mylist,srch,start,stop)
srch=42
start=0
stop=len(mylist)
x = binarsrch(mylist,srch,start,stop)
if x == False:
    print("Item" + x ,"not found")
