# グラフ描画

## 1. 仮想環境の構築

```bash
# フォルダに移動
cd graph-training

# 仮想環境作成 + パッケージインストール
uv sync
```

## 2. VSCodeでの設定

1. VSCodeでフォルダを開く
2. Python拡張が`.venv`の仮想環境を自動検出します
3. 右下に表示されるPythonバージョンが`.venv`のものか確認
4. 自動検出されない場合は、`Ctrl+Shift+P` → "Python: Select Interpreter" → `.venv\Scripts\python.exe`を選択

## 3. 動作確認

`sample.py`を実行してグラフが表示されればOK！

---

## 仮想環境って何？

仮想環境は、プロジェクトごとに独立したPython環境を作る仕組みです。

- 他のプロジェクトと依存関係が競合しない
- チーム全員が同じ環境で作業できる
- システム全体のPythonを汚さない

## uv syncで何が起こる？

- `pyproject.toml` と `uv.lock` を読み取り
- `.venv` フォルダに仮想環境を作成
- 必要なパッケージ（matplotlib, numpy, pandas）を自動インストール
- バージョンを固定して再現可能な環境を構築

## トラブルシューティング

**PowerShellでuvが認識されない場合:**

- PowerShellを再起動してください

**Pythonインタープリターが見つからない場合:**

- VSCodeでフォルダを開き直してください
- `.venv\Scripts\python.exe` が存在するか確認してください

**グラフが表示されない場合:**

- `plt.show()` が実行されているか確認
- バックエンドエラーの場合は `plt.savefig('test.png')` で画像保存を試してください

## 次のステップ

環境構築が完了したら `Exercise.md` の練習問題に挑戦してみましょう！
