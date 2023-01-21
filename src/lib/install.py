import subprocess
import os

def install(path) -> None:
    for root, dirs, files in os.walk(path):
        for f in files:
            if f == "installer.ns":
                commands = open(root + '/' + f, 'rb').readlines()
                print("[+] Starting installation")
                wd = '.'
                for c in commands:
                    c = c.decode("utf-8").rstrip('\n')
                    print(f"[+] Running {c}")
                    if c.startswith('cd'):
                        wd = c.split(' ')[1]
                        continue
                    subprocess.run(c.split(" "), check=True, cwd=wd)
