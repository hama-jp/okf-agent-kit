# OKF v0.2 frontmatter テンプレート (新規ノート用)

そのままコピーして、コメントに従って埋めてください。
v0.2 で必須なのは `type` だけ。残りは書けるものだけ書き、書けないものは消してください。

```yaml
---
# 何の種類の知識か (唯一の必須キー)。語彙は自分のリポジトリで統一する
type: research/note

# 今の内容を「誰が・いつ」作ったか。at は最後の意味ある変更日 (ISO 8601)
generated: { by: claude/sonnet-5, at: "2026-08-08" }

# 内容を出典と突き合わせて確認したイベントのリスト。
# 確認していないなら、この欄ごと書かない (unverified のままが正直)。
# どこまで確認したか (scope) は by の括弧内に書くと後から分かる
verified:
  - { by: "human:sato (数値を一次ソースと突合)", at: "2026-08-08" }

# draft | stable | deprecated。無指定 = stable 扱いなので、書きかけは必ず draft に
status: draft

# この日を過ぎたら要再確認、という絶対日付 (YYYY-MM-DD)。
# 「90日」のような相対日数は書けない仕様。決められなければ null + 理由コメント
stale_after: "2026-09-08"

# 派生元。resource は辿れる URL / リポジトリ内相対パス
sources:
  - id: primary-spec
    resource: https://example.com/spec
    title: 元にした一次ソースの名前
---
```

## actor 記法 (書き手・確認者の表記)

| 主体 | 書き方 | 例 |
|---|---|---|
| 人間 | `human:<id>` | `human:sato` |
| エージェント/ツール | `<producer>/<version>` | `claude/sonnet-5`, `reference_agent/gemini-2.5-pro` |
| 自動プロセス | `process:<id>` | `process:nightly-audit` |

⚠️ 表記は最初に決めて、この表をリポジトリに置いてください。
同じ人が `human:sato` と `human:sato-t` で混ざると、あとからの集計が効かなくなります。
