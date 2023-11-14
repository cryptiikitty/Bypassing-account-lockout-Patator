import os
import time
import datetime
import argparse
 
 
os.system("cat /result/20*.txt | grep -e '500' -e 'xxx' | cut -d: -f5 | awk -F\| '{print $1}' |sort -u | awk '{$1=$1};1' >> /res.tmp")
 
if os.stat("/res.tmp").st_size == 0:
    print('no weak password')
else:
    os.system("python3 /bot2.py --f /res.tmp")
 
os.system("rm -f /res.tmp")
