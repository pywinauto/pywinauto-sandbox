from __future__ import print_function
import sys, os

print("\xef\xbb\xbf")

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

app = pywinauto.Application().start_(r"c:\Program Files\Windows NT\Accessories\wordpad.exe")
print('started')
app.DocumentWordPad.UIRibbonDockTop.ClickInput(coords=(580, 60))

list = app.DateAndTime.ListBox.WrapperObject()

print(list.GetProperties())

columns = list.Texts()
print(columns)