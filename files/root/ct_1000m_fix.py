#!/usr/bin/python3
from subprocess import run,PIPE
import json
PYTHONIOENCODING='utf-8'
def ifup(eth: str):
    run(f'ubus call network.interface.{eth} up', shell=True)


def ifdown(eth: str):
    run(f'ubus call network.interface.{eth} down', shell=True)


def status(eth: str) -> dict:
    r1 = run(f'ubus call network.interface.{eth} status', shell=True, stdout=PIPE)
    return json.loads(r1.stdout.decode('utf-8'))


if __name__ == "__main__":
    wan = status("wan")
    iptv0 = status("iptv0")
    iptv1 = status("iptv1")
    if min(iptv0['uptime'], iptv1['uptime'])-30 <= wan['uptime']:
        print("IPTV start time is lower than WAN, try to speed.")
        print(iptv0["uptime"])
        print(iptv1["uptime"])
        print(wan["uptime"])
        ifdown("wan")
        ifup("wan")
    else:
        print("WAN can running with max speed")
    pass
