from bs4 import BeautifulSoup

with open("./tmp.xml") as fp:
    soup = BeautifulSoup(fp,features="xml")

questions = soup.find('library').find_all('question')


N = 16

def print_sol(q):
    solution = q.find('solution')
    print( "<details open><summary>Sol.</summary>\n<p>" + solution.text + "</p>\n</details>\n")

def print_parta( q ):
    content = q.find('questionContent')
    qtype = q.find('type').text
    print( "<li>\n<p>" + content.text + "</p>\n</li>")
    if qtype=='mc' or qtype=='sc':
        options = q.find_all('option')
        print("<ol>")
        for o in options:
            print("<li>"+ o.text +"</li>" )
        print("</ol>")

    print_sol( q )

def print_partb( q ):
    content = q.find('questionContent')
    print( "<p><b>B"+str(i-9)+".</b>" + content.text + "</p>\n")
    print_sol( q )


for i in range(10):
    q = questions[i]
    if i == 0:
        print("<ol>")
    print_parta( q )
    if i == 9:
        print("</ol>")

'''

for i in range(10,N):
    q = questions[i]
    if i == 10:
        print("Subjective Questions\n---\n")

    print_partb( q )

'''


