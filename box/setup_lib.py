import os

def install_prereqs():
    print("Installing prerequisites...")
    os.system('sudo apt-get install python3-pip libglib2.0-dev')
    os.system('sudo apt update')
    os.system('sudo apt install python3 python3-rpi.gpio python3-pip -y')
    print("Installing Flask web server...")
    os.system('sudo .venv/bin/pip install flask')
    print("Installing required libraries...")
    os.system('sudo apt install gcc')
    os.system('sudo .venv/bin/pip install numpy flask_sslify keyboard melopero_lsm9ds1 requests wifi bluepy GPIO RPi.GPIO pyOpenSSL pandas pillow scipy luma.core luma.oled matplotlib')

def copy_configs():
    print("Copying configuration files...")
    os.system('sudo rm -r /lib/ips_project')
    os.system('sudo rm -r /etc/ips_project')
    os.system('sudo mkdir /usr/lib/ips_project')
    os.system('sudo mkdir /etc/ips_project')
    os.system('sudo cp -a * /usr/lib/ips_project/')

if __name__ == "__main__":
    install_prereqs()
    copy_configs()
