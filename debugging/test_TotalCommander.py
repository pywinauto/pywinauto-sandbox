# -*- coding: mbcs -*-
from __future__ import print_function
import sys, os, time

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

if pywinauto.sysinfo.is_x64_Python():
    app = pywinauto.Application().start_(r"C:\Program Files\Sublime Text 3\sublime_text.exe") #'C:\totalcmd\TOTALCMD64.EXE')
else:
    app = pywinauto.Application().start_(r"C:\Program Files (x86)\Passware\Passware Kit 2015 Demo\PasswareKitForensic.exe")
    win = app.PasswarePasswordRecoveryKitForensicDemo.WrapperObject()
    win.Menu().Item(0).SubMenu().Item(1).SubMenu()
print('started')

win = app.Window_(title_re='^Total Commander.*$')

#win.Menu().Items()

from pywinauto import win32structures, win32defines, win32functions
import ctypes

#menu_info  = win32structures.MENUITEMINFOW()
#menu_info.cbSize = ctypes.sizeof (menu_info)
#menu_info.fMask = win32defines.MIIM_CHECKMARKS | win32defines.MIIM_ID | win32defines.MIIM_STATE | win32defines.MIIM_SUBMENU | win32defines.MIIM_TYPE
