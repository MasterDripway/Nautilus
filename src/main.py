from lib.fetch import fetch
from lib.install import install

def main():
    print("[+] Starting installation")
    fetch('https://github.com/MasterDripway/Nautilus.git')
    install("/home/manuel/proj/nautilus/src/Nautilus")

if __name__ == '__main__':
    main()