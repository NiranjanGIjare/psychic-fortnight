#!/bin/python3

import os
import sys

def allsearch(strt):
    f=open("/tmp/search.txt",'w')
    f.write("https://www.google.com/search?q="+'+'.join(sys.argv[strt::])+"&ie=utf-8&oe=utf-8&client=firefox-b-ab")
    f.close()
    os.system("firefox $(cat /tmp/search.txt)")

if len(sys.argv)==1:
    os.system("firefox https://www.google.com")
elif sys.argv[1]=='-i':
    f=open("/tmp/search.txt",'w')
    f.write("https://www.google.co.in/search?hl=en&tbm=isch&source=hp&biw=1366&bih=630&ei=Sfo0W4DFHs2c9QO0gIugCg&q="+'+'.join(sys.argv[2::])+"&oq="+'+'.join(sys.argv[2::])+"&gs_l=img.3..0l10.")
    f.close()
    os.system("firefox $(cat /tmp/search.txt)")
elif sys.argv[1]=='-a':
    allsearch(2)
else :
    allsearch(1)
