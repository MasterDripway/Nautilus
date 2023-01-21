from lib.fetch import fetch
from lib.install import install
from lib.update import update
import os

def main():
    print("[+] Starting installation")
    with open("setup/toolset.ns", 'rb') as items:
        for item in items:
            item = item.decode("utf-8").rstrip("\n")
            dirname = item.rstrip(".git").split('/')[-1]
            path = f"{os.getcwd()}/{dirname}"
            try:
                fetch(item)
            except Exception as e:
                update(path)
            install(path)

if __name__ == '__main__':
    main()