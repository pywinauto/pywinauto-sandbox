from __future__ import print_function
import sys, os

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

app = pywinauto.Application().start_(r'.\apps\MFC_samples\x64\RowList.exe')
print('started')
list = app.RowListSampleApplication.ListView.WrapperObject()

print(list.GetProperties())

columns = list.Columns()
print(columns)

list.Select(1)
#list.ClickInput()

yellow = list.GetItem('Yellow')
yellow.Check()