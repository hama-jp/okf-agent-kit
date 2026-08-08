# プロンプト例① — 新しいノートを書かせるとき

Claude Code などにノート作成を頼むとき、依頼文の末尾にこれを付けます
(または CLAUDE.md に常設 → `claude_md_snippet.md` 参照)。

```text
knowledge/ に調査ノートを書くときは、先頭に OKF v0.2 語彙の
YAML frontmatter を付けてください。

- type: ノートの種類 (例: research/note)
- generated: { by: あなたのモデル名, at: 今日の日付 }
- verified: 実際に一次ソースと突き合わせた場合のみ { by, at } を追記。
  確認した範囲を by の括弧内に書く (例: "claude/sonnet-5 (数値のみ突合)")
- status: draft から始める
- stale_after: 内容が古びる日付。決められない場合は null にして
  理由をコメントで書く

確認していない検証イベントを書いてはいけません。
verified が無いままなのは正常な状態です (unverified として扱われるだけ)。
```

## このプロンプトの意図

- **最後の2行が本体**です。エージェントは頼めば何でも書けてしまうので、
  「痕跡の無い検証を書かない」を明文で禁じ、「無くても正常」と伝えて
  埋めたがる圧力を抜いておきます。
- `status: draft` 始まりにするのは、v0.2 では無指定 = stable 扱いだからです。
  書きかけが stable に見える事故を防ぎます。
