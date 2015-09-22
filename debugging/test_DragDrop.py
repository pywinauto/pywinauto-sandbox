from __future__ import print_function
import sys, os, time
import logging

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

logger = logging.getLogger('pywinauto')
print(logger.level)

pywinauto.actionlogger.enable()
logger = logging.getLogger('pywinauto')
print(logger.level)

mfc_samples_folder = os.path.join(
   os.path.dirname(sys.argv[0]), r"apps\MFC_samples")
if pywinauto.sysinfo.is_x64_Python():
    mfc_samples_folder = os.path.join(mfc_samples_folder, 'x64')

app = pywinauto.Application.start(os.path.join(mfc_samples_folder, u"CmnCtrl1.exe"))
print('connected')
tree = app.Common_Controls_Sample.TreeView.WrapperObject()

birds = tree.GetItem(r'\Birds')
dogs = tree.GetItem(r'\Dogs')

#tree.DragMouse("left", birds.Rectangle().mid_point(), dogs.Rectangle().mid_point())
tree.DragMouseInput("left", birds.Rectangle().mid_point(), dogs.Rectangle().mid_point())
#app.kill_()

#app = pywinauto.Application.start(os.path.join(mfc_samples_folder, u"CmnCtrl3.exe"))
#dlg = app.Common_Controls_Sample