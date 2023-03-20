import os
import time



def setup():
    while True:
        print("""
        

            _                                       
           | |                                      
 _ __   ___| |_ ___  ___ __ _ _ __  _ __   ___ _ __ 
| '_ \ / _ | __/ __|/ __/ _` | '_ \| '_ \ / _ | '__|
| | | |  __| |_\__ | (_| (_| | | | | | | |  __| |   
|_| |_|\___|\__|___/\___\__,_|_| |_|_| |_|\___|_|   
                                                                                      
                                                                                   
                                                 
              [1] - Install Dependecies with PIP
              [2] - Install Dependencies with PIP3
        """)

        result = input("[root@whoami]: ")


        if result == "1":
            print("[PIP library] - Installing...")
            time.sleep(3)
            pip()
            break
        elif result == "2":
            print("[PIP3 library]  - Installing...")
            time.sleep(3)
            pip3()
            break
        else:
            print("[ERROR] - Please choose one option.")
            time.sleep(2)
            os.system("clear")
            continue


def pip():
    os.system("pip install os")
    os.system("pip install time")
    os.system("pip install scapy==2.4.0")
    os.system("pip install scapy-http==1.8.2")
    os.system("pip install colorama")
    os.system("pip install binascii")


def pip3():
    os.system("pip3 install os")
    os.system("pip3 install time")
    os.system("pip3 install scapy==2.4.0")
    os.system("pip3 install scapy-http==1.8.2")
    os.system("pip3 install colorama")
    os.system("pip3 install binascii")


if __name__ == "__main__":
    setup()