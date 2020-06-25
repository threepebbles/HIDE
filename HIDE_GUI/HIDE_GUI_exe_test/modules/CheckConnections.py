#-*- coding: utf-8 -*-

import urllib.request, urllib.error
import time, threading, sys, os
import Login


# check network state
def check_net():
    while True:
        try:
            urllib.request.urlopen('http://216.58.192.142', timeout=1)
            
            # network is connected
            print('connect network')

            Login.login()

        except urllib.error.URLError as err: 
            # network is disconnected
            print('disconnect network')
            print(err)
        time.sleep(10)