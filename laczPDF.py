import sys
import os
import subprocess
import shutil
import tkinter
import re
from tkinter import filedialog

#################################wybór directory
root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Wybierz katlog z plikami (wieloma)')
if len(tempdir) > 0:
    print ("You chose %s" % tempdir)
directory=tempdir
##################################

currdir = os.getcwd()
tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Wybierz plik do dołączenia')
if len(tempdir) > 0:
    print ("You chose %s" % tempdir)
plik=tempdir
##################################

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

for path in os.walk(os.path.normpath(directory)):
    if not os.path.exists(path[0]+"//_zrobione//"):
        os.makedirs(path[0]+"//_zrobione//")
    string=str(path[0]).replace("/","\\")
    splt=string.split("\\")
    print (path[0])
    for filename in os.listdir(path[0]):
        if filename.endswith(".pdf"):
            shutil.copyfile(path[0]+"//"+filename,path[0]+"//_zrobione//"+filename)
            filename=path[0]+"\\"+filename
            programname= "cpdf.exe" 
            subprocess.call([resource_path(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),programname)),"-merge",filename,plik,"-o",filename])