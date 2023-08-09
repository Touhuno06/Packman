# Packman
本プロジェクトではpythonを用いてコンソール上で動作するパックマンを作成した。


## Requirement
- pythonのバージョン：python 3.10


## Installation
- 各種モジュールのインストール
```shell
pip install -r requirements.txt
```


## Usage
- mainプログラムの実行.
```shell
python main.py
```


## Directory Structure
- プロジェクトの構成は以下の通り.
```shell
.
|-- README.md           
|-- controller.py       #描画処理を行うファイル
|-- game.py             #ゲーム全体の動作ファイル
|-- ghost.py            #ゴーストの動作ファイル
|-- main.py             #実行ファイル
|-- map.py              #マップの生成及び判定のファイル
|-- player.py           #プレイヤ―の動作ファイル
`-- requirements.txt    
```