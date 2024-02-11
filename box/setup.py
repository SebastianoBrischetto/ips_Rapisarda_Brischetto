import os
import sys


def main():
    if os.geteuid() != 0:
        sys.exit('You need root access to install!')

    print("\n\n###################################")
    print("###  Indoor Positioning System  ###")
    print("###   Indoor Navigation System  ###")
    print("### Based on Geomagnetic Field  ###")
    print("###    Box di Acquisizione      ###")
    print("###################################\n")

    install_ans = input("Sei pronto per eseguire il commit delle modifiche al sistema? [y/N]: ")

    if install_ans.lower() == 'y':
        install_prereqs()
        copy_configs()
    else:
        print("\n\n===================================================")
        print("---------------------------------------------------")
        print("\nIPS Installazione Annullata. Nothing changed...\n")
        print("---------------------------------------------------")
        print("===================================================\n")
        sys.exit()

    print("\n\n#####################################")
    print("##### Indoor Positioning System Installazione Completata  #####")
    print("#####################################\n")


def install_prereqs():
    print("Installing prerequisites...")
    os.system('sudo apt-get install python3-pip libglib2.0-dev')
    os.system('sudo apt update')
    os.system('sudo apt install python3 python3-rpi.gpio python3-pip -y')
    # os.system('sudo apt-get install python3.11-dev -y') needed for GPIO RPi.GPIO
    print("Installing Flask web server...")
    os.system('sudo .venv/bin/pip install flask')
    print("Installing required libraries...")
    os.system('sudo apt install gcc')
    os.system(
        'sudo .venv/bin/pip install numpy flask_sslify keyboard melopero_lsm9ds1 requests wifi bluepy GPIO RPi.GPIO pyOpenSSL pandas pillow scipy luma.core luma.oled matplotlib')


def copy_configs():
    print("Copying configuration files...")
    os.system('sudo rm -r /lib/ips_project')
    os.system('sudo rm -r /etc/ips_project')
    os.system('sudo mkdir /usr/lib/ips_project')
    os.system('sudo mkdir /etc/ips_project')
    os.system('sudo cp -a * /usr/lib/ips_project/')


if __name__ == "__main__":
    main()
