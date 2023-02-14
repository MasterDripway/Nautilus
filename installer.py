from lib.install import install
import os

install("setup")
cwd = os.getcwd()
HOME = os.getenv("HOME", "/home/")
print('[+] Adding NAUTILUS_HOME to ~/.bashrc')
with open(HOME + '/.bashrc', 'a') as writer:
    writer.write(f"export NAUTILUS_HOME=\"{cwd}\"")
