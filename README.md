# pandoc-latex-to-hateblo-custom: LaTeXからはてな記法への変換用Pandocフィルタ

自分が使いやすいようにするためだけのフォークである.
upstream からは以下のような変更を行っている.

- apt や Homebrew などでインストールできる `pandoc` と `pandoc-crossref` で動作するように変更.
- Python のパッケージマネージャとして `uv` を導入.
- はてなブログの「tex記法」は MathJax v2 を使用するため, 環境によっては数式の表示が崩れる.
  - 代わりに KaTeX を使用する.
  - 「ブログを管理」→「設定」→「詳細設定」から, 「`<head>`要素にメタデータを追加」の欄に `hateblo_script.html` の内容をペーストする必要がある.
    その際「[利用上の注意](https://help.hatenablog.com/entry/developer-option)」を確認すること.
    また, KaTeX のバージョンも適宜書き換えること.
- 数式中の一部の文字に対してエスケープシーケンスを使用するように変更.
- 英数字と CJK 文字の間にスペースが入るように変更.

また, upstream の `README.md` も参照するとよい.
