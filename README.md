# pandoc-hateblo: はてなブログ用Pandocフィルタ

はてなブログのMarkdown記法をサポートする、Pandoc用のフィルタです。

## 必要なもの

- Pandoc
    - Mac: `$ brew install pandoc`
    - Windows: [ダウンロードページ](https://github.com/jgm/pandoc/releases/latest)からダウンロード・インストール
- Stack (Haskell用ビルドツール)
    - Mac: `$ brew install haskell-stack`
    - Windows: [こちらを参照](https://docs.haskellstack.org/en/stable/install_and_upgrade/#windows)

## ビルド・インストール

```
$ git clone https://github.com/sky-y/pandoc-hateblo.git
$ cd pandoc-hateblo
$ stack setup
$ stack build
$ stack install
```

`stack install`により、`~/.local/bin`にバイナリがコピーされます。

（`~/.local/bin`に.bashrcや.zshrcなどに`PATH`を設定することをおすすめします）

## やること

- 見出しを`h3`がトップになるようにする
- `h3`から`h5`までを見出しとし、それより低いレベルの見出しをただの段落（テキスト）にする

## 使い方

```
pandoc input.hoge --filter hateblo -o output.md
```

## ラッパースクリプト: opml2hateblo

WorkFlowyなどのアウトライナー（OPML形式でエクスポート）をPandocではてなブログMarkdownに変換するスクリプトです。

（Pandocが余計に付けるバックスラッシュも除去します）

```
$ opml2hateblo input.opml
```

同様に、`~/.local/bin`(あるいは`PATH`の通っているディレクトリ)にコピーするか、シンボリックリンクを張ることをおすすめします。

## ライセンス

MIT