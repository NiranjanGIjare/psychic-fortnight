#!/bin/python3

import os
import sys

if len(sys.argv)==1:
    os.system("firefox https://www.google.com")
else:
    l=sys.argv[2::]
    search_string=sys.argv[1]
    for argument in l:
        search_string=search_string+"+"+argument
    search_string="https://www.google.com/search?q="+search_string+"&ie=utf-8&oe=utf-8&client=firefox-b-ab"
    f=open("/home/fedora/.google-command-line-tool/search.txt",'w')
    f.write(search_string)
    f.close()
    os.system("firefox $(cat /home/fedora/.google-command-line-tool/search.txt)")
