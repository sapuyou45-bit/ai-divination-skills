# AI Divination Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

AI agent のための、直接的で実用的な占術 skill 集です。

`ai-divination-skills` は、タロット、易経、小六壬、そして今後追加される象徴体系のためのオープンソース skill コレクションです。agent ワークフロー向けに設計されており、ローカルスクリプトがカード、卦、位置を生成し、AI agent が明確な安全境界の中で解釈します。

このプロジェクトは占術を、決定論的な予言ではなく、象徴的推論と内省の道具として扱います。

## 多言語ドキュメント

プロジェクトには、ページ内で言語切り替えできる GitHub Pages ドキュメントがあります。

- [English](https://sapuyou45-bit.github.io/ai-divination-skills/?lang=en)
- [简体中文](https://sapuyou45-bit.github.io/ai-divination-skills/?lang=zh)
- [日本語](https://sapuyou45-bit.github.io/ai-divination-skills/?lang=ja)

ローカルプレビュー：

```bash
python3 -m http.server 8000 -d docs
```

公開ページ：

```text
https://sapuyou45-bit.github.io/ai-divination-skills/?lang=ja
```

## 含まれる Skills

| Skill | 内容 | スクリプト |
|---|---|---|
| `tarot` | 内省、意思決定、創作の停滞、プロジェクトの見直しのためにカードを引きます。 | `skills/tarot/scripts/draw.py` |
| `iching` | 六本の爻から本卦と之卦を出力します。 | `skills/iching/scripts/cast.py` |
| `xiaoliuren` | 旧暦風の数値、または軽量なグレゴリオ暦 fallback から小六壬を起こします。 | `skills/xiaoliuren/scripts/cast.py` |

## なぜ作るのか

多くの AI 占いプロンプトでは、モデルが結果そのものを作ってしまいます。このプロジェクトは役割を分けます。

1. スクリプトがカード、卦、位置を生成する。
2. AI agent がその具体的な結果を解釈する。

これにより、読みはテスト、再現、監査、再利用がしやすくなります。

## クイックスタート

任意のスクリプトを直接実行できます。

```bash
python3 skills/tarot/scripts/draw.py --deck major --spread three-card --reversals
python3 skills/iching/scripts/cast.py --method coins
python3 skills/xiaoliuren/scripts/cast.py --method numbers --month 3 --day 12 --hour 7
```

再現可能な demo には seed を使います。

```bash
python3 skills/tarot/scripts/draw.py --spread decision --seed demo
python3 skills/iching/scripts/cast.py --method random --seed demo
```

すべてのスクリプトは JSON を出力します。

## Agent Skill としてインストール

必要な skill フォルダを agent の skill ディレクトリへコピーします。

```bash
cp -R skills/tarot ~/.codex/skills/tarot
cp -R skills/iching ~/.codex/skills/iching
cp -R skills/xiaoliuren ~/.codex/skills/xiaoliuren
```

各 skill は自己完結型です。

```text
skills/name/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
```

必要な skill だけを個別にコピーしてください。

## Agent の振る舞い

各 skill は agent に次のことを求めます。

- 具体的な抽選/起卦結果を生成または受け取る
- 必要なときだけ簡潔な参照資料を読む
- 共有レスポンス形式で解釈する
- 確定的表現、宿命論、専門的助言を避ける

共有ガイド：

- `shared/response-contract.md`
- `shared/randomness-protocol.md`
- `shared/safety-policy.md`
- `shared/interpretation-style.md`

## Examples

- `examples/tarot-decision.md`
- `examples/iching-strategy.md`
- `examples/xiaoliuren-daily.md`

## 安全境界

これらの skills は、医療、法律、金融、危機対応の助言には使いません。

よい読みは：

- 結果を象徴的な内省として扱う
- 主な解釈を生成された結果に結びつける
- ユーザーの主体性を保つ
- 小さく可逆的な次の一歩を提案する
- 不確実性を明確に示す

詳しくは `ETHICS.md` を参照してください。

## 開発

Python 3 以外の実行時依存はありません。

テスト：

```bash
python3 -m unittest discover -s tests
```

## ロードマップ

近いうちに：

- MVP skills の参照資料を拡充する。
- 例の読みを増やす。
- 簡単なインストーラーを追加する。
- 中国語と日本語ドキュメントをさらに整える。

将来：

- `meihua`
- `liuyao`
- `runes`
- `numerology`
- `astrology`

## License

MIT
