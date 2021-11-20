import os
import sys

usage = "usage: wlan_password_clear.py <ssid>"


def wlanclear(ssid):
    cmd = 'netsh wlan show profile name=' + ssid + ' key=clear | findstr "Key Content"'
    results = os.system(cmd)
    return results


if len(sys.argv) == 2:
    ssid = sys.argv[1]
    wlanclear(ssid)
else:
    print(usage)
