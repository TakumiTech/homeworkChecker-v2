import datetime,os,sys,io
from fieldStorage import FieldStorage

print("Content-Type: text/html,charset=utf-8_sig")
print()   
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8_sig')
form = FieldStorage()
id = form.getvalue("id")

date = datetime.datetime.now()
if len(str(date.month))==1:
    m="0"+str(date.month)
else:m=str(date.month)
if len(str(date.day))==1:
    d="0"+str(date.day)
else:d=str(date.day)

homepath=os.path.expanduser("~")
if not os.path.exists(homepath+"/.homeworkChecker/results/"+str(date.year)+"/"+m+"/"):
    os.makedirs(homepath+"/.homeworkChecker/results/"+str(date.year)+"/"+m+"/")

submitted=False
try:
    with open(homepath+"/.homeworkChecker/results/"+str(date.year)+"/"+m+"/"+d+".txt",mode="r") as f:
        for i in f.readlines():
            if i==id+"\n":
                submitted=True
except FileNotFoundError:
    pass

if submitted==True:
    print("""<!doctype html><html>
    <head>
    <title>提出済み</title>
    </head><body>
    <h1>提出状況</h1>
    <h2 style="text-align:center;">提出済みです</h2>
    <p>ID """+id+""" さんは既に宿題を提出しています。</p>
    <p>間違っているなら、サーバー機の日付を確認してください。</p>
    <script>function makeBlank(){
        document.open()
        document.write("")
        document.close()
    }
    const myTimeout = setTimeout(makeBlank, 5000);</script>
    </body></html>""")
else:
    with open(homepath+"/.homeworkChecker/results/"+str(date.year)+"/"+m+"/"+d+".txt",mode="a") as f:
        f.write(id+"\n")
    print("""<!doctype html><html>
    <head>
    <title>提出完了</title>
    </head><body>
    <h1>提出状況</h1>
    <h2 style="text-align:center;">チェックしました</h2>
    <p>ID <b>"""+id+"""</b> さんは宿題を出したとします。</p>
    <script>function makeBlank(){
        document.open()
        document.write("")
        document.close()
    }
    const myTimeout = setTimeout(makeBlank, 5000);</script>
    </body></html>""")