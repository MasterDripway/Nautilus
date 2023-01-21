import requests
import subprocess
from lib.fetch import fetch

def get_ver(path):
    ver = ''
    with open(path + '/' + 'version.txt', 'rb') as rfile:
        ver, addr, repo = [i.decode('utf-8').rstrip('\n').strip(' ') for i in rfile.readlines()]
    git_ver = requests.get(addr).content.decode('utf-8').split(' ')[0]
    return (ver, git_ver, addr, repo)

def update(path):
    info = get_ver(path)
    if info[0] != info[1]:
        try:
            subprocess.run(['mkdir', 'temp'], check=True)
        except Exception as e:
            pass
        finally:
            subprocess.run(['mv', path, 'temp'], check=True)
            try:
                fetch(info[3])
            except Exception as e:
                path_split = path.split('/')
                newpath = "/".join(path_split[:-1]) + '/temp/' + path_split[-1]
                subprocess.run(['rm', '-rf', path], check=True)
                subprocess.run(['mv', newpath, '.'], check=True)
            subprocess.run(['rm', '-rf', 'temp'], check=True)


def main():
    update("/home/manuel/proj/Nautilus/OTP")

if __name__ == "__main__":
    main()
