from __future__ import print_function
import pywinauto

pywinauto.Application().Start(r'explorer.exe')
explorer = pywinauto.Application().Connect(path='explorer.exe')

# Go to "Control Panel -> Programs and Features"
NewWindow = explorer.Window_(top_level_only=True, active_only=True, class_name='CabinetWClass')
try:
    NewWindow.AddressBandRoot.ClickInput()
    NewWindow.TypeKeys(r'Control Panel\Programs\Programs and Features{ENTER}', with_spaces=True, set_foreground=False)
    ProgramsAndFeatures = explorer.Window_(top_level_only=True, active_only=True, title='Programs and Features', class_name='CabinetWClass')

    # wait while list of programs is loading
    explorer.WaitCPUUsageLower(threshold=5)

    item_7z = ProgramsAndFeatures.FolderView.GetItem('7-Zip 9.20 (x64 edition)')
    item_7z.EnsureVisible()
    item_7z.ClickInput(button='right', where='icon')
    explorer.PopupMenu.MenuItem('Uninstall').Click()

    Confirmation = explorer.Window_(title='Programs and Features', class_name='#32770', active_only=True)
    if Confirmation.Exists():
        Confirmation.Yes.ClickInput()
        Confirmation.WaitNot('visible')

    WindowsInstaller = explorer.Window_(title='Windows Installer', class_name='#32770', active_only=True)
    if WindowsInstaller.Exists():
        WindowsInstaller.WaitNot('visible', timeout=20)

    SevenZipInstaller = explorer.Window_(title='7-Zip 9.20 (x64 edition)', class_name='#32770', active_only=True)
    if SevenZipInstaller.Exists():
        SevenZipInstaller.WaitNot('visible', timeout=20)

    if '7-Zip 9.20 (x64 edition)' not in ProgramsAndFeatures.FolderView.Texts():
        print('OK')
finally:
    NewWindow.Close()