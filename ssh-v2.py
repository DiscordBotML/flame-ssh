import os
import time

print ('Запуск библиотек...')
s='█'
for i in range(101):
 time.sleep(0.025)
 print('\r','Загрузка',i*s,str(i),'%',end='')

os.system('pip install paramiko')
os.system('pip install requests')
os.system('pip install emoji')
os.system('')
os.system('')
os.system('')

os.system('neofetch')

symb = ('@')
sym = ('\n')
host = input('\n\n Host ip: ')
user = input('\n Login as: ')

all_info = f'--------------------------\nhost: { host }\nuser: { user }\nBy ENDER#4335\n\n--------------------------'

print( all_info )

my_file = open("ssh.log", "w+")
my_file.write("<INFO> ssh-log: \n" + host + sym + user)
my_file.close()

os.system('ssh ' + user + symb + host)