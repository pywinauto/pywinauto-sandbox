from __future__ import print_function
from pywinauto.application import Application
import time

app = Application().start_("Notepad")
dlg = app.Window_(title='Untitled - Notepad', class_name='Notepad')
dlg.edit.SetEditText("Here is some text\r\n and some more")
time.sleep(10)
app.kill_()