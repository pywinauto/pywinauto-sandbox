from __future__ import print_function
import sys, os

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

app = pywinauto.Application().start_(r'.\apps\controlspy0998\Toolbar.exe')
print('started')
bar = app.MicrosoftControlSpy.Toolbar

