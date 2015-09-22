from __future__ import print_function
import sys, os, time

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto
ctlspy = pywinauto.Application().start_(u'apps\\ControlSpy_20\\ControlSpyV6.exe')
dlg = ctlspy.Window_(top_level_only=True, title=u'Control Spy')
lb = dlg.ListBox3.WrapperObject()
lb.Select(item=u'TreeView')

tree = dlg.TreeView.WrapperObject()
for elem in tree.GetItem([0]).SubElements(): # 'Planets' tree item sub-elements
    print(elem.Text())

dlg.SetFocus()
tree.GetItem((0,0,0)).Click(button='left')
tree.GetItem((0,0,1)).Click(button='left')
tree.GetItem((0,0,2)).Click(button='left')