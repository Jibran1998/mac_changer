#!/usr/bin/env python

import subprocess
import optparse
import re
def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change the mac address of.")
    parser.add_option("-m","--mac", dest="new_mac", help="new mac address")
    (options, arguments)= parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify the interface you want to change, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify the new mac address, use --help for more info.")
    return options
def mac_change(interface,new_mac):
    print("[+] changing mac to"+ new_mac)
    subprocess.call(['ifconfig',interface,'down'])
    subprocess.call(['ifconfig',interface,'hw', 'ether',new_mac])
    subprocess.call(['ifconfig',interface,'up'])
def get_mac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig",interface])
    mac_address_search=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)

    if mac_address_search.group(0):
        return str(mac_address_search.group(0))
    else:
        print("[-] Mac address not found")

options=get_arguments()
current_mac=get_mac(options.interface)
print("Current mac= "+current_mac)
mac_change(options.interface,options.new_mac)
current_mac=get_mac(options.interface)
if current_mac==options.new_mac:
    print("[+] Mac address changed to " + current_mac)

else:
    print("[-] Mac address did not change.")
