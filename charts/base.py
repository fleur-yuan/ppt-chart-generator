"""
通用图表基类 — 负责应用风格、保存文件等公共逻辑
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch

from styles.base import StyleConfig
from palettes.presets import Palette

# 启动时注册内置中文字体
_BUILTIN_FONT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "styles", "NotoSansCJKsc-Regular.otf")
if os.path.exists(_BUILTIN_FONT):
    fm.fontManager.addfont(_BUILTIN_FONT)
    _cjk_font_name = fm.FontProperties(fname=_BUILTIN_FONT).get_name()
    matplotlib.rcParams["font.family"] = _cjk_font_name
    matplotlib.rcParams["axes.unicode_minus"] = False


class BaseChart:
    def __init__(self, style: StyleConfig, palette: Palette):
        self.style = style
        self.palette = palette

    # ── 创建画布 ──────────────────────────────────────────────
    def _create_figure(self):
        s = self.style
        fig, ax = plt.subplots(
            figsize=(s.fig_width, s.fig_height),
            facecolor=s.figure_background,
        )
        ax.set_facecolor(s.background)
        fig.subplots_adjust(
            left=s.pad_left,
            right=s.pad_right,
            top=s.pad_top,
            bottom=s.pad_bottom,
        )
        return fig, ax

    # ── 应用风格到坐标轴 ──────────────────────────────────────
    def _apply_style(self, ax, title: str = "", subtitle: str = ""):
        s = self.style

        # 轴线（spine）— 极坐标轴没有 top/right/left/bottom，跳过
        if not getattr(ax, "name", "") == "polar":
            for spine_name, visible in [
                ("top", s.spine_top),
                ("right", s.spine_right),
                ("left", s.spine_left),
                ("bottom", s.spine_bottom),
            ]:
                if spine_name in ax.spines:
                    ax.spines[spine_name].set_visible(visible)
                    if visible:
                        ax.spines[spine_name].set_color(s.spine_color)
                        ax.spines[spine_name].set_linewidth(s.spine_width)

        # 网格
        if s.grid:
            axis = s.grid_axis
            if axis in ("y", "both"):
                ax.yaxis.grid(
                    True,
                    color=s.grid_color,
                    linestyle=s.grid_linestyle,
                    linewidth=s.grid_width,
                    alpha=s.grid_alpha,
                )
            if axis in ("x", "both"):
                ax.xaxis.grid(
                    True,
                    color=s.grid_color,
                    linestyle=s.grid_linestyle,
                    linewidth=s.grid_width,
                    alpha=s.grid_alpha,
                )
            ax.set_axisbelow(True)

        # 刻度
        ax.tick_params(
            axis="both",
            length=s.tick_length,
            width=s.tick_width,
            colors=s.tick_color,
            labelsize=s.tick_size,
        )

        # 字体（全局）
        plt.rcParams["font.family"] = s.font_family
        plt.rcParams["axes.unicode_minus"] = False

        # 让已有的 tick labels 也使用正确字体
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontfamily(s.font_family)

        # 标题
        if title:
            fig = ax.get_figure()
            y_title = s.pad_top + 0.02
            fig.text(
                s.pad_left,
                y_title,
                title,
                fontsize=s.title_size,
                fontweight=s.title_weight,
                color=s.title_color,
                va="bottom",
                ha="left",
                fontfamily=s.font_family,
            )
            if subtitle:
                fig.text(
                    s.pad_left,
                    y_title - 0.045,
                    subtitle,
                    fontsize=s.subtitle_size,
                    color=s.label_color,
                    va="bottom",
                    ha="left",
                    fontfamily=s.font_family,
                )

        # 顶部强调线
        if s.emphasis_line:
            fig = ax.get_figure()
            fig.add_artist(
                mpatches.FancyArrowPatch(
                    (s.pad_left, s.pad_top + 0.075),
                    (s.pad_right, s.pad_top + 0.075),
                    arrowstyle="-",
                    color=s.emphasis_line_color,
                    linewidth=s.emphasis_line_width,
                    transform=fig.transFigure,
                    clip_on=False,
                )
            )

    # ── 图例 ──────────────────────────────────────────────────
    def _add_legend(self, ax, labels, colors):
        if not self.style.legend or not labels:
            return
        s = self.style
        handles = [
            mpatches.Patch(color=c, label=l)
            for c, l in zip(colors, labels)
        ]
        ax.legend(
            handles=handles,
            loc=s.legend_position,
            frameon=s.legend_frame,
            fontsize=s.legend_fontsize,
            labelcolor=s.label_color,
        )

    # ── 保存文件 ──────────────────────────────────────────────
    def save(self, fig, path: str, fmt: str = "png"):
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        fig.savefig(
            path,
            format=fmt,
            dpi=self.style.dpi,
            bbox_inches="tight",
            facecolor=fig.get_facecolor(),
        )
        plt.close(fig)
        return path
