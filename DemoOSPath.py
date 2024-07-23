# DemoOSPath.py
from os.path import *
from os import *

fileName="c:\\python310\\python.exe"

if exists(fileName):
    print("file exist:{0}".format(getsize(fileName)))
else:
    print("file is not ")
print(abspath("python.exe"))
print(basename(fileName))

print("OS name:{0}".format(name))
print("environ:{0}".format(environ))

#system("notepad.exe")
#파일목록
import glob
#약식 표기:r(raw string notation )
print(glob.glob(r"c:\work\*.py"))

