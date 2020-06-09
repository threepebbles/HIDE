# -*- coding: utf-8 -*-

import urllib.request, urllib.error
import time, threading, sys, os
import Login


def check_net():
    _log_file = 'C:/Users/이은영/Desktop/log.txt'
    while True:
        try:
            urllib.request.urlopen('http://216.58.192.142', timeout=1)

            # network is connected
            print('connect network')
            with open(_log_file, 'a') as f:
                f.write('connect network {}\n'.format(time.strftime('%c', time.localtime(time.time()))))

            Login.login()

        except urllib.error.URLError as err:
            # network is disconnected
            print('disconnect network')
            print(err)
            with open(_log_file, 'a') as f:
                f.write('disconnect network {}\n'.format(time.strftime('%c', time.localtime(time.time()))))
        time.sleep(10)