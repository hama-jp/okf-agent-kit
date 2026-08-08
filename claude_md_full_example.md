# このリポジトリの規約

## ノートの規約 (OKF v0.2 語彙)

knowledge/ の新規ノートには、ファイルの先頭に**このテンプレート通りの**
YAML frontmatter を付ける (キーはトップレベル。metadata などで入れ子にしない):

```yaml
---
type: research/note
generated: { by: claude/haiku-4.5, at: "YYYY-MM-DD" }
status: draft
stale_after: "YYYY-MM-DD"   # 内容が古びる日付。決められなければ null + 理由コメント
sources:
  - resource: <派生元への相対パスまたはURL>
---
```

- status は draft から始める (無指定 = stable 扱いのため)
- verified は今回は**書かない**。検証イベントは、実際に出典と突き合わせた者が
  そのときに追記する (確認していない検証イベントを書いてはいけない)
- 書き手の表記: 人間= human:<id> / エージェント= <producer>/<version> / 自動= process:<id>
