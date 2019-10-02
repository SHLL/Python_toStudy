import winreg
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key,"Desktop")[0]

path = get_desktop()

def text_creation():
    for name in range(1,2):
        with open(path + str(name) + '.text','w') as text:
            text.write(str(name))
            text.close()
            print('Done')

text_creation()