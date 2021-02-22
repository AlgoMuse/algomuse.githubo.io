import os
import subprocess
import csv
from operator import itemgetter



point = { }

with open('scorecard.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        total = 0
        if line_count == 0:
            line_count += 1
        else:
            title = row[2].replace(" ","_")
            point[ title ] = [int(row[3])]
            total += int(row[3])
            for i in range(4,10):
                if row[i].isalpha():
                    point[title].append( 0  )
                else:
                    point[title].append( int(row[i]) )
                    total += int(row[i])
            point[title].append( total )
            line_count += 1
            #print title,point[title]


#exit(0)


#os.system("ls -1")

sorted_tuples = sorted(point.items(), key=lambda item: (-item[1][7],item[1][0]) )
#print(sorted_tuples)

sorted_point = {k: v for k, v in sorted_tuples}


#print sorted_tuples


#exit(0)


rawout = subprocess.check_output(['ls'])

names = rawout.split("\n")
#print names, type(names)


#print point.keys(), "\n" , names[:-1]

#exit(0)

count = 0

for obj in sorted_tuples:

    name = obj[0]
    count += 1

    if os.path.isdir(name):
        fname = name+"/PartA.jpg"
        if os.path.isfile(fname):
            print "<button class=\"markbutton rank\">"+str(count)+". </button>"
            print "<input type=\"button\" class=\"markbutton white\" value=\""+name.replace("_"," ")+"\"/>"
            print "<button class=\"markbutton blank\" onclick = \"markdisplay(\'"+name+"/PartA\')\">"+str(point[name][0])+"</button>"
            print "<button class=\"button white\"></button>"

        for i in range(1,7):
            fname = name+"/B"+str(i)
            if os.path.isfile(fname+".jpg"):

                verdict = "right"
                if point[name][i]<4:
                    verdict="wrong"
                print "<button class=\"markbutton "+verdict+"\" onclick = \"markdisplay(\'"+fname+"\')\">"+ str(point[name][i]) +"</button>"

            else:
                print "<button class=\"button blank\"></button>"

        print "<button class=\"markbutton total\">"+str(point[name][7])+"</button>"


'''

<input type="button" class="markbutton white" value="Maryam&nbsp;Mirzakhani"/>
<button class="markbutton blank" onclick="location.href='/docs/trigonometry/#an-easy-problem';" onmouseover = "markdisplay('PartA')">&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp;</button>
<button class="markbutton white" onclick="location.href='/docs/trigonometry/#an-easy-problem';" onmouseover = "markdisplay('A1_2010')"> </button>
<button class="markbutton right" onclick="location.href='/docs/algebra/polynomials/#parity-of-a-polynomial';" onmouseover = "markdisplay('B1')">6</button>
<button class="button blank"></button>
<button class="markbutton blank" onclick="location.href='/docs/combinatorics/#progression-of-squares';" onmouseover = "markdisplay('A4_2010')">4</button>
<button class="markbutton wrong" onclick="location.href='/docs/number_theory/modulo_arithmetic/#fermats-little-theorem';" onmouseover = "markdisplay('A5_2010')">9</button>
<button class="markbutton blank" onclick="location.href='/docs/combinatorics/#progression-of-squares';" onmouseover = "markdisplay('A4_2010')">4</button>
<button class="markbutton wrong" onclick="location.href='/docs/number_theory/modulo_arithmetic/#fermats-little-theorem';" onmouseover = "markdisplay('A5_2010')">9</button>

'''


