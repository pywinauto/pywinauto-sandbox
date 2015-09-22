from __future__ import print_function
import sys, os, time

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

app = pywinauto.Application().start_(r"C:\Program Files (x86)\Internet Explorer\iexplore.exe")
main = app.Window_(title_re='^.* - Windows Internet Explorer$')

main.PageControlToolbar.WrapperObject().PressButton(6)
main.ToolbarFile.PressButton('&Tools')
time.sleep(1)
main.TypeKeys('{UP}{ENTER}')

#OptionsDialog = app.Window_(title='Internet Options', class_name='#32770')
app.InternetOptions.Wait('ready')
#app.InternetOptions.PrintControlIdentifiers()
app.InternetOptions.HomePageTabControl.Select('Connections')