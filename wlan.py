import os
import sys 

cmd = 'netsh wlan show profile name='+sys.argv[1]+' key=clear | findstr "Key Content"'
os.system(cmd)