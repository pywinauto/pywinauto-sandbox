from __future__ import print_function
import sys, os

print("\xef\xbb\xbf")

script_dir = os.path.join(os.getcwd(), os.path.dirname(sys.argv[0]))
print('script_dir = ' + script_dir)
os.chdir(script_dir)
import pywinauto

app = pywinauto.Application().start_(os.path.join(script_dir, r"apps\MFC_tutorial\MFC_Tutorial9.exe"))
print('started')
dlg = app.MFC_Tutorial9

dlg.TypeYourTextEdit.TypeKeys('qqq')
dlg.Add.Click()

dlg.TypeYourTextEdit.Select()
dlg.TypeYourTextEdit.TypeKeys('123')
dlg.Add.Click()

dlg.TypeYourTextEdit.Select()
dlg.TypeYourTextEdit.TypeKeys('third item', with_spaces=True)
dlg.Add.Click()

ctrl = dlg.ListBox.WrapperObject()