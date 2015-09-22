from __future__ import print_function
import sys, os, time

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

if pywinauto.sysinfo.is_x64_Python():
    app = pywinauto.Application().start_(r'.\apps\controlspy0998\x64\Up-Down.exe')
else:
    app = pywinauto.Application().start_(r'.\apps\controlspy0998\Up-Down.exe')
print('started')
up_down = app.MicrosoftControlSpy.UpDown2.WrapperObject()
print('connected')

up_down.SetValue(23)
#time.sleep(1)
print(up_down.GetValue())

#pywinauto.win32functions.SendMessage(tree, pywinauto.win32defines.TVM_SELECTITEM, pywinauto.win32defines.TVGN_CARET, tree.GetItem((0, 1, 2)).elem)