# pandoc-hateblo: はてな記法用pandocフィルタ

texファイルをはてなブログのはてな記法に変換するフィルタ. upstream とはもはや別物になった

## システム要件

- `Python` 3.8 (.6, .7 でも使えそうだが保証も対応もしない)
- [`panflute`](http://scorreia.com/software/panflute/) 1.12.5
- `Pandoc` 2.9.2.1
- `pandoc-crossref{ 0.3.6.4 の修正版 (後述)
- `Stack` 2.3.3 くらい
- `bash` の使える環境

## インストール

1. Python, pandoc が指定のバージョンになっていることを確認する
2. `pandoc-crossref` 0.3.6.4 の私家修正版をインストールする  
この措置は `pandoc`, `pandoc-crossfef`, `panflute` の互換性がシビアだったことによるもので, panflute が最新バージョンに対応すればもう少し簡単になるはず.

```sh
git clone git@github.com:Gedevan-Aleksizde/pandoc-crossref.git
cd pandoc-crossref
git checkout 4e02b07
stack clean
stack build
stack install
```

3. 適当なディレクトリに移動して

```sh
git clone git@github.com:Gedevan-Aleksizde/pandoc-hateblo.git
git checkout hatena-filter
export PATH=<ここにpandoc-hateblo/binのパス>:${PATH} >> ~/.bashrc
```

4. はてなフォトライフのAPIキーを取得して, 設定ファイル `settings.json` に書き込んでおく. `HATENA_BLOG` は人によっては違う形式になるはず. `FOTO_FOLDER` は画像のアップロード先.

```
{
  "FOTO_API_KEY": "XXXXXX",
  "HATENA_USER": "YYYYY",
  "HATENA_BLOG": "YYYYY.hatenablog.com",
  "FOTO_FOLDER": "ZZZZ"
}
```

もしくは上記のようなファイルをカレントディレクトリに置く, または各パラメータと同名の環境変数を設定して実行する.


## 特筆すべき機能

* 図表キャプションへの自動付番 (「図1」「表2」など)
* 数式, 引用文献, 図表の相互参照に自動付番し, かつアンカーリンクを自動付与
* ローカルの画像ファイルを自動ではてなフォトライフにアップロード
* はてな記法の便利な構文, 脚注, ハイパーリンク, コードブロック, 引用ブロックなどへの変換 (全てのはてな記法に対応しているわけではない)

## 使用法

以下のようなコマンドで変換する. [...] はオプション. ただし現時点では**変換対象ファイルのディレクトリで実行する前提**

```
latex2hatena.sh [-o OUTPUT.html] [--bibliography=CITATIONS.bib] [--csl=CSL.csl] INPUT.tex
```


## 使用例

以下の投稿と [`expample`](example/) にある `main.tex`, `main.pdf` を比較してみてください.

https://ill-identified.hatenablog.com/entry/2020/08/24/132209
