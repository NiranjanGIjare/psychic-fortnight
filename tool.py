#!/bin/python3

import os
import sys

if len(sys.argv)==1:
    os.system("firefox https://www.google.com")
else:
    f=open("/home/fedora/.google-command-line-tool/search.txt",'w')
    f.write("https://www.google.com/search?q="+'+'.join(sys.argv[1::])+"&ie=utf-8&oe=utf-8&client=firefox-b-ab")
    f.close()
    os.system("firefox $(cat /home/fedora/.google-command-line-tool/search.txt)")
