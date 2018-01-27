import urllib.request
import json
import sys
import time

with open('finalnobin.json') as json_data:   # import file list 
    items = json.load(json_data)

########################################### Progress Bar
def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.perf_counter()
        return
    duration = time.perf_counter() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds elapsed" % (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


########################################### Download function
def batch(startAt, stopAt): 
    a=0 
    for i in items:
        a+=1
        
        if a < startAt or a > stopAt:
            continue

        num = i['id']
        url = i['url']
        typ = i['type']
        urlfinal = (url + "/" + str(num) + typ)
        filename = (str(num) + typ)
        print("\n " + '\n[%d] Downloading file %s...' % (a, str(num) + typ))
        urllib.request.urlretrieve(urlfinal, filename, reporthook)

        if a == stopAt:
            print("\n " + "\nAll files downloaded successfully. \nYou can close the program.")
        else:
         pass     
batch(1, 1000) #download file from n to N
