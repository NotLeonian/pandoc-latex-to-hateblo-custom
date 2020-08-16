# pandoc-hateblo: はてな記法用pandocフィルタ

はてなブログのはてな記法に変換するフィルタ

## 要件

- Python 3.8
- [panflute](http://scorreia.com/software/panflute/) 1.12.5
- Pandoc 2.9.2.1
- pandoc-crossref 0.3.6.4
- Stack 2.3.3 くらい
- bash の使える環境

## インストール方法

1. 適当なディレクトリに移動して

```sh
git clone git@github.com:Gedevan-Aleksizde/pandoc-hateblo.git
git checkout hatena-filter
export PATH=<ここにpandoc-hateblo/binのパス>:${PATH} >> ~/.bashrc
```

2. はてなフォトライフのAPIキーを取得して, 設定ファイル `settings.json` に書き込んでおく. `blog_name` は人によっては違う形式になるはず. `FOTO_FOLDER` は画像のアップロード先.

```
{
  "FOTO_API_KEY": "XXXXXX",
  "HATENA_USER": "YYYYY",
  "HATENA_BLOG": "YYYYY.hatenablog.com",
  "FOTO_FOLDER": "ZZZZ"
}
```

もしくは上記のようなファイルをカレントディレクトリに置く, または各パラメータと同名の環境変数を設定して実行する.


## 主な機能

* 図表キャプションへの自動付番
* 数式, 引用文献, 図表の相互参照にアンカーリンク自動付与
* はてな記法による脚注, ハイパーリンク, コードブロック, 引用ブロックなどへの変換

## 使い方

以下のようなコマンドで変換する. [...] はオプション. ただし現時点では変換対象ファイルのディレクトリで実行

```
latex2hatena.sh [-o OUTPUT.html] [--bibliography=CITATIONS.bib] [--csl=CSL.csl] INPUT.tex
```