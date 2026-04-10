from .base import StyleConfig
from .font_utils import DEFAULT_SANS, DEFAULT_SERIF

# ── 麦肯锡商务风 ──────────────────────────────────────────────
MCKINSEY = StyleConfig(
    name="麦肯锡商务",
    background="#FFFFFF",
    figure_background="#FFFFFF",

    emphasis_line=True,
    emphasis_line_color="#000000",
    emphasis_line_width=3.0,

    font_family=DEFAULT_SANS,
    title_size=15,
    title_weight="bold",
    title_color="#000000",
    label_color="#222222",
    tick_color="#444444",
    tick_size=9,

    spine_top=False,
    spine_right=False,
    spine_left=False,
    spine_bottom=True,
    spine_color="#000000",
    spine_width=1.2,

    grid=True,
    grid_axis="y",
    grid_color="#E0E0E0",
    grid_linestyle="-",
    grid_alpha=0.8,
    grid_width=0.5,

    tick_length=0,
    bar_width=0.55,
    bar_radius=0,
    bar_edge_color="none",

    line_width=2.8,
    line_marker="none",

    show_value_labels=True,
    value_label_position="outside_end",
    value_label_weight="bold",
    value_label_color="#000000",

    legend=True,
    legend_frame=False,
    legend_position="upper right",

    pad_left=0.08,
    pad_right=0.96,
    pad_top=0.85,
    pad_bottom=0.14,
)

# ── 苹果极简风 ────────────────────────────────────────────────
APPLE = StyleConfig(
    name="苹果极简",
    background="#FFFFFF",
    figure_background="#FFFFFF",

    emphasis_line=False,

    font_family=DEFAULT_SANS,
    title_size=16,
    title_weight="light",
    title_color="#1D1D1F",
    label_color="#6E6E73",
    tick_color="#6E6E73",
    tick_size=9,

    spine_top=False,
    spine_right=False,
    spine_left=False,
    spine_bottom=False,

    grid=True,
    grid_axis="y",
    grid_color="#F0F0F0",
    grid_linestyle="-",
    grid_alpha=1.0,
    grid_width=1.0,

    tick_length=0,
    bar_width=0.5,
    bar_radius=4,
    bar_edge_color="none",

    line_width=2.5,
    line_marker="o",
    line_marker_size=5,

    show_value_labels=False,

    legend=True,
    legend_frame=False,
    legend_position="upper right",

    pad_left=0.08,
    pad_right=0.96,
    pad_top=0.88,
    pad_bottom=0.12,
)

# ── 科技深色风 ────────────────────────────────────────────────
TECH_DARK = StyleConfig(
    name="科技深色",
    background="#1A1F2E",
    figure_background="#1A1F2E",

    emphasis_line=False,

    font_family=DEFAULT_SANS,
    title_size=14,
    title_weight="bold",
    title_color="#E8EAF0",
    label_color="#A0A8C0",
    tick_color="#707890",
    tick_size=9,

    spine_top=False,
    spine_right=False,
    spine_left=False,
    spine_bottom=True,
    spine_color="#3A4060",
    spine_width=1.0,

    grid=True,
    grid_axis="y",
    grid_color="#2E3450",
    grid_linestyle="-",
    grid_alpha=1.0,
    grid_width=0.8,

    tick_length=0,
    bar_width=0.6,
    bar_radius=2,
    bar_edge_color="none",

    line_width=2.5,
    line_marker="o",
    line_marker_size=5,

    show_value_labels=True,
    value_label_position="outside_end",
    value_label_weight="normal",
    value_label_color="#C0C8E0",

    legend=True,
    legend_frame=False,
    legend_position="upper right",

    pad_left=0.08,
    pad_right=0.96,
    pad_top=0.88,
    pad_bottom=0.14,
)

# ── Notion 信息图风 ───────────────────────────────────────────
NOTION = StyleConfig(
    name="Notion信息图",
    background="#F7F6F3",
    figure_background="#F7F6F3",

    emphasis_line=False,

    font_family=DEFAULT_SANS,
    title_size=14,
    title_weight="bold",
    title_color="#37352F",
    label_color="#6B6860",
    tick_color="#9B9A97",
    tick_size=9,

    spine_top=False,
    spine_right=False,
    spine_left=False,
    spine_bottom=False,

    grid=True,
    grid_axis="y",
    grid_color="#E8E7E4",
    grid_linestyle="-",
    grid_alpha=1.0,
    grid_width=1.0,

    tick_length=0,
    bar_width=0.55,
    bar_radius=3,
    bar_edge_color="none",

    line_width=2.2,
    line_marker="o",
    line_marker_size=6,

    show_value_labels=True,
    value_label_position="outside_end",
    value_label_weight="normal",
    value_label_color="#37352F",

    legend=True,
    legend_frame=False,
    legend_position="upper right",

    pad_left=0.08,
    pad_right=0.96,
    pad_top=0.88,
    pad_bottom=0.12,
)

# ── 学术论文风 ────────────────────────────────────────────────
ACADEMIC = StyleConfig(
    name="学术论文",
    background="#FFFFFF",
    figure_background="#FFFFFF",

    emphasis_line=False,

    font_family=DEFAULT_SERIF,
    title_size=13,
    title_weight="normal",
    title_color="#000000",
    label_color="#000000",
    tick_color="#000000",
    tick_size=9,

    spine_top=True,
    spine_right=True,
    spine_left=True,
    spine_bottom=True,
    spine_color="#000000",
    spine_width=0.8,

    grid=True,
    grid_axis="both",
    grid_color="#CCCCCC",
    grid_linestyle="--",
    grid_alpha=0.5,
    grid_width=0.5,

    tick_length=4,
    tick_width=0.8,
    bar_width=0.6,
    bar_radius=0,
    bar_edge_color="#333333",
    bar_edge_width=0.5,

    line_width=1.5,
    line_marker="s",
    line_marker_size=5,

    show_value_labels=False,

    legend=True,
    legend_frame=True,
    legend_position="upper right",

    pad_left=0.10,
    pad_right=0.95,
    pad_top=0.90,
    pad_bottom=0.14,
)

# ── 政务/国企风 ───────────────────────────────────────────────
GOVERNMENT = StyleConfig(
    name="政务国企",
    background="#FFFFFF",
    figure_background="#FFFFFF",

    emphasis_line=True,
    emphasis_line_color="#CC0000",
    emphasis_line_width=3.0,

    font_family=DEFAULT_SANS,
    title_size=15,
    title_weight="bold",
    title_color="#1A1A1A",
    label_color="#333333",
    tick_color="#555555",
    tick_size=9,

    spine_top=False,
    spine_right=False,
    spine_left=True,
    spine_bottom=True,
    spine_color="#AAAAAA",
    spine_width=1.0,

    grid=True,
    grid_axis="y",
    grid_color="#E8E8E8",
    grid_linestyle="--",
    grid_alpha=0.8,
    grid_width=0.6,

    tick_length=3,
    tick_width=0.8,
    bar_width=0.6,
    bar_radius=0,
    bar_edge_color="none",

    line_width=2.5,
    line_marker="o",
    line_marker_size=5,

    show_value_labels=True,
    value_label_position="outside_end",
    value_label_weight="normal",
    value_label_color="#333333",

    legend=True,
    legend_frame=False,
    legend_position="upper right",

    pad_left=0.10,
    pad_right=0.95,
    pad_top=0.86,
    pad_bottom=0.14,
)

# ── 注册表 ────────────────────────────────────────────────────
STYLES = {
    "mckinsey":   MCKINSEY,
    "apple":      APPLE,
    "tech_dark":  TECH_DARK,
    "notion":     NOTION,
    "academic":   ACADEMIC,
    "government": GOVERNMENT,
}


def get_style(name: str) -> StyleConfig:
    key = name.lower().replace("-", "_").replace(" ", "_")
    if key not in STYLES:
        available = ", ".join(STYLES.keys())
        raise ValueError(f"未知风格 '{name}'，可用风格：{available}")
    return STYLES[key]
