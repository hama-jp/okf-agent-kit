# OKF v0.2 をコーディングエージェントで使う — プロンプト&テンプレート集

動画「OKF活用入門 v0.2対応版」の付属ファイルです。
Claude Code などのコーディングエージェントで、OKF (Open Knowledge Format) v0.2 の
信頼語彙をエージェント運用のノート・台帳に取り入れるための最小セットです。

- 仕様の正本: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md (v0.2, 2026-07-24)
- 公式ブログ: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
- サンプルバンドル (架空企業 acme_retail): https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf/bundles/acme_retail

## 同梱ファイル

| ファイル | 用途 |
|---|---|
| `claude_md_full_example.md` | **動画の実録デモで実際に使った CLAUDE.md 全文**(テンプレート逐語方式) |
| `agents_md_example.md` | 同内容の AGENTS.md 版(Codex 等) + 「なぜテンプレ逐語か」の実測メモ |
| `header_template.md` | 新規ノート用の OKF v0.2 frontmatter テンプレート(コメント付き) |
| `prompt_1_new_note.md` | プロンプト例① — エージェントに新規ノートを書かせるときの指示 |
| `prompt_2_audit.md` | プロンプト例② — 週1回の棚卸し監査(報告のみ・書き換えなし) |
| `claude_md_snippet.md` | CLAUDE.md / AGENTS.md への常設追記例(最小版) |
| `check_frontmatter.py` | frontmatter の決定論チェッカー(AI不使用・約60行) |

## 重要な実測メモ: 規約は「テンプレート逐語」で書く

散文で「OKF語彙の frontmatter を付けて」と書くだけでは、エージェントは
自分の流儀と混ぜて出力します(実測: `metadata:` 配下への入れ子・独自キーの発明)。
**テンプレートそのものを規約に逐語で貼り、「この通りに。入れ子にしない」と書く**と、
完全準拠になります。散文の規約は「解釈」される、と覚えてください。

## 注意

- v0.2 の新しい欄は**すべて任意**です。必須は今も `type` ただ1つ。
- 欄を書いたから信頼できるようになる、という魔法ではありません。
  「確認していない検証イベントを書かない」という運用規律とセットで初めて意味を持ちます。
- 仕様はバージョン 0.2、参照実装は概念実証段階です。ここにあるのは仕様への準拠を
  目指すツールではなく、v0.2 の語彙を日々のエージェント運用に借りる最小プロファイルです。
