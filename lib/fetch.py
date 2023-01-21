import requests
import subprocess

def fetch(url) -> None:
    print("[+] Starting Download")
    subprocess.run(['git', 'clone', url], check=True)
