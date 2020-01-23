import os
import webbrowser

dir_path = os.path.dirname(os.path.realpath(__file__))

cmd = 'powercfg /batteryreport'
os.system(cmd)

path = str(dir_path) + "\\battery-report.html"

webbrowser.open(path, new=2)