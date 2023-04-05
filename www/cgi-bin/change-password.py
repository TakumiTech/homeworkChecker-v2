import os,sys,io,hashlib,pickle
from fieldStorage import FieldStorage
print("Content-Type: text/html,charset=utf-8_sig")
print()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8_sig')
form = FieldStorage()
old=form.getvalue("oldpw")
new=form.getvalue("newpw")
invalid=False
if old==None:
    invalid=True
if new==None:
    invalid=True
old=hashlib.sha512(old.encode()).hexdigest()
new=hashlib.sha512(new.encode()).hexdigest()
with open(os.path.expanduser("~").replace("\\","/")+"/.homeworkChecker/pw",mode="rb") as f:
    oldpw=pickle.load(f)
if oldpw!=old:
    invalid=""

if invalid==False:
    with open(os.path.expanduser("~").replace("\\","/")+"/.homeworkChecker/pw",mode="wb") as f:
        pickle.dump(new,f)
        print("<!doctype html><html><head><title>パスワードが変更されました</title><meta http-equiv=\"refresh\" content=\"5;URL=/check.html\"></head><body><p>パスワードが変更されました。</p><p>5秒後に<a href=\"/check.html\">パスワード入力画面</a>に戻ります。</p></body></html>")
elif invalid==True:
    print("<meta http-equiv=\"refresh\" content=\"0;URL=/change-password.html?error=error\">")
elif invalid=="":
    print("<meta http-equiv=\"refresh\" content=\"0;URL=/change-password.html?error=oldPasswordInvalid\">")
else:
    print("原因不明のエラーが発生しました。開発者にご連絡していただけると幸いです。<br>")