# jangan lupa subscribe MisterAM
# Sepesial idul fitri
# sceipt gua kagak pernah gua encriypt ngab

#jangan ubah
import requests,os,sys,time
from time import sleep
#kalo biaa jangan di ubah :v
os.system('clear')
print ('\033[36;1mSubscribe yt ku bang \033[37mArul MINIKREP \033[36mok! :v')
os.system('termux-open-url https://youtube.com/channel/UCJh9I1GEVJk8qQWGs1t09eQ')
sleep(5)
os.system('clear')
print ('\033[37;1m Save Wa Gw Bang :')
os.system('xdg-open https://wa.me/6288219647445')
sleep(3)
os.system('clear')
# Ubah Terserah kalian ngab
banner= """

\033[31;1m ███████╗██████╗  █████╗ ███╗   ███╗ \033[31;1m███████╗███╗   ███╗███████╗
\033[31;1m ██╔════╝██╔══██╗██╔══██╗████╗ ████║ \033[31;1m██╔════╝████╗ ████║██╔════╝
\033[31;1m ███████╗██████╔╝███████║██╔████╔██║ \033[31;1m███████╗██╔████╔██║███████╗
\033[37;1m ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║ \033[37;1m╚════██║██║╚██╔╝██║╚════██║
\033[37;1m ███████║██║     ██║  ██║██║ ╚═╝ ██║ \033[37;1m███████║██║ ╚═╝ ██║███████║
\033[37;1m ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ \033[37;1m╚══════╝╚═╝     ╚═╝╚══════╝

\033[33;1m╔═════════════════════════════════════════════════════╗
\033[33;1m║  \033[36;1m [•] Author  : Asrul                              \033[33;1m ║
\033[33;1m║  \033[36;1m [•] GitHub  : https:github.com/ArulMC123         \033[33;1m ║
\033[33;1m║  \033[36;1m [•] Yotube  : Arul MINIKREP                      \033[33;1m ║
\033[33;1m║  \033[36;1m [•] Friends : Dims,Adly,Faiz,Angga,Asrul,Putra   \033[33;1m ║
\033[33;1m╚═════════════════════════════════════════════════════╝
\033[36;1m╔═══════════════════════════╗
\033[36;1m║\033[33;1m   GUNAKAN DENGAN BENAR   \033[36;1m ║
\033[36;1m╚═══════════════════════════╝"""
sleep(1)
print(banner)

# Jangan lu ubah ngab
print ('\033[31;1m[!] \033[32;1mExample: \033[33;1m8xxxxxxx')

nomor = input(' \033[36;1mMasukan Nomor Orang Nya :\033[33;1m ')
print ('\033[32;1mMASUKAN JUMLAH SPAMNYA !!')
print ('')
jm = int(input('\033[31;1m Jumlah Spam :\033[33;1m '))

for i in range(jm):
      req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
      if "mengirim" in req:
            print ('\n \033[37;1m[\033[32;1m✓\033[37;1m]\033[32;1mSUKSES MENGIRIM SPAM')
      else:
            print ('\n \033[37;1m[\033[33;1m LOADING \033[37;1m]\033[36;1mSEDANG MENGIRIM SPAM')


# subscribe MisterAM
