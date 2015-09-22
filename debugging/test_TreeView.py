from __future__ import print_function
import sys, os, time

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

if pywinauto.sysinfo.is_x64_Python():
    app = pywinauto.Application().start_(r'.\apps\controlspy0998\x64\Tree View.exe')
else:
    app = pywinauto.Application().start_(r'.\apps\controlspy0998\Tree View.exe')
print('started')
tree = app.MicrosoftControlSpy.TreeView.WrapperObject()
print('connected')

tree.SetFocus()
tree.Select((0, 1, 2))

#pywinauto.win32functions.SendMessage(tree, pywinauto.win32defines.TVM_SELECTITEM, pywinauto.win32defines.TVGN_CARET, tree.GetItem((0, 1, 2)).elem)