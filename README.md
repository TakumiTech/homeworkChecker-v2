# 宿題、出した?
## 説明
宿題、出した？は、顔認証・QRコードで宿題を出した人を管理できるソフトウェアです。

2022年度全国選抜小学生プログラミング大会の全国大会で、優秀賞を受賞しました。プレゼンテーションは[こちら](https://youtu.be/VQ2U4-zF0E4?t=8241)

※発表終了後、司会の方が「先生方のご負担も増える」と言っていますが、正しくは「先生方のご負担が**減る**」です。

## インストール
### 動作環境
 - Windows 10 または 11
 - Macでは動作しません
 - [Python 3](https://python.org/downloads/) (インストール時に「Add python.exe to PATH」にチェックをいれてください)

以下のリンクからインストーラー(exe)をダウンロードしてください。警告が出るかもしてませんが、安全です。
 - [64bit版](https://takumitech.github.io/homework-install-x64-signed.exe)
 - [32bit版](https://takumitech.github.io/homework-install-x86-signed.exe)

また、以下のコマンドをコマンド プロンプトで実行してインストールすることも可能です。管理者権限は不要です。この場合、[Git](https://git-scm.com/download/win)を事前にインストールする必要があります。

```git clone https://github.com/TakumiTech/homeworkChecker-v2.git %userprofile%/.homeworkChecker```

## 実行方法

実行するには、以下のコマンドを実行した後、ブラウザで```http://localhost/```にアクセスしてください。
%UserProfile%\.homeworkChecker\サーバーを立ち上げる.lnk からも実行できます。

```python -m http.server 80 --cgi -d %userprofile%\.homeworkchecker\www\```


宿題を出した人を確認するときの初期パスワードは「Homework」です。ログイン後に、変更できます。

## トラブルシューティング
| 質問 | 解決策 |
| ----- | ----- |
| Microsoft Edgeで、「homework-install-x64 (86).exeは一般的にダウンロードされていません。...」と表示される | 右側の…から保存を選択し、詳細表示をクリック。その後、「保持する」をクリックしてください。このファイルは署名がされていないため発行元は不明となっていますが、安全です。 |
| Google Chromeで、「homework-install-....exeは危害を及ぼす可能性があります。Googleに送信してスキャンしますか?」と表示される。 | 「送信」をクリックまたは右の矢印をクリックし、「開く」を選択。 |
| 実行すると「WindowsによってPCが保護されました」と表示される | 「詳細情報」をクリックした後、「実行」をクリックしてください。 |
| コマンドでインストールしようとすると、```'git' は、内部コマンドまたは外部コマンド、操作可能なプログラムまたはバッチ ファイルとして認識されていません。```と表示される | gitをインストールしてください。 |
| 2つ目のコマンドを実行すると、「Pythonとだけ表示される | 設定アプリ→アプリ→アプリの詳細設定→アプリ実行エイリアス→アプリ インストーラー python.exe　をオフにしてください。 |
| コマンド プロンプトって、どこから開ける? | 画面下の検索ボックスで、「コマンド プロンプト」や「cmd」などと検索してみてください。 |
| 顔認証されない | インストーラーを使ってフォルダを作成し、そこに2枚の顔写真を登録してください。ファイル名は、```1.jpg```と```2.jpg```にしてください。 |
| 宿題を出した人を確認したいのですが、パスワードが分かりません。 | 初期パスワードは「Homework」ですが、変更された可能性もあります。大文字・小文字・半角全角も区別します。 |
| 宿題を出す・出した人を確認するのは、コマンドを実行していない端末でもできますか。 | はい。設定アプリからIPアドレスを確認し、同じWi-Fiに接続している端末からそのIPアドレスにアクセスしてください。読み込みが遅い場合、セキュリティをオフにしてみてください。 |
 
## ちょっとおまけ (上級者向け)
どうしてもコントロールパネル・設定アプリのアプリ一覧に表示させたいのであれば、```HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall\homeworkChecker```に以下のレジストリを追加してください。(homeworkCheckerキーも作成してください)

| キーの名前 | 種類 | データ (値) |
|--|--|--|
| DisplayName | REG_SZ (文字列値) | 宿題、出した? |
| DisplayIcon | REG_SZ (文字列値) | %USERPROFILE%\.homeworkChecker\icon.ico |
| Publisher | REG_SZ (文字列値) | TakumiTech |
| URLInfoAbout | REG_SZ (文字列値) | https://github.com/TakumiTech/homeworkChecker-v2 |
| DisplayVersion | REG_SZ (文字列値) | 2 |
| ModifyPath | REG_SZ (文字列値) | cmd /c "python.exe %USERPROFILE%\.homeworkChecker\インストーラー.py" |
| InstallLocation | REG_SZ (文字列値) | %USERPROFILE%\\.homeworkChecker |

## 使用API
 - [face-api.js](https://github.com/justadudewhohacks/face-api.js)
 - [ZXing](https://github.com/zxing-js/library)
 - [Python http.server (旧SimpleHTTPServer)](https://docs.python.org/ja/3/library/http.server.html)
