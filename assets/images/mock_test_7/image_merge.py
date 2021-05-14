import os
import subprocess
from pathlib import Path


#os.system("ls -1")

#rawout = subprocess.check_output(['ls -d'])

names = next(os.walk('.'))[1]
names.sort()




for name in names:
    for i in range(1,7):
        cmd = "convert "+ name + "/B"+str(i)+"* -append" + " " + name + "/B"+str(i)+".jpg"
        is_present = len(list(Path(name).glob("B"+str(i)+"*")))>0
        if is_present:
            print cmd
            os.system(cmd)


