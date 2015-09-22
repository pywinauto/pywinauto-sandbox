from __future__ import print_function
import sys, os

os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
import pywinauto

app = pywinauto.Application.start(r'msiexec.exe /i 7z920-x64.msi')

Wizard = app['7-Zip 9.20 (x64 edition) Setup']
Wizard.NextButton.Click()

Wizard['I &accept the terms in the License Agreement'].Wait('enabled').CheckByClick()
Wizard.NextButton.Click()

Wizard['Custom Setup'].Wait('enabled')
Wizard.NextButton.Click()

Wizard.Install.Click()

Wizard.Finish.Wait('enabled', timeout=30)
Wizard.Finish.Click()
Wizard.WaitNot('visible')

if os.path.exists(r"C:\Program Files\7-Zip\7zFM.exe"):
    print('OK')
else:
    print('FAIL')
