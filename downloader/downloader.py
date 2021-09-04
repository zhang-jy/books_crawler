import requests
import threading
import time
import os

cur_path = os.path.dirname(os.path.abspath(__file__))

home_url = "https://www.56fz.com/books/28360/{}.html"
pages_index = range(900,1074)
total = len(pages_index)
task_ss = [0, 0, 0]

def comp_r_log():
    print("total: {}/{}".format(task_ss[0],total))
    print("success: {}%".format(task_ss[1]*100/task_ss[0]))
    print("failed: {}%".format(task_ss[2]*100/task_ss[0]))

class downloadThread(threading.Thread):
    def __init__(self, url, index):
        threading.Thread.__init__(self)
        self.url = url
        self.index = index
    def run(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            with open(os.path.join(cur_path,"download","page-{}".format(self.index)), "w", encoding="utf-8") as fd:
                fd.write(r.text)
            print("{}-{} done".format(self.url, self.index))
            thread_lock.acquire()
            task_ss[0] += 1
            task_ss[1] += 1
            comp_r_log()
            thread_lock.release()
        else:
            print("{}-{} failed".format(self.url,self.index))
            thread_lock.acquire()
            task_ss[0] += 1
            task_ss[2] += 1
            comp_r_log()
            thread_lock.release()
        
count = 0
thread_lock = threading.Lock()

for page_index in pages_index:
    try:
        url = home_url.format(page_index)
        thread_cur = downloadThread(url, page_index)
        thread_cur.start()
        thread_cur.join()
        count += 1
        if count >= 10:
            time.sleep(5)
            count = 0
    except:
        print("failed"+page_index)
