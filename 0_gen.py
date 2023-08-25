import os
import time
import platform
import json
import codecs

try:
    f = codecs.open(r'_tasks.json', "r", "utf_8_sig").read()
    data = json.loads(f)
    i = 0
    for e in data:
        if i>=100 and i<=700:
            f = open(str(i), "w")
            f.write(json.dumps(e));
            f.close()
        i+=1
except BaseException as e:
    print('FATAL ERROR')
    print(str(e))
    print('close 3')
    time.sleep(1)
    print('close 2')
    time.sleep(1)
    print('close 1')
    time.sleep(1)