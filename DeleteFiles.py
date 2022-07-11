import os
import shutil
import time

path=input("Enter path of folder:")
days=3
seconds=time.time()-(days*864000)

if (os.path.exists(path)):
    for root,dirs,files in os.walk(path,topdown=True):
        for name in files:
            path=os.path.join(root,name)
            ctime=os.stat(path).st_ctime

            if (seconds>=ctime):
                os.remove(path)
                print("\n Deleted the path" + path + "successfully")

        for x in dirs:
            path = os.path.join(root, x)
            ctime = os.stat(path).st_ctime

            if (seconds >= ctime):
                shutil.rmtree(path)
                print("\n Deleted the path " + path)

else:
    print("\n Path not found")