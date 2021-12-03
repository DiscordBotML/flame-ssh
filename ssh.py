import paramiko
import json
import os
import platform
import random
import sys
import requests

symb = ('@')
sym = ('\n')
host = input('Host ip: ')
user = input('Login as: ')

all_info = f'--------------------------\nhost: { host }\nuser: { user }\nBy ENDER#4335\n\n--------------------------'

print( all_info )

my_file = open("ssh.log", "w+")
my_file.write("<INFO> ssh-log: \n" + host + sym + user)
my_file.close()

os.system('ssh ' + user + symb + host)