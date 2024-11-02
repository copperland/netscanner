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
    os.system("pip install backports.entry-points-selectable==1.1.0")
    os.system("pip install click==8.0.1")
    os.system("pip install cycler==0.10.0")
    os.system("pip install distlib==0.3.2")
    os.system("pip install dlib")
    os.system("pip install et-xmlfile==1.1.0")
    os.system("pip install face-recognition==1.3.0")
    os.system("pip install face-recognition-models==0.3.0")
    os.system("pip install filelock==3.0.12")
    os.system("pip install Flask==2.0.1")
    os.system("pip install imageio==2.27")
    os.system("pip install itsdangerous==2.0.1")
    os.system("pip install Jinja2==3.0.3")
    os.system("pip install joblib==1.3.0")
    os.system("pip install kiwisolver==1.3.2")
    os.system("pip install MarkupSafe==2.0.1")
    os.system("pip install matplotlib")
    os.system("pip install networkx==2.8")
    os.system("pip install nltk==3.6.6")
    os.system("pip install numpy==1.25.0")
    os.system("pip install opencv-python==4.6.0.66")
    os.system("pip install openpyxl==3.0.7")
    os.system("pip install pandas==1.5.3")
    os.system("pip install Pillow")
    os.system("pip install platformdirs==2.5")
    os.system("pip install pyparsing==2.4.7")
    os.system("pip install python-dateutil==2.8.2")
    os.system("pip install pytz==2021.1")
    os.system("pip install PyWavelets==1.3.0")
    os.system("pip install regex==2023.5.5")
    # scikit-image
    os.system("pip install scikit-learn==1.3.0")
    os.system("pip install scipy==1.10.1")
    os.system("pip install six==1.16.0")
    os.system("pip install threadpoolctl==2.2.0")
    os.system("pip install tifffile==2022.8.12")
    os.system("pip install torch")
    os.system("pip install torchvision")
    os.system("pip install tqdm==4.61.2")
    os.system("pip install typing-extensions==4.0.0")
    os.system("pip install irtualenv==20.7.2")
    os.system("pip install Werkzeug==2.0.1")
    os.system("pip install facenet-pytorch")
    os.system("pip install os")
    os.system("pip install time")
    os.system("pip install scapy==2.4.0")
    os.system("pip install scapy-http==1.8.2")
    os.system("pip install colorama")
    os.system("pip install binascii")


def pip3():
    os.system("pip3 install backports.entry-points-selectable==1.1.0")
    os.system("pip3 install click==8.0.1")
    os.system("pip3 install cycler==0.10.0")
    os.system("pip3 install distlib==0.3.2")
    os.system("pip3 install dlib")
    os.system("pip3 install et-xmlfile==1.1.0")
    os.system("pip3 install face-recognition==1.3.0")
    os.system("pip3 install face-recognition-models==0.3.0")
    os.system("pip3 install filelock==3.0.12")
    os.system("pip3 install Flask==2.0.1")
    os.system("pip3 install imageio==2.27")
    os.system("pip3 install itsdangerous==2.0.1")
    os.system("pip3 install Jinja2==3.0.3")
    os.system("pip3 install joblib==1.3.0")
    os.system("pip3 install kiwisolver==1.3.2")
    os.system("pip3 install MarkupSafe==2.0.1")
    os.system("pip3 install matplotlib")
    os.system("pip3 install networkx==2.8")
    os.system("pip3 install nltk==3.6.6")
    os.system("pip3 install numpy==1.25.0")
    os.system("pip3 install opencv-python==4.6.0.66")
    os.system("pip3 install openpyxl==3.0.7")
    os.system("pip3 install pandas==1.5.3")
    os.system("pip3 install Pillow")
    os.system("pip3 install platformdirs==2.5")
    os.system("pip3 install pyparsing==2.4.7")
    os.system("pip3 install python-dateutil==2.8.2")
    os.system("pip3 install pytz==2021.1")
    os.system("pip3 install PyWavelets==1.3.0")
    os.system("pip3 install regex==2023.5.5")
    # scikit-image
    os.system("pip3 install scikit-learn==1.3.0")
    os.system("pip3 install scipy==1.10.1")
    os.system("pip3 install six==1.16.0")
    os.system("pip3 install threadpoolctl==2.2.0")
    os.system("pip3 install tifffile==2022.8.12")
    os.system("pip3 install torch")
    os.system("pip3 install torchvision")
    os.system("pip3 install tqdm==4.61.2")
    os.system("pip3 install typing-extensions==4.0.0")
    os.system("pip3 install irtualenv==20.7.2")
    os.system("pip3 install Werkzeug==2.0.1")
    os.system("pip3 install facenet-pytorch")
    os.system("pip3 install os")
    os.system("pip3 install time")
    os.system("pip3 install scapy==2.4.0")
    os.system("pip3 install scapy-http==1.8.2")
    os.system("pip3 install colorama")
    os.system("pip3 install binascii")


if __name__ == "__main__":
    setup()