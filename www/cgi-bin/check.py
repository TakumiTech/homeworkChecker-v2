import hashlib,random,pickle,sys,io,os
from fieldStorage import FieldStorage

print("Content-Type: text/html,charset=utf-8_sig")
print()   
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8_sig')
form = FieldStorage()
fpw=form.getvalue("pw")
if fpw!=None:
    evalue = hashlib.sha512(fpw.encode()).hexdigest()
else:
    evalue=None
ukey = form.getvalue("key")
homepath=os.path.expanduser("~").replace("\\\\","/")
with open(homepath+"/.homeworkchecker/key2","rb") as f:
    try:
        key2=pickle.load(f)
    except:
        key2=""
with open(homepath+"/.homeworkChecker/pw","rb") as f:
    pw=pickle.load(f)
if evalue==None and ukey==None:
    print("<meta http-equiv=\"refresh\" content=\"0;URL=/check.html?error=passwordNone\">")
elif evalue != pw and ukey!=key2:
    print("<meta http-equiv=\"refresh\" content=\"0;URL=/check.html?error=passwordInvalid\">")
else:
    letters="/qwerty!uiopa#sdfgh$jklzx*cvbnm&%,-.:=?@[]^_`|~QWERTY(UIOPA)SDFGH+JKLZX<CVBNM>}1234567890{\;" #make key
    key=""                                                                                                 #
    for i in range(100):                                                                                   #
        key+=letters[random.randrange(92)]                                                                 #
    with open(homepath+"/.homeworkChecker/key","wb") as f:                                                 #
        pickle.dump(key,f) #
    print("""<!doctype html>
    <html>
    <head>
    <link rel="icon" href="/icon.png">
    <title>先生・秘書係専用ページ</title>
    </head>
    <body>
    <a href="/"><img src="/logo.png" alt="ロゴ「宿題、出した?」"></a>
    <h1>出した人　一覧</h1>
    <h3>表示するには日付を選んでください。</h3>
    <form action="/cgi-bin/view.py" method="POST">
    <input type="date" required name="date" id="datePicker">
    <input type="hidden" name="loggedInPass" value='"""+key+"""'>
    <input type="submit" value="検索">
    </form>
    <script>
    const today = new Date();
    function dateFormat(today, format){
        format = format.replace("YYYY", today.getFullYear());
        format = format.replace("MM", ("0"+(today.getMonth() + 1)).slice(-2));
        format = format.replace("DD", ("0"+ today.getDate()).slice(-2));
        return format;
    }
    const yyyymmdd = dateFormat(today,'YYYY-MM-DD');
    document.getElementById("datePicker").max=yyyymmdd;
    document.getElementById("datePicker").value=yyyymmdd;
    </script>
            <div style="background-color: lightgoldenrodyellow;text-align: center;">
            <h4>⚠注意</h4>
            <p>セキュリティ上、2台以上同時に見ることはできません。(エラーが発生します｡)</p>
        </div>
    <p><a href="/">トップへ戻る</a></p>
    <p><a href="/change-password.html">パスワードを変更</a></p>
    <p><a href="/check.html">ログアウト (サインアウト)</a></p>
    </body>
    </html>
    """)