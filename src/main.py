from lib.fetch import fetch
from lib.install import install

def main():
    print("[+] Starting installation")
    with open("toolset.ns", 'rb') as items:
        for item in items:
            fetch(item.decode("utf-8").rstrip("\n"))
        install("~/proj/Nautilus/src/Nautilus/tools")

if __name__ == '__main__':
    main()