import subprocess
import sys
import os

def open(url):
    """ Launches browser depending on os """

    if sys.platform=='win32':
        os.startfile(url)
    elif sys.platform=='darwin':
        subprocess.Popen(['open', url])
    else:
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            import webbrowser
            webbrowser.open(url)
