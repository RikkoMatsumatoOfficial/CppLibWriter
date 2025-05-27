@echo off

set MAIN=Main.py

pyinstaller %MAIN% --console --onefile --name "CppLibWriter"