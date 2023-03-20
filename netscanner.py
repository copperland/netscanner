import scapy.all as scapy
import argparse
import colorama
from colorama import Fore, Style , init

         
init(autoreset=True)
def banner():
    return print('\033[31m' + """
          _ __   ___| |_ ___  ___ __ _ _ __  _ __   ___ _ __ 
         | '_ \ / _ | __/ __|/ __/ _` | '_ \| '_ \ / _ | '__|
         | | | |  __| |_\__ | (_| (_| | | | | | | |  __| |   
         |_| |_|\___|\__|___/\___\__,_|_| |_|_| |_|\___|_|                                                                                                                                                                                  
        """)




def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip_addres", dest="target_ip", help="Target IP / IP range example: 10.0.2.0/24 ")
    options = parser.parse_args()
    return options



def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    banner()
    print(Fore.GREEN + "[+] Initializing...")
    print(Fore.GREEN + "[+] Summoning the Network Scanner wizard")

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list





def print_result(results_list):
    print('\033[36m' + 'IP\t\t\tMAC Address\n-----------------------------------------')
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target_ip)
print_result(scan_result)

