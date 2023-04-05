# 宿題、出した?
## 説明
宿題、出した？は、顔認証・QRコードで宿題を出した人を管理できるソフトウェアです。

2022年度全国選抜小学生プログラミング大会の全国大会で、優秀賞を獲得しました。プレゼンテーションは[こちら](https://youtu.be/VQ2U4-zF0E4?t=8241)

※発表終了後、司会の方が「先生方のご負担も増える」と言っていますが、正しくは「先生方のご負担が**減る**」です。

## インストール
### 動作環境
 - Windows 10 または 11
 - Macでは動作しません
 - Python 3 (インストール時に「Add python.exe to PATH」にチェックをいれてください)

以下のコマンドをコマンドプロンプトで実行してください。管理者権限は不要です。

```git clone https://github.com/TakumiTech/homeworkChecker-v2.git %userprofile%/.homeworkChecker```

実行するには、以下のコマンドを実行した後、ブラウザで```http://localhost/```にアクセスしてください。

```python -m http.server  80 --cgi -d %userprofile%\.homeworkchecker\www\```


**実行すると「Python」とだけ表示される場合は、設定アプリ→アプリ→アプリの詳細設定→アプリ実行エイリアス→アプリ インストーラー python.exe　をオフにしてください。**

### ちょっとおまけ (上級者向け)
どうしてもコントロールパネル・設定アプリのアプリ一覧に表示させたいのであれば、```HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall\homeworkChecker```に以下のレジストリを追加してください。(homeworkCheckerキーも作成してください)

| キーの名前 | 種類 | データ (値) |
|--|--|--|
| DisplayName | REG_SZ | 宿題、出した? |
| Publisher | REG_SZ | TakumiTech
| URLInfoAbout | REG_SZ | https://github.com/TakumiTech/homeworkChecker-v2 |
| DisplayVersion | REG_SZ | 2
| ModifyPath | REG_SZ | python.exe %USERPROFILE%\\.homeworkChecker\\インストーラー.py
| InstallLocation | REG_SZ | %USERPROFILE%\\.homeworkChecker
