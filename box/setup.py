import os
import sys
import setup_lib

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
        setup_lib.install_prereqs()
        setup_lib.copy_configs()
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

if __name__ == "__main__":
    main()
