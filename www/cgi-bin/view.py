import pickle,sys,io,random,os
from fieldStorage import FieldStorage

print("Content-Type: text/html,charset=utf-8")
print()   
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8_sig')
form = FieldStorage()
homepath=os.path.expanduser("~")
with open(homepath+"/.homeworkChecker/key","rb") as f:
    key=pickle.load(f)
if form.getvalue("loggedInPass")!=key:
    print("<!doctype html><title>エラー</title><meta http-equiv=\"refresh\" content=\"5;URL=/check.html\"><p>2台同時に見ようとしたか、エラーが発生しました。</p><p>5秒後に<a href=\"/check.html\">パスワード入力画面</a>に戻ります。<p><hr><details><summary style='cursor:pointer;'>上級者向け</summary><p>アクセスごとに発行されるkeyが無効または入力されていないです。また、keyは1つしかないため、複数台同時にアクセスするとそのkeyが無効になり、この画面が表示されます。</p></details")
else:
    try:
        letters="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCBVNM12346579890" #make key
        key2=""#
        for i in range(100):#
            key2+=letters[random.randrange(63)]#
        with open(homepath+"/.homeworkChecker/key2","wb") as f:#
            pickle.dump(key2,f)#
        with open(homepath+"/.homeworkChecker/results/"+form.getvalue("date").replace("-","/")+".txt", mode="rt") as f:#
            who=""
            for i in f.readlines():
                who+="<li>"+i+"</li>"
            #who=f.read().replace("\n","<li>")#
        print("""<!doctype html>
        <html>
        <head>
        <link rel="icon" href="/icon.png">
        <title>先生・秘書係専用ページ</title>
        <meta charset="utf-8">
        </head>
        <body>
        <a href="/"><img src="/logo.png" alt="ロゴ「宿題、出した?」"></a>
        <h2>"""+form.getvalue("date")+"""に出した人 (ID) 一覧</h2>
        <p><ul>"""+who+"""</ul></p>
        <form method="POST" action="/cgi-bin/check.py">
        <input type="hidden" name="key" value='"""+key2+"""'>
        <input type="submit" value="戻る">
        </form>
        <script>
        history.pushState(null, null, location.href);
        window.addEventListener('popstate', (e) => {
          history.go(1);
        });
        </script>
        </body>
        </html>""")
    except FileNotFoundError:
        print("<title>見つかりません</title><meta http-equiv=\"refresh\" content=\"5;URL=/cgi-bin/check.py?key="+key2+"\"><p>この日のデータがありません。</p><p>5秒後に<a href=\"/cgi-bin/check.py?key="+key2+"\">日付選択画面</a>に戻ります。<p>")