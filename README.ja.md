# AI Divination Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

✨ AI agent のためのオープンソース占術 skill 集です。乱数、カードドロー、起卦はツールが行い、AI は具体的な結果だけを解釈します。

`ai-divination-skills` は、タロット、易経、小六壬、そして今後追加される象徴体系のための実用的な skill コレクションです。agent ワークフロー向けに、監査可能なランダム性、明確な方法境界、再利用できる解釈テンプレートを重視しています。

このプロジェクトは占術を、決定論的な予言ではなく、象徴的推論と内省の道具として扱います。

## ✨ 概要

多くの AI 占いプロンプトでは、モデルが結果そのものを作ってしまいます。このリポジトリは役割を分けます。

1. ローカルスクリプトがカード、卦、小六壬の位置を生成する。
2. AI agent がその具体的な結果を、安全境界の中で解釈する。

これにより、読みはテスト、再現、監査、再利用がしやすくなります。

## 🧭 方法論的厳密性

基本ルールは明確です。スクリプト、またはユーザーが物理的に得た結果がカード、卦、位置を生成します。AI はその生成済みの結果を解釈するだけで、占術結果そのものは生成しません。

これは占術の科学的有効性を証明するものではありません。象徴的推論をより監査しやすくするための workflow です。

- 実際の reading はデフォルトでシステム乱数を使う
- seed はテストと再現可能な demo のみ
- 各 skill が伝統的方法と制限を記録する
- JSON 出力に監査可能な方法メタデータを含める
- 近似モードは warning を出し、伝統的精度を装わない

## 🌐 多言語ドキュメント

GitHub Pages のルートページは、デフォルトで簡体中文を表示します。ページ内で 3 言語に切り替えできます。

- [Default / 简体中文](https://sapuyou45-bit.github.io/ai-divination-skills/)
- [English](https://sapuyou45-bit.github.io/ai-divination-skills/?lang=en)
- [简体中文](https://sapuyou45-bit.github.io/ai-divination-skills/?lang=zh)
- [日本語](https://sapuyou45-bit.github.io/ai-divination-skills/?lang=ja)

ローカルプレビュー：

```bash
python3 -m http.server 8000 -d docs
```

公開ページ：

```text
https://sapuyou45-bit.github.io/ai-divination-skills/
```

## 🧩 含まれる Skills

| Skill | 内容 | スクリプト |
|---|---|---|
| `tarot` | 内省、意思決定、創作の停滞、プロジェクトの見直しのためにカードを引きます。 | `skills/tarot/scripts/draw.py` |
| `iching` | 六本の爻から本卦と之卦を出力します。 | `skills/iching/scripts/cast.py` |
| `xiaoliuren` | 旧暦風の数値、または軽量なグレゴリオ暦 fallback から小六壬を起こします。 | `skills/xiaoliuren/scripts/cast.py` |

## 🚀 クイックスタート

ローカル checkout から統一 CLI をインストールします。

```bash
pip install .
```

開発中は editable mode も使えます。

```bash
pip install -e .
```

3 つの体系を同じ入口で呼び出せます。

```bash
ai-divination tarot --deck major --spread three-card --reversals
ai-divination iching --method yarrow
ai-divination xiaoliuren --method numbers --month 3 --day 12 --hour 7
```

agent 用の解釈テンプレートも表示できます。

```bash
ai-divination template tarot
```

Python API から直接使うこともできます。

```python
from ai_divination_skills.tarot import draw
from ai_divination_skills.iching import cast
from ai_divination_skills.xiaoliuren import cast_numbers
```

従来どおり、下層のスクリプトを直接実行することもできます。

```bash
python3 skills/tarot/scripts/draw.py --deck major --spread three-card --reversals
python3 skills/iching/scripts/cast.py --method coins
python3 skills/iching/scripts/cast.py --method yarrow
python3 skills/xiaoliuren/scripts/cast.py --method numbers --month 3 --day 12 --hour 7
```

再現可能な demo には seed を使います。

```bash
python3 skills/tarot/scripts/draw.py --spread decision --seed demo
python3 skills/iching/scripts/cast.py --method yarrow --seed demo
```

すべてのスクリプトは JSON を出力します。

## 📦 Agent Skill としてインストール

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

各 skill スクリプトは単独フォルダでも動作します。Python package がインストール済みなら package runtime に委譲し、skill フォルダだけをコピーした場合は、その skill に同梱された standalone スクリプトへ fallback します。

## 🤖 Agent の振る舞い

各 skill は agent に次のことを求めます。

- 具体的な抽選/起卦結果を生成または受け取る
- 必要なときだけ簡潔な参照資料を読む
- 共有レスポンス形式で解釈する
- 確定的表現、宿命論、専門的助言を避ける

共有ガイド：

- `shared/methodology.md`
- `shared/interpretation-protocol.md`
- `shared/response-contract.md`
- `shared/randomness-protocol.md`
- `shared/safety-policy.md`
- `shared/interpretation-style.md`

## 🧪 Examples

- `examples/tarot-decision.md`
- `examples/iching-strategy.md`
- `examples/xiaoliuren-daily.md`

## 🛡️ 安全境界

これらの skills は、医療、法律、金融、危機対応の助言には使いません。

よい読みは：

- 結果を象徴的な内省として扱う
- 主な解釈を生成された結果に結びつける
- ユーザーの主体性を保つ
- 小さく可逆的な次の一歩を提案する
- 不確実性を明確に示す

詳しくは `ETHICS.md` を参照してください。

## 🛠️ 開発

Python 3 以外の実行時依存はありません。

テスト：

```bash
python3 -m unittest discover -s tests
```

## 🗺️ ロードマップ

近いうちに：

- Python package 公開用 workflow を追加する。
- CI の自動 skill validation をさらに拡充する。
- MVP skills の参照資料を拡充する。
- 例の読みを増やす。
- agent 連携例を増やす。

将来：

- `meihua`
- `liuyao`
- `runes`
- `numerology`
- `astrology`

## 📄 License

MIT
