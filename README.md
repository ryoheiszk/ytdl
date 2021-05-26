# R's YouTube Downloader

使用の際は適法性の検討を欠かさずに。

## Exeファイルによる実行

1. `ytdl_data.json`を編集
2. `ytdl.exe`を実行

エラーが発生した場合、Pythonファイルによる実行を試す。

## Pythonファイルによる実行

1. Pythonをインストール

2. `youtube-dl`をインストール
  `pip install youtube-dl`

3. `ytdl_data.json`を編集

4. `main.py`を実行
  `python main.py`

エラーが発生した場合、下記のコマンドを実行する。

```bash
pip install --upgrade pip
pip install --upgrade youtube-dl
```

## コンパイル方法

下記のワンライナーを実行する。
これは2021-05-26現在での情報であるため、最新は下記参考ページを参照されたし。

```bash
docker run --rm -v "$(pwd):/src/" --entrypoint /bin/sh cdrx/pyinstaller-windows -c \
  "pip install -r requirements.txt && \
  pyinstaller main.py --onedir --onefile --clean && \
  mv dist/main.exe main.exe && \
  rm -rf __pycache__/ build/ dist/ && \
  rm -f main.spec"
```

参考: <https://qiita.com/ryoheiszk/items/2ea26594d24304c721e2>
