import glob as gl
from os import _exit as exitfunc
from time import sleep as slp
from ctypes import cdll
import os
titlename = "CppLibWriter by RikkoMatsumatoOfficial"

def DecodeToUTF8(encoding_type = "utf-8"):
    return bytes(titlename, encoding_type)
def Main():
    Kernel32 = cdll.LoadLibrary("Kernel32.dll")
    Kernel32.SetConsoleTitleA(DecodeToUTF8())
    delimiter = " "
    libname = input("Write Folder for Writing Lists of Libs: ")
    file = [os.path.basename(x) for x in gl.glob(libname + "\\*.lib")]
    with open("Libs.txt", "wt") as libs:
        print(delimiter.join(file) + "\n")
        libs.write(delimiter.join(file))
        slp(12)
        exitfunc(332)
   
    exitfunc(312)

if __name__ == "__main__":
    Main()