#!/bin/bash

{
for ((i=0;i<50;i++))
do
    DIR="/opt/jedione/mcjedi.bin"
    echo 25
    if [ -d "$DIR" ]; then
        echo 100
        break
    else
        cd /opt/jedione/
        echo 50
        sudo unzip mcjedi.zip
        sudo ./mcjedi.bin -service install
        sudo ./mcjedi.bin -service start
        echo 75
        sudo python led.py
        echo 100
        sleep 1
        break
    fi
sleep 3
done
} | whiptail --title "JEDI One PiBakery" --gauge "\nInstalling JEDI One..." 8 40 0