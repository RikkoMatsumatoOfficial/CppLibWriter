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
    with open("{}".format(os.getcwd() + "\\Libs.txt"), "a") as libs:
        print(file)
        libs.write(delimiter.join(file) + "\r\n")
        slp(12)
        libs.close()
        exitfunc(332)
   
    exitfunc(312)

if __name__ == "__main__":
    Main()
