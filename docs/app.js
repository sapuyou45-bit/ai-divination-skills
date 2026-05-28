const translations = {
  en: {
    "nav.skills": "Skills",
    "nav.quickStart": "Quick start",
    "nav.safety": "Safety",
    "nav.github": "GitHub",
    "hero.eyebrow": "Open-source skills for AI agents",
    "hero.title": "Direct divination tools, grounded agent workflows.",
    "hero.copy":
      "Tarot, I Ching, and Xiao Liu Ren skills that separate the draw from the interpretation. Scripts produce JSON. Agents interpret with clear boundaries.",
    "hero.github": "View on GitHub",
    "hero.quickStart": "Try the scripts",
    "intro.label": "Why it exists",
    "intro.title": "The model should not invent the oracle result.",
    "intro.copy":
      "This project treats divination systems as symbolic reasoning and reflection tools, not deterministic prediction engines. A local script creates the card draw, hexagram, or position; the AI agent interprets that concrete result.",
    "skills.label": "Included skills",
    "skills.title": "Three practical modules to start.",
    "skills.tarot.title": "Tarot",
    "skills.tarot.copy": "Draw cards for reflection, decisions, creative blocks, and project reframing.",
    "skills.iching.title": "I Ching",
    "skills.iching.copy": "Cast six-line hexagrams with primary and resulting hexagram output.",
    "skills.xiaoliuren.title": "Xiao Liu Ren",
    "skills.xiaoliuren.copy": "Cast from lunar-style numbers or a lightweight Gregorian time fallback.",
    "quick.label": "Quick start",
    "quick.title": "Run any script directly.",
    "quick.copy": "The MVP has no runtime dependencies beyond Python 3. Every script emits JSON.",
    "install.label": "Install",
    "install.title": "Copy only the skills you need.",
    "install.copy": "Each skill is self-contained with a SKILL.md file, OpenAI agent metadata, scripts, and references.",
    "safety.label": "Safety",
    "safety.title": "Symbolic reflection, not certainty.",
    "safety.item1": "Do not use readings as medical, legal, financial, or crisis guidance.",
    "safety.item2": "Tie every interpretation to the generated result.",
    "safety.item3": "Preserve user agency and offer small, reversible next steps.",
    "footer.ethics": "Ethics"
  },
  zh: {
    "nav.skills": "技能",
    "nav.quickStart": "快速开始",
    "nav.safety": "安全边界",
    "nav.github": "GitHub",
    "hero.eyebrow": "给 AI agent 使用的开源技能",
    "hero.title": "直接、可验证的占卜工具，服务于稳健的 agent 工作流。",
    "hero.copy":
      "塔罗、易经、小六壬技能将抽取/起卦与解释分开：脚本输出 JSON，AI agent 在清晰边界内解读结果。",
    "hero.github": "查看 GitHub",
    "hero.quickStart": "试用脚本",
    "intro.label": "为什么做这个",
    "intro.title": "模型不应该自己编出占卜结果。",
    "intro.copy":
      "本项目将占卜体系视为象征推理与反思工具，而不是确定性预言机器。本地脚本生成牌面、卦象或位置，AI agent 基于这个具体结果进行解释。",
    "skills.label": "已包含技能",
    "skills.title": "先从三个实用模块开始。",
    "skills.tarot.title": "塔罗",
    "skills.tarot.copy": "用于反思、决策、创作卡点和项目复盘的抽牌工具。",
    "skills.iching.title": "易经",
    "skills.iching.copy": "生成六爻卦象，输出本卦、变爻与之卦。",
    "skills.xiaoliuren.title": "小六壬",
    "skills.xiaoliuren.copy": "支持用农历式数字起课，也支持轻量公历时间 fallback。",
    "quick.label": "快速开始",
    "quick.title": "直接运行任意脚本。",
    "quick.copy": "MVP 除 Python 3 外没有运行依赖。所有脚本都会输出 JSON。",
    "install.label": "安装",
    "install.title": "只复制你需要的技能。",
    "install.copy": "每个 skill 都是自包含目录，包含 SKILL.md、OpenAI agent 元数据、脚本和参考资料。",
    "safety.label": "安全边界",
    "safety.title": "象征性反思，不是确定性预言。",
    "safety.item1": "不要把解读用作医疗、法律、金融或危机处置建议。",
    "safety.item2": "每个主要解释都要回到脚本生成的具体结果。",
    "safety.item3": "保留用户自主性，并给出小而可逆的下一步。",
    "footer.ethics": "伦理说明"
  },
  ja: {
    "nav.skills": "スキル",
    "nav.quickStart": "クイックスタート",
    "nav.safety": "安全性",
    "nav.github": "GitHub",
    "hero.eyebrow": "AI agent のためのオープンソース skill",
    "hero.title": "扱いやすい占術ツールを、堅実な agent ワークフローへ。",
    "hero.copy":
      "タロット、易経、小六壬の skill は、抽選や起卦と解釈を分離します。スクリプトが JSON を出力し、agent が境界を明確にして解釈します。",
    "hero.github": "GitHub で見る",
    "hero.quickStart": "スクリプトを試す",
    "intro.label": "目的",
    "intro.title": "モデルが占い結果を作り出すべきではありません。",
    "intro.copy":
      "このプロジェクトは占術体系を、決定論的な予言ではなく、象徴的推論と内省のための道具として扱います。ローカルスクリプトがカード、卦、位置を生成し、AI agent がその具体的な結果を解釈します。",
    "skills.label": "含まれるスキル",
    "skills.title": "まずは実用的な 3 つのモジュールから。",
    "skills.tarot.title": "タロット",
    "skills.tarot.copy": "内省、意思決定、創作の停滞、プロジェクトの見直しに使えるカードドロー。",
    "skills.iching.title": "易経",
    "skills.iching.copy": "六本の爻から本卦と之卦を出力します。",
    "skills.xiaoliuren.title": "小六壬",
    "skills.xiaoliuren.copy": "旧暦風の数値入力、または軽量なグレゴリオ暦の時刻 fallback に対応します。",
    "quick.label": "クイックスタート",
    "quick.title": "任意のスクリプトを直接実行できます。",
    "quick.copy": "MVP は Python 3 以外の実行時依存を持ちません。すべてのスクリプトは JSON を出力します。",
    "install.label": "インストール",
    "install.title": "必要な skill だけをコピーします。",
    "install.copy": "各 skill は SKILL.md、OpenAI agent メタデータ、スクリプト、参照資料を含む自己完結型です。",
    "safety.label": "安全性",
    "safety.title": "象徴的な内省であり、確定的な予言ではありません。",
    "safety.item1": "医療、法律、金融、危機対応の助言として使わないでください。",
    "safety.item2": "すべての解釈を、生成された具体的な結果に結びつけてください。",
    "safety.item3": "ユーザーの主体性を保ち、小さく可逆的な次の一歩を提案してください。",
    "footer.ethics": "倫理"
  }
};

const langButtons = Array.from(document.querySelectorAll("[data-lang]"));
const translatable = Array.from(document.querySelectorAll("[data-i18n]"));
const supportedLanguages = Object.keys(translations);

function preferredLanguage() {
  const stored = localStorage.getItem("ads-language");
  if (supportedLanguages.includes(stored)) {
    return stored;
  }

  const browserLanguage = navigator.language.toLowerCase();
  if (browserLanguage.startsWith("zh")) {
    return "zh";
  }
  if (browserLanguage.startsWith("ja")) {
    return "ja";
  }
  return "en";
}

function setLanguage(lang) {
  const dictionary = translations[lang] || translations.en;
  document.documentElement.lang = lang === "zh" ? "zh-CN" : lang;
  localStorage.setItem("ads-language", lang);

  translatable.forEach((node) => {
    const key = node.dataset.i18n;
    if (dictionary[key]) {
      node.textContent = dictionary[key];
    }
  });

  langButtons.forEach((button) => {
    button.setAttribute("aria-pressed", String(button.dataset.lang === lang));
  });
}

langButtons.forEach((button) => {
  button.addEventListener("click", () => setLanguage(button.dataset.lang));
});

setLanguage(preferredLanguage());

const canvas = document.getElementById("system-map");
const ctx = canvas.getContext("2d");
let width = 0;
let height = 0;
let particles = [];

function resizeCanvas() {
  const ratio = window.devicePixelRatio || 1;
  width = canvas.offsetWidth;
  height = canvas.offsetHeight;
  canvas.width = Math.floor(width * ratio);
  canvas.height = Math.floor(height * ratio);
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
  particles = Array.from({ length: Math.max(36, Math.floor(width / 22)) }, (_, index) => ({
    x: (index * 97) % width,
    y: (index * 53) % height,
    r: 1.6 + (index % 5) * 0.45,
    speed: 0.16 + (index % 7) * 0.025
  }));
}

function drawHexagram(x, y, scale, t) {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(Math.sin(t / 1800) * 0.045);
  ctx.strokeStyle = "rgba(250, 249, 244, 0.5)";
  ctx.lineWidth = 2;
  for (let i = 0; i < 6; i += 1) {
    const yy = i * scale * 0.45;
    if (i % 2 === 0) {
      ctx.beginPath();
      ctx.moveTo(-scale, yy);
      ctx.lineTo(scale, yy);
      ctx.stroke();
    } else {
      ctx.beginPath();
      ctx.moveTo(-scale, yy);
      ctx.lineTo(-scale * 0.25, yy);
      ctx.moveTo(scale * 0.25, yy);
      ctx.lineTo(scale, yy);
      ctx.stroke();
    }
  }
  ctx.restore();
}

function drawCard(x, y, w, h, t) {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(Math.sin(t / 1500) * 0.035);
  ctx.strokeStyle = "rgba(198, 71, 45, 0.62)";
  ctx.lineWidth = 2;
  ctx.strokeRect(-w / 2, -h / 2, w, h);
  ctx.beginPath();
  ctx.arc(0, 0, Math.min(w, h) * 0.18, 0, Math.PI * 2);
  ctx.stroke();
  ctx.restore();
}

function animate(time) {
  ctx.clearRect(0, 0, width, height);
  ctx.fillStyle = "#101010";
  ctx.fillRect(0, 0, width, height);

  particles.forEach((particle, index) => {
    particle.y -= particle.speed;
    if (particle.y < -10) {
      particle.y = height + 10;
    }
    ctx.fillStyle = index % 3 === 0 ? "rgba(0, 122, 90, 0.55)" : "rgba(250, 249, 244, 0.35)";
    ctx.beginPath();
    ctx.arc(particle.x, particle.y, particle.r, 0, Math.PI * 2);
    ctx.fill();
  });

  ctx.strokeStyle = "rgba(49, 83, 165, 0.24)";
  ctx.lineWidth = 1;
  for (let x = -80; x < width + 80; x += 120) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x + height * 0.24, height);
    ctx.stroke();
  }

  drawCard(width * 0.72, height * 0.38, 118, 172, time);
  drawCard(width * 0.82, height * 0.62, 92, 136, time + 500);
  drawHexagram(width * 0.61, height * 0.64, 54, time);
  drawHexagram(width * 0.88, height * 0.28, 38, time + 800);

  requestAnimationFrame(animate);
}

resizeCanvas();
window.addEventListener("resize", resizeCanvas);
requestAnimationFrame(animate);
