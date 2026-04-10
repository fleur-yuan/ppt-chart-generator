from dataclasses import dataclass
from typing import List


@dataclass
class Palette:
    name: str
    colors: List[str]          # 数据系列颜色，按顺序使用
    highlight: str             # 强调色（单系列图表主色）
    neutral: str               # 次要色 / 背景色块
    text_on_dark: str = "#FFFFFF"
    text_on_light: str = "#333333"


# ── 商务蓝 ────────────────────────────────────────────────────
BUSINESS_BLUE = Palette(
    name="商务蓝",
    colors=["#1F4E79", "#2E75B6", "#5BA4D4", "#9DC3E6", "#BDD7EE", "#DEEAF1"],
    highlight="#2E75B6",
    neutral="#BDD7EE",
)

# ── 暖橙系 ────────────────────────────────────────────────────
WARM_ORANGE = Palette(
    name="暖橙系",
    colors=["#C55A11", "#E07030", "#F4A460", "#F8C89A", "#FAE0C8", "#FDF2E9"],
    highlight="#E07030",
    neutral="#F8C89A",
)

# ── 森林绿 ────────────────────────────────────────────────────
FOREST_GREEN = Palette(
    name="森林绿",
    colors=["#1E5631", "#2D8047", "#4CAF6F", "#85C99A", "#B8DFC5", "#E4F2E9"],
    highlight="#2D8047",
    neutral="#85C99A",
)

# ── 霓虹科技 ──────────────────────────────────────────────────
NEON_TECH = Palette(
    name="霓虹科技",
    colors=["#00D4FF", "#7B2FFF", "#FF6B35", "#00FF88", "#FFE135", "#FF4FA0"],
    highlight="#00D4FF",
    neutral="#7B2FFF",
)

# ── 极简黑白灰 ────────────────────────────────────────────────
MONO = Palette(
    name="极简黑白",
    colors=["#1A1A1A", "#555555", "#888888", "#AAAAAA", "#CCCCCC", "#E8E8E8"],
    highlight="#1A1A1A",
    neutral="#AAAAAA",
)

# ── 中国红 ────────────────────────────────────────────────────
CHINA_RED = Palette(
    name="中国红",
    colors=["#CC0000", "#003F88", "#E63B2E", "#2A5CAA", "#F4A7A3", "#A8C4E0"],
    highlight="#CC0000",
    neutral="#2A5CAA",
)

# ── 紫色渐变 ──────────────────────────────────────────────────
PURPLE_FADE = Palette(
    name="紫色渐变",
    colors=["#4A0E8F", "#7B2FBE", "#A855F7", "#C084FC", "#DDB6FD", "#F3E8FF"],
    highlight="#7B2FBE",
    neutral="#C084FC",
)

# ── 珊瑚粉 ────────────────────────────────────────────────────
CORAL = Palette(
    name="珊瑚粉",
    colors=["#C0392B", "#E74C6B", "#FF6B8A", "#FF9AAF", "#FFC5D0", "#FFEAED"],
    highlight="#E74C6B",
    neutral="#FF9AAF",
)

# ── 注册表 ────────────────────────────────────────────────────
PALETTES = {
    "business_blue": BUSINESS_BLUE,
    "warm_orange":   WARM_ORANGE,
    "forest_green":  FOREST_GREEN,
    "neon_tech":     NEON_TECH,
    "mono":          MONO,
    "china_red":     CHINA_RED,
    "purple_fade":   PURPLE_FADE,
    "coral":         CORAL,
}


def get_palette(name: str) -> Palette:
    key = name.lower().replace("-", "_").replace(" ", "_")
    if key not in PALETTES:
        available = ", ".join(PALETTES.keys())
        raise ValueError(f"未知颜色方案 '{name}'，可用方案：{available}")
    return PALETTES[key]
