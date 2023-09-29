import requests
import hashlib
import urllib.parse

def sha256_sign(secret, message):
    sha256 = hashlib.sha256()
    sha256.update(f"{message}{secret}".encode())
    return sha256.hexdigest()

url = "http://127.0.0.1:21051/api"
region = "dev_docker"
ticket = "GM"
command = "1116"
uid = "UID"
msg = "COMMAND"
secret = "KEY"

payload = {
    "region": region,
    "ticket": ticket,
    "cmd": command,
    "uid": uid,
    "msg": msg
}

kvs = []
for key, value in payload.items():
    kvs.append(f"{key}={value}")
kvs.sort()

qstr = "&".join(kvs)
sign = sha256_sign(secret, qstr)

params = {
    "region": region,
    "ticket": ticket,
    "cmd": command,
    "uid": uid,
    "msg": msg,
    "sign": sign
}

response = requests.get(url, params=params)
print(response.content.decode())
