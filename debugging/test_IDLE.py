# -*- coding: mbcs -*-
from __future__ import print_function
import sys, os, time

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

if pywinauto.sysinfo.is_x64_Python():
    app = pywinauto.Application().Start(r"C:\Python27_x64\Lib\idlelib\idle.bat", wait_for_idle=False)
    app = pywinauto.Application().Connect(path="C:\Python27_x64\pythonw.exe")
else:
    app = pywinauto.Application().Start(r"C:\Python27\Lib\idlelib\idle.bat", wait_for_idle=False)
    app = pywinauto.Application().Connect(path="C:\Python27\pythonw.exe")
print('started')

win = app.Window_(title_re='^Python.*')

#win.Menu().Items()

from pywinauto import win32structures, win32defines, win32functions
import ctypes

#menu_info  = win32structures.MENUITEMINFOW()
#menu_info.cbSize = ctypes.sizeof (menu_info)
#menu_info.fMask = win32defines.MIIM_CHECKMARKS | win32defines.MIIM_ID | win32defines.MIIM_STATE | win32defines.MIIM_SUBMENU | win32defines.MIIM_TYPE
