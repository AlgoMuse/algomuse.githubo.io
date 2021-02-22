import os
import subprocess


#os.system("ls -1")

rawout = subprocess.check_output(['ls'])

names = rawout.split("\n")
print names, type(names)



for name in names[:-1]:
    for i in range(1,7):
        cmd = "convert "+ name + "/B"+str(i)+"-* -append" + " " + name + "/B"+str(i)+".jpg"
        print cmd
        os.system(cmd)


