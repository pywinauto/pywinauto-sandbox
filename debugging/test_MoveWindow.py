from __future__ import print_function
import sys, os, time

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

app = pywinauto.Application()
if pywinauto.sysinfo.is_x64_Python() or not pywinauto.sysinfo.is_x64_OS():
    app.start_(r"C:\Windows\System32\calc.exe")
else:
    app.start_(r"C:\Windows\SysWOW64\calc.exe")

dlg = app.Calculator
dlg.MenuSelect('View->Scientific\tAlt+2')
ctrl = pywinauto.controls.HwndWrapper.HwndWrapper(dlg.Button2.handle) # Backspace


subdialogs = [child for child in dlg.Children() if child.Class() == '#32770']
dlgClientRect = subdialogs[2].Rectangle()

prev_rect = ctrl.Rectangle() - dlgClientRect

new_rect = pywinauto.win32structures.RECT(prev_rect)
new_rect.left -= 1
new_rect.top -= 1
new_rect.right += 2
new_rect.bottom += 2

ctrl.MoveWindow(
    new_rect.left,
    new_rect.top,
    new_rect.width(),
    new_rect.height(),
    )
time.sleep(0.1)

print('prev_rect = ', prev_rect)
print('new_rect = ', new_rect)
print('dlgClientRect = ', dlgClientRect)
print('ctrl.Rectangle() = ', ctrl.Rectangle())
