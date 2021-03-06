import os
import subprocess


#os.system("ls -1")

rawout = subprocess.check_output(['ls'])

names = rawout.split("\n")
print names, type(names)



for i in range(1,7):
    cmd = "convert "+  "./B"+str(i)+"*jpg -append" + " " + "B"+str(i)+".jpg"
    print cmd
    os.system(cmd)


