const translations = {
  en: {
    "meta.title": "AI Divination Skills",
    "meta.description": "Direct, practical divination skills for AI agents: tarot, I Ching, Xiao Liu Ren, and more.",
    "nav.skills": "Skills",
    "nav.rigor": "Method",
    "nav.quickStart": "Quick start",
    "nav.safety": "Safety",
    "nav.github": "GitHub",
    "hero.eyebrow": "Open-source skills for AI agents",
    "hero.title": "Direct divination tools, grounded agent workflows.",
    "hero.copy":
      "Tarot, I Ching, and Xiao Liu Ren skills that separate the divination process from interpretation. Scripts perform the draw or cast and emit JSON. AI only interprets.",
    "hero.github": "View on GitHub",
    "hero.quickStart": "Try the scripts",
    "intro.label": "Why it exists",
    "intro.title": "The model should not invent the oracle result.",
    "intro.copy":
      "This project treats divination systems as symbolic reasoning and reflection tools, not deterministic prediction engines. A local script creates the card draw, hexagram, or position; the AI agent interprets that concrete result.",
    "rigor.label": "Methodological rigor",
    "rigor.title": "Randomness and interpretation stay separate.",
    "rigor.copy":
      "For real readings, the divination result comes from system randomness, a traditional probability model, or explicit user-provided physical input. Seeded mode is reserved for tests and reproducible demos.",
    "rigor.item1": "Tarot uses an explicit Fisher-Yates shuffle.",
    "rigor.item2": "I Ching supports three-coin casts and digital yarrow-equivalent probabilities.",
    "rigor.item3": "Xiao Liu Ren prefers lunar numbers, with optional lunar-time conversion.",
    "rigor.item4": "Approximate modes are labeled with warnings.",
    "skills.label": "Included skills",
    "skills.title": "Three practical modules to start.",
    "skills.tarot.title": "Tarot",
    "skills.tarot.copy": "Draw cards for reflection, decisions, creative blocks, and project reframing.",
    "skills.iching.title": "I Ching",
    "skills.iching.copy": "Cast six-line hexagrams with primary and resulting hexagram output.",
    "skills.xiaoliuren.title": "Xiao Liu Ren",
    "skills.xiaoliuren.copy": "Cast from lunar-style numbers or a lightweight Gregorian time fallback.",
    "quick.label": "Quick start",
    "quick.title": "Install once, call one CLI.",
    "quick.copy": "Use pip install . from a checkout, then call tarot, I Ching, Xiao Liu Ren, or agent templates through ai-divination.",
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
    "meta.title": "AI 占卜 Skills",
    "meta.description": "给 AI agent 使用的直接、实用占卜技能集：塔罗、易经、小六壬，以及更多象征系统。",
    "nav.skills": "技能",
    "nav.rigor": "方法",
    "nav.quickStart": "快速开始",
    "nav.safety": "安全边界",
    "nav.github": "GitHub",
    "hero.eyebrow": "给 AI agent 使用的开源技能",
    "hero.title": "直接、可验证的占卜工具，服务于稳健的 agent 工作流。",
    "hero.copy":
      "塔罗、易经、小六壬技能将占卜过程与解释分开：脚本负责抽取或起课并输出 JSON，AI 只负责解读。",
    "hero.github": "查看 GitHub",
    "hero.quickStart": "试用脚本",
    "intro.label": "为什么做这个",
    "intro.title": "模型不应该自己编出占卜结果。",
    "intro.copy":
      "本项目将占卜体系视为象征推理与反思工具，而不是确定性预言机器。本地脚本生成牌面、卦象或位置，AI agent 基于这个具体结果进行解释。",
    "rigor.label": "方法论严谨性",
    "rigor.title": "随机过程和 AI 解读清楚分开。",
    "rigor.copy":
      "真实 reading 的占卜结果来自系统随机、传统概率模型，或用户自己提供的实体占卜输入。seed 只用于测试和可复现 demo。",
    "rigor.item1": "塔罗使用显式 Fisher-Yates 洗牌。",
    "rigor.item2": "易经支持三枚硬币法和数字蓍草等价概率。",
    "rigor.item3": "小六壬优先使用农历数字，也支持可选 lunar-time 转换。",
    "rigor.item4": "近似模式必须带 warning，不伪装成传统准确起法。",
    "skills.label": "已包含技能",
    "skills.title": "先从三个实用模块开始。",
    "skills.tarot.title": "塔罗",
    "skills.tarot.copy": "用于反思、决策、创作卡点和项目复盘的抽牌工具。",
    "skills.iching.title": "易经",
    "skills.iching.copy": "生成六爻卦象，输出本卦、变爻与之卦。",
    "skills.xiaoliuren.title": "小六壬",
    "skills.xiaoliuren.copy": "支持用农历式数字起课，也支持轻量公历时间 fallback。",
    "quick.label": "快速开始",
    "quick.title": "安装一次，用一个 CLI 调用。",
    "quick.copy": "在 checkout 中使用 pip install .，之后通过 ai-divination 调用塔罗、易经、小六壬或 agent 解读模板。",
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
    "meta.title": "AI Divination Skills",
    "meta.description": "AI agent のための、直接的で実用的な占術 skill 集です。タロット、易経、小六壬などに対応します。",
    "nav.skills": "スキル",
    "nav.rigor": "方法",
    "nav.quickStart": "クイックスタート",
    "nav.safety": "安全性",
    "nav.github": "GitHub",
    "hero.eyebrow": "AI agent のためのオープンソース skill",
    "hero.title": "扱いやすい占術ツールを、堅実な agent ワークフローへ。",
    "hero.copy":
      "タロット、易経、小六壬の skill は、占術プロセスと解釈を分離します。スクリプトが抽選や起卦を行って JSON を出力し、AI は解釈だけを担当します。",
    "hero.github": "GitHub で見る",
    "hero.quickStart": "スクリプトを試す",
    "intro.label": "目的",
    "intro.title": "モデルが占い結果を作り出すべきではありません。",
    "intro.copy":
      "このプロジェクトは占術体系を、決定論的な予言ではなく、象徴的推論と内省のための道具として扱います。ローカルスクリプトがカード、卦、位置を生成し、AI agent がその具体的な結果を解釈します。",
    "rigor.label": "方法論的厳密性",
    "rigor.title": "乱数処理と AI の解釈を分けます。",
    "rigor.copy":
      "実際の reading では、占術結果はシステム乱数、伝統的な確率モデル、またはユーザーが物理的に得た入力から生成します。seed はテストと再現可能な demo 専用です。",
    "rigor.item1": "タロットは明示的な Fisher-Yates シャッフルを使います。",
    "rigor.item2": "易経は三枚硬貨法とデジタル蓍草等価確率に対応します。",
    "rigor.item3": "小六壬は旧暦の数値入力を優先し、任意で lunar-time 変換を使えます。",
    "rigor.item4": "近似モードは warning を出し、伝統的精度を装いません。",
    "skills.label": "含まれるスキル",
    "skills.title": "まずは実用的な 3 つのモジュールから。",
    "skills.tarot.title": "タロット",
    "skills.tarot.copy": "内省、意思決定、創作の停滞、プロジェクトの見直しに使えるカードドロー。",
    "skills.iching.title": "易経",
    "skills.iching.copy": "六本の爻から本卦と之卦を出力します。",
    "skills.xiaoliuren.title": "小六壬",
    "skills.xiaoliuren.copy": "旧暦風の数値入力、または軽量なグレゴリオ暦の時刻 fallback に対応します。",
    "quick.label": "クイックスタート",
    "quick.title": "一度インストールして、1 つの CLI で呼び出します。",
    "quick.copy": "checkout で pip install . を実行すると、ai-divination からタロット、易経、小六壬、agent テンプレートを呼び出せます。",
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

const langLinks = Array.from(document.querySelectorAll("[data-lang]"));
const translatable = Array.from(document.querySelectorAll("[data-i18n]"));
const supportedLanguages = Object.keys(translations);

function preferredLanguage() {
  const params = new URLSearchParams(window.location.search);
  const queryLanguage = params.get("lang");
  if (supportedLanguages.includes(queryLanguage)) {
    return queryLanguage;
  }

  const stored = localStorage.getItem("ads-language");
  if (supportedLanguages.includes(stored)) {
    return stored;
  }

  return "zh";
}

function setLanguage(lang) {
  const dictionary = translations[lang] || translations.zh;
  document.documentElement.lang = lang === "zh" ? "zh-CN" : lang;
  document.title = dictionary["meta.title"];
  const description = document.querySelector('meta[name="description"]');
  if (description) {
    description.setAttribute("content", dictionary["meta.description"]);
  }
  localStorage.setItem("ads-language", lang);

  translatable.forEach((node) => {
    const key = node.dataset.i18n;
    if (dictionary[key]) {
      node.textContent = dictionary[key];
    }
  });

  langLinks.forEach((link) => {
    link.setAttribute("aria-pressed", String(link.dataset.lang === lang));
  });
}

langLinks.forEach((link) => {
  link.addEventListener("click", (event) => {
    event.preventDefault();
    const lang = link.dataset.lang;
    const url = new URL(window.location.href);
    url.searchParams.set("lang", lang);
    window.history.pushState({}, "", url);
    setLanguage(lang);
  });
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
