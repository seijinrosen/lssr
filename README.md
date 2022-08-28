# lssr

Alternative ls command.

[![PyPI](https://img.shields.io/pypi/v/lssr)](https://pypi.python.org/pypi/lssr)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lssr)](https://pypi.python.org/pypi/lssr)
[![Tests](https://github.com/seijinrosen/lssr/actions/workflows/tests.yml/badge.svg)](https://github.com/seijinrosen/lssr/actions/workflows/tests.yml)
[![CodeQL](https://github.com/seijinrosen/lssr/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/seijinrosen/lssr/actions/workflows/codeql-analysis.yml)
[![codecov](https://codecov.io/gh/seijinrosen/lssr/branch/main/graph/badge.svg)](https://codecov.io/gh/seijinrosen/lssr)
[![Downloads](https://pepy.tech/badge/lssr)](https://pepy.tech/project/lssr)
[![Downloads](https://pepy.tech/badge/lssr/month)](https://pepy.tech/project/lssr)
[![Downloads](https://pepy.tech/badge/lssr/week)](https://pepy.tech/project/lssr)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## インストール

Python 3.7 以上がインストールされていれば利用可能です。

```sh
pip install lssr
```

## 使い方

```sh
# カレントディレクトリにあるアイテムを表示
lssr

# 指定したディレクトリにあるアイテムを表示（相対パス）
lssr path/to/target/dir

# 絶対パスでの指定
lssr /absolute/path/to/target/dir

# ソート順を逆にする
lssr -r
lssr --reverse path/to/target/dir

# 最終内容更新時刻順の新しい順にソート
lssr -t
# 古い順
lssr -tr

# ファイルサイズの大きい順にソート
lssr -S
# 小さい順
lssr -rS

# オプションの並び順は、ある程度自由です
lssr -t path/to/target/dir --reverse

# ヘルプを表示
lssr -h
lssr --help

# バージョンを表示
lssr -V
lssr --version
```

## `ls` コマンドとの違い

- アイテムの並び順が異なります。デフォルトで、以下の順序でアイテムが表示されます。
  - フォルダ -> ファイル
  - Unicode

  つまり、GitHub と同様の並び順になるはずです。

- ドットファイルを含んだリスト形式でのカラー表示がデフォルトです（`ls -AGl` と同等）。
- 現在、パスを2つ以上指定することはできません。その代わり、オプションの指定はパスの前後どちらでも良いです。
- 多くのオプションがまだ実装されていません。利用できるオプションは上記「使い方」やヘルプコマンドを参照してください。
