# AGENTS.md 版 (Codex などCLAUDE.md以外のエージェント用)

内容は CLAUDE.md 版(`claude_md_full_example.md`)と同一です。
エージェントが読む指示ファイル名に合わせて、そのまま貼ってください。
`generated.by` の例だけ、実際に使うモデルの表記に変えます (例: `gpt-5.6-sol`)。

```markdown
## ノートの規約 (OKF v0.2 語彙)

knowledge/ の新規ノートには、ファイルの先頭に**このテンプレート通りの**
YAML frontmatter を付ける (キーはトップレベル。metadata などで入れ子にしない):

---
type: research/note
generated: { by: <あなたのモデル表記 例 gpt-5.6-sol>, at: "YYYY-MM-DD" }
status: draft
stale_after: "YYYY-MM-DD"   # 内容が古びる日付。決められなければ null + 理由コメント
sources:
  - resource: <派生元への相対パスまたはURL>
---

- status は draft から始める (無指定 = stable 扱いのため)
- verified は書かない。検証イベントは、実際に出典と突き合わせた者が
  そのときに追記する (確認していない検証イベントを書いてはいけない)
- 書き手の表記: 人間= human:<id> / エージェント= <producer>/<version> / 自動= process:<id>
```

## なぜ「テンプレート逐語」なのか (実測)

散文で「type/generated/verified/status/stale_after を付けて」とだけ書いた規約では、
エージェント(実測: Claude Haiku 4.5)は自分の流儀と混ぜて出力しました
(`metadata:` の下に入れ子・`authors` という独自キーの発明)。
テンプレートを逐語で貼り「この通りに。入れ子にしない」と書いたところ、完全準拠になりました。
散文の規約は「解釈」されます。形を固定したいものは、形そのものを見せてください。
