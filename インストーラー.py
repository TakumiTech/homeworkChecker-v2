#!/usr/bin/python
#このインストーラーを実行するにはPythonのインストールが必要です。
#Pythonをインストールしてください
#https://python.org
counter=1
def gui():
    def rGo(): #連続
        try:
            set(range(int(se.get()),int(ee.get())))
            messagebox.showinfo("完了!","連続モードでのセットアップが完了しました。個別モードでのセットアップが完了しました。フォルダに1.jpg, 2.jpgを追加してください。")
            window.destroy()
        except:
            messagebox.showerror("エラー","エラーが発生しました。入力したものが数字であるかをもう一度確認してください。")
    window=tk.Tk()
    window.title("【作者公式】宿題、出した? インストーラー")

    tk.Label(text="連続モード").grid(column=0,row=0,columnspan=2)
    tk.Label(text="はじめ").grid(column=0,row=1)
    se=tk.Entry()
    se.grid(column=1,row=1)
    tk.Label(text="おわり").grid(column=0,row=2)
    ee=tk.Entry()
    ee.grid(column=1,row=2)
    counter=1
    btnlist=[]
    tk.Button(text="セットアップ開始!",command=rGo).grid(column=0,row=3,columnspan=2)
    def kGo():
      getlist=[]
      for i in btnlist:
        getlist.append(i.get())
      set(getlist)
      messagebox.showinfo("完了!","個別モードでのセットアップが完了しました。フォルダに1.jpg, 2.jpgを追加してください。")
      window.destroy()
    def createEntry():
      global counter
      tmpEntry=tk.Entry()
      btnlist.append(tmpEntry)
      tmpEntry.grid(column=2,row=counter)
      newBtn.grid(column=2,row=counter+1)
      startBtn.grid(column=2,row=counter+2)
      counter+=1
      print("created entry. btnlist is",btnlist)
    tk.Label(text="個別モード").grid(column=2,row=0,columnspan=2)
    startBtn=tk.Button(text="セットアップ開始!",command=kGo)
    newBtn=tk.Button(text="1個追加",command=createEntry)
    createEntry()
    window.mainloop()

def cui():
    print("\n　　　宿題、出した? インストーラー")
    print("CTRL+Cを押すと終了できます。")
    print("\n\nモードを選択してください (番号+Enter)")
    c=input("1: 連続モード (1から5、など、数字のみ)\n2: 個別モード (A, B, C, D, E など)\n> ")
    if c=="1" or c =="１":
        start=input("最初のID (例: 000)> ")
        end=input("終わりのID (例: 999)> ")
        try:
            set(list(range(int(start),int(end)+1)))
        except (TypeError,ValueError) as e:
            print("数字を入力してください",e)
    elif c=="2" or c=="２":
        print("使う人全員のIDを入力してください (Enterで1人確定)")
        users=[]
        while True:
            name=input("次のユーザーのIDを入力してください (空白のままEnterで終了)> ")
            if name=="":
                break
            else:
                users.append(name)
        set(users)
    else:
        print("1か2を入力してください")
        cui()

def set(users:list):
    import os
    homedir=os.path.expanduser("~").replace("\\","/")
    os.chdir(homedir+"/.homeworkChecker/www/assets")
    print("作成中です...")
    for i in users:
        try:
            os.mkdir(str(i))
        except FileExistsError:
            pass
    with open(os.path.expanduser("~")+"/.homeworkChecker/www/index.html",mode="w",encoding="utf-8") as f:
        f.write("""<!doctype html>
<html lang="en"><head>
    <meta charset="utf-8">
    <title>宿題、出した?</title>
    <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <link rel="icon" href="/icon.png" type="image/png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Yomogi&display=swap" rel="stylesheet">
    <link rel="stylesheet" as="style" href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic">
  <style>
  h1,h2,h3,h4,h5,h6,p,label{
    font-family: 'Yomogi', cursive;
  }
  p{ font-size:20px; }
  * {
    text-align: center;
    margin-left: auto;
    margin-right: auto;
  }
  @media (prefers-color-scheme: dark) { /* dark mode*/
    body{
      background: #272727;
      color: white;
    }
    #logo{
      background-image: url("/logoDark.png");
    }
  }
  body{
    background: rgb(174,217,255);
    background: linear-gradient(99deg, rgba(174,217,255,1) 0%, rgba(235,247,255,1) 100%);
  }
  </style></head>
<!--body-->
  <body>
    <noscript>
      <style>
        #pop-up2:checked + .overlay2 {
	        display: block;
	        z-index: 9999;
	        background-color: #00000070;
	        position: fixed;
	        width: 100%;
	        height: 100vh;
	        top: 0;
	        left: 0;
        }
        .window2{
	        position: fixed;
	        top: 50%;
	        left: 50%;
          transform: translate(-50%, -50%);
          background:lightyellow;
        }
        .overlay2 {
	        display: none; /* xで消えるように */
        }
        #video{
          display: none !important;
        }
      </style>
      <input type="checkbox" id="pop-up2" checked style="display: none;">
      <div class="overlay2">
        <div class="window2">
          <h2>お使いのブラウザでは利用できません</h2>
          <p>お使いのブラウザはJavaScriptに対応していないかオフになっているため、顔認証やQRコードスキャンナーを利用できません。</p>
          <p>最新版の<a href="microsoft-edge:http://localhost">Microsoft Edge</a>をの利用をお勧めします。</p>
          <p><a href="https://www.microsoft.com/ja-jp/edge/download" target="_blank">Microsoft Edgeをダウンロード</a></p>
          <p><a href="https://youtu.be/BovYk73Uwsg" target="_blank">Microsoft EdgeでJavaScriptを有効にする方法</a></p>
          <label style="cursor:pointer;border:2px solid black; background-color: lightgray;" for="pop-up2">閉じる</label>
        </div>
      </div>
    </noscript><!--end noscript-->
    <img src="/logo.png" alt="ロゴ「宿題、出した?」" id="logo">
        <div style="position:relative;width:640px;height:480px;margin-left: auto;margin-right: auto;" id="container">
          <video id="video" style="position: relative;" muted autoplay width="640" height="480"></video>
          <canvas id="facecanvas" style="position: absolute;top:0px;right:0px;" width="640" height="480"></canvas>
          <iframe height="480" name="frame" style="position:absolute;border:none;">お使いのブラウザはiframeに対応していないため、送信ができません。</iframe>
        </div>
        <div id="sourceSelectPanel" style="display:none"> <!--wil show when cam is detected-->
            <label for="sourceSelect">カメラ</label>
            <select id="sourceSelect" style="max-width:400px"></select>
          </div>
          <form style="font-size:30px;" action="/cgi-bin/submit.py" id="form" method="POST" target="frame">
            <label for="input">ID: </label><input required autofocus placeholder="手動入力もOK!" style="font-size:30px;" id="input" name="id" autocomplete="off" onblur="this.select()">
            <input style="font-size:30px;cursor:pointer;" type="submit" value="GO!!!"> </form>
          <hr><p><a href="check.html">【先生・秘書係専用】出した人を見る</a></p>
          <canvas id="canvas2" style="display:none;"></canvas>
    <!--below javascript etc-->
    <script type="text/javascript" src="https://unpkg.com/@zxing/library@latest"></script>
    <script src="/js/face-api.js"></script>
    <script type="text/javascript"> 
      window.addEventListener('load', function () {
        console.log('%c ', `background-image: url("/icon.png");background-size: contain;background-position: center center;background-repeat: no-repeat;padding-right: 100px;padding-bottom: 121px;`);
        console.log("%cこんなところまでついついチェックしてしまうアナタ!!\n僕の恥ずかしい (?) コンソールへようこそ。\n英文とエラーばかりのコンソールで申し訳ございません。\n\nコンソール読者(?)限定! Google検索の裏技です!!\nGoogle英語版で\"text adventure\"と検索し、コンソールで\"yes\"と入力するとゲームを遊べます。\n日本語版で検索すると出てこないので注意してください。\nhttps://www.google.com/search?q=text+adventure&hl=en\n\nそれでは。","font-family:sans-serif;font-size:17px;")
        if(/MSIE/i.test(navigator.userAgent)) { //IE11 does not qualify
            console.log("Detected unsupported browser: " + navigator.userAgent);
            window.location="microsoft-edge:http://localhost/";
        }

        let selectedDeviceId;
        const codeReader = new ZXing.BrowserQRCodeReader()
        console.log('QR Code scanner open')
        codeReader.getVideoInputDevices()
          .then((videoInputDevices) => {
            const sourceSelect = document.getElementById('sourceSelect')
            selectedDeviceId = videoInputDevices[0].deviceId
            if (videoInputDevices.length >= 1) {
              videoInputDevices.forEach((element) => {
                const sourceOption = document.createElement('option')
                sourceOption.text = element.label
                sourceOption.value = element.deviceId
                sourceSelect.appendChild(sourceOption)
              })
  
              sourceSelect.onchange = () => {
                selectedDeviceId = sourceSelect.value;
              };
  
              const sourceSelectPanel = document.getElementById('sourceSelectPanel')
              sourceSelectPanel.style.display = 'block'
            }
          
          codeReader.decodeFromInputVideoDeviceContinuously(selectedDeviceId, 'video', (result, err) => {
          if (result) {
            // qr code decoded
            console.log('Found QR code!', result)
            document.getElementById("input").value=result.text
            document.getElementById("form").submit()
          }
          if (err) {
            // Excepted Exceptions:
            //
            //  - NotFoundException
            //  - ChecksumException
            //  - FormatException
  
            //if (err instanceof ZXing.NotFoundException) {
            //  console.log('No QR code found...')
            //}
            if (err instanceof ZXing.ChecksumException) {
              console.log('A code was found, but it\'s read value was not valid.')
            }
            if (err instanceof ZXing.FormatException) {
              console.log('A code was found, but it was in a invalid format.')
            }
          }})
  
              console.log(`Started scanning with camera with id ${selectedDeviceId}`)
          })
          .catch((err) => {
            console.error(err)
          })
      })
      </script><script>
      //below face-api
      let image;
      let canvas;
      Promise.all([
        faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
        faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
        faceapi.nets.ssdMobilenetv1.loadFromUri('/models'),
        faceapi.nets.tinyFaceDetector.loadFromUri("/models")
      ]).then(start)
      async function look(){
        //if (image) image.remove()
        //if (canvas) canvas.remove()
        //image = await faceapi.bufferToImage(convert())
        //canvas = faceapi.createCanvasFromMedia(image)
        const labeledFaceDescriptors = await loadLabeledImages()
        const faceMatcher = new faceapi.FaceMatcher(labeledFaceDescriptors, 0.6)
        //convert()
        const canvas2=document.getElementById("canvas2")
        const video=document.getElementById("video")
        canvas2.setAttribute('width', video.width)
        canvas2.setAttribute('height', video.height)
        //canvas2.setAttribute('style','display:none;')
        canvas2.getContext('2d').drawImage(video, 0, 0, video.width, video.height)
        console.log("drawed image to canvas2")
        //console.log(canvas2.toDataURL())
        const displaySize = { width: canvas2.width, height: canvas2.height }
        console.log("canvas2 width: "+canvas2.width+"\ncanvas2 height: "+canvas2.height)
        //faceapi.matchDimensions(canvas2, displaySize)
        const detections = await faceapi.detectAllFaces(canvas2,new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceDescriptors()
        console.log(detections)
        console.log(detections.length)
        const resizedDetections = faceapi.resizeResults(detections, displaySize)
        console.log(resizedDetections)
        const results = resizedDetections.map(d => faceMatcher.findBestMatch(d.descriptor))
        console.log(results)
        console.log("results in str is "+toString(results))
        console.log("found "+results.length+" people")
        results.forEach((result, i) => {
          const box = resizedDetections[i].detection.box
          const stringResult=result.label
          const drawBox = new faceapi.draw.DrawBox(box, { label: stringResult })
          console.log("found "+stringResult)
          if (stringResult=="unknown"){
            console.log("found person, but cannot detect who")
          } else{
            document.getElementById("input").value=stringResult
            document.getElementById("form").submit()
            document.getElementById("input").value=""
          }
          canvas=document.getElementById("facecanvas")
          canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
          drawBox.draw(canvas)
        })
        if (results.length===0){
          canvas=document.getElementById("facecanvas")
          canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
        }
      }
      async function start() {
        const container = document.getElementById("container")
        const labeledFaceDescriptors = await loadLabeledImages()
        const faceMatcher = new faceapi.FaceMatcher(labeledFaceDescriptors, 0.6)
        console.log("face-api.js loaded")
      }

      function loadLabeledImages() {
        const labels = """+users+"""
        return Promise.all(
          labels.map(async label => {
            const descriptions = []
            for (let i = 1; i <= 2; i++) {
              const img = await faceapi.fetchImage(`/assets/${label}/${i}.jpg`)
              const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor()
              descriptions.push(detections.descriptor)
            }

            return new faceapi.LabeledFaceDescriptors(label, descriptions)
          })
        )
      }
      console.log("made all functions with the error(s) above. Now setting interval")
      console.log("interval set. ending script")
      setInterval(look,3000)
    </script>
</body></html>""")

def check(): #check if tkinter is installed
  try:
      global tk
      global messagebox
      import tkinter as tk0
      from tkinter import messagebox
      gui()
  except ModuleNotFoundError:
      print("\nTkinterが見つかりませんでした。\nGUIバージョンを希望する場合は、\nPythonインストーラー->Modify->tcl/tk and IDLE にチェック->Next->Next->Install->Close\nでTkinterをインストールしてください。")
      cui()
try:
    import sys
    args=sys.argv
    if len(args)==2:
        if args[1]=="cui":
            cui()
        else:
            check()
    else:
        check()
except Exception as e:
    print("エラーが発生したため、インストールできません。大変お手数ですが、手動でインストールを行ってください。")
    print("\nPythonに詳しい人向け: エラー内容")
    print(type(e),e)