import subprocess
import os

def install(path) -> None:
    for root, dirs, files in os.walk(path):
        for f in files:
            if f == "installer.ns":
                commands = open(root + '/' + f, 'rb').readlines()
                print("[+] Starting installation")
                for c in commands:
                    c = c.decode("utf-8")
                    print(f"[+] Running {c}")
                    subprocess.run(c.split(" "), check=True)
