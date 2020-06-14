#-*- coding: utf-8 -*-

import CheckConnections as cc
import time, threading

def loop():
    cc.check_net()
    
if __name__ == '__main__':
    while True:    
        child = threading.Thread(target=loop)
        child.daemon = True
        child.start()
        child.join()

        time.sleep(10)
