from __future__ import print_function
import sys, os, time

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

explorer = pywinauto.Application().connect_(path='explorer.exe')
print('connected')
dlg = explorer.Window_(top_level_only=True, title='pywinauto', class_name='CabinetWClass')

print(dlg.TreeView.GetProperties())

tree = dlg.TreeView.WrapperObject()
for elem in tree.GetItem([1]).SubElements(): # desktop tree item sub-elements
	print(elem.Text())

#dlg.SetFocus(); tree.GetItem((1,2,0)).Click(button='left')
#dlg.SetFocus(); tree.GetItem((1,2,0)).Click(button='right')
#tree.ClickInput()
'''
from pywinauto import taskbar

taskbar.TaskBar.Button.ClickInput()

popup_dlg = taskbar.explorer_app.Window_(class_name='NotifyIconOverflowWindow')
popup_toolbar = popup_dlg.Overflow_Notification_Area
print(popup_toolbar.Texts())
popup_dlg.PrintControlIdentifiers()

btn = popup_toolbar.Button('Pythonwin')

windows_before = taskbar.explorer_app.Windows_(top_level_only=False, visible_only=True)
btn.ClickInput(button='right')
time.sleep(2)
windows_after = taskbar.explorer_app.Windows_(top_level_only=False, visible_only=True)

#taskbar.explorer_app.PopupMenu.GetMenuPath('Activate').Click()
'''

from pywinauto import taskbar
#taskbar.RightClickHiddenSystemTrayIcon('Google Chrome')
