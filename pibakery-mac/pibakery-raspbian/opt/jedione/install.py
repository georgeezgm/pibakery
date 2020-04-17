#!/usr/bin/python

import os
from time import sleep

# Check if binary already exists
# Exit if it already exists, we will do it only while installing
sleep(3)

if os.path.exists("mcjedi.dat"):
    os.exit()

# Install JEDI One and run
install_jedi = "sudo ./mcjedi.bin -service install"
run_jedi = "sudo ./mcjedi.bin -service start"
run_led = "sudo python led.py"

sleep(3)
# os.system(cmd_zip)
os.system(install_jedi)  
print('returned value:', install_jedi)
os.system(run_jedi)
os.system(run_led)