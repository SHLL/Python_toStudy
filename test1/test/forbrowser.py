import webbrowser
import webbrowser as web
import time
def forin(x,y,z):
    for j in range(int(x), int(y)):
        web.register('chrome', None, webbrowser.BackgroundBrowser(z))
        url = '192.168.44.' + str(j)
        time.sleep(1)
        web.get('chrome').open_new_tab(url)

first = input('first var:')
double = input('double var:(input var + 1 )')
path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
forin(first,double,path)







