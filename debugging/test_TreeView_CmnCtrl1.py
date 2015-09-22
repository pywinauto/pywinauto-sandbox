# -*- coding: mbcs -*-
from __future__ import print_function
import sys, os, time

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

if pywinauto.sysinfo.is_x64_Python():
    app = pywinauto.Application().start_(r'.\apps\MFC_samples\x64\CmnCtrl1.exe')
else:
    app = pywinauto.Application().start_(r'.\apps\MFC_samples\CmnCtrl1.exe')
print('started')
tree = app.CommonControlsSample.TreeView.WrapperObject()
print('connected')

tree.Select((0, ))

app.CommonControlsSample.TVS_CHECKBOXES.Check()

birds = tree.GetItem(r'\Birds')
birds.IsChecked()
birds.IsSelected()

birds.Expand()
eagle = tree.GetItem(r'\Birds\Eagle')
tree.Select(r'\Birds\Eagle')
eagle.IsSelected()

app.CommonControlsSample.TabControl.Select('CToolBarCtrl')
print(app.CommonControlsSample.ToolbarNew.TipTexts())
print(app.CommonControlsSample.ToolbarErase.WrapperObject().TipTexts())
print(app.CommonControlsSample.ToolbarErase.WrapperObject().GetToolTipsControl().Texts())

app.CommonControlsSample.TabControl.Select('CAnimateCtrl')
app.CommonControlsSample.Edit.SetFocus()
app.CommonControlsSample.Edit.TypeKeys(u'ннн_ff{LEFT}{DEL}')
app.CommonControlsSample.Edit.RightClickInput()
time.sleep(1)
print(app.CommonControlsSample.PopupWindow())