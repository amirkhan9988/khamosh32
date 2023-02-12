#coding=utf-8
import os, sys, platform

os.system('xdg-open https://www.facebook.com/shadab.king.524/')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Khamosh.so Khamosh32.so')
except:
    pass
os.system('rm -rf Khamosh.so Kamosh32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Khamosh.so'):
        os.system('curl -L https://github.com/Khamosh-XD/executables/blob/main/Khamosh.cpython-311.so?raw=true -o Khamosh.so') 
        import Khamosh
    else:
        import Khamosh

elif bit == '32bit':
    if not os.path.isfile('Khamosh32.so'):
        os.system('curl -L https://github.com/amirkhan9988/ami/tree/main Khamosh32.cpython-311.so?raw=true -o Khamosh32.so') 
        import Khamosj32
    else:
        import Khamosh32
