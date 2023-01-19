from lib.fetch import fetch
from lib.install import install

def main():
    print("[+] Starting installation")
    fetch('https://github.com/MasterDripway/Nautilus.git')
    install("~/proj/Nautilus/src/Nautilus")

if __name__ == '__main__':
    main()