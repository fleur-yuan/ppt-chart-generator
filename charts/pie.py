"""
饼图 / 环形图
"""
from typing import List
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

from .base import BaseChart
from styles.base import StyleConfig
from palettes.presets import Palette


class PieChart(BaseChart):
    def render(
        self,
        labels: List[str],
        values: List[float],
        title: str = "",
        subtitle: str = "",
        donut: bool = False,    # 覆盖 style.donut
        explode_max: bool = True,  # 最大那块自动弹出
        output_path: str = "output/pie.png",
        fmt: str = "png",
    ) -> str:
        s = self.style
        p = self.palette
        fig, ax = self._create_figure()

        n = len(values)
        colors = p.colors[:n]
        use_donut = donut or s.donut

        # 最大块弹出
        vals = np.array(values, dtype=float)
        explode = [0.0] * n
        if explode_max:
            explode[int(np.argmax(vals))] = 0.05

        wedge_props = dict(
            edgecolor=s.pie_wedge_edge,
            linewidth=s.pie_wedge_edge_width,
        )

        wedges, texts, autotexts = ax.pie(
            vals,
            labels=None,
            colors=colors,
            explode=explode,
            autopct="%1.1f%%",
            startangle=s.pie_startangle,
            wedgeprops=wedge_props,
            pctdistance=0.75 if use_donut else 0.6,
            textprops={"fontsize": s.annotation_size, "color": s.background},
        )

        # 百分比标签颜色
        for at in autotexts:
            at.set_fontsize(s.annotation_size)
            at.set_fontweight(s.value_label_weight)
            at.set_color("#FFFFFF")
            at.set_path_effects([
                pe.withStroke(linewidth=1.5, foreground="#00000040")
            ])

        # 环形
        if use_donut:
            centre_circle = plt.Circle(
                (0, 0),
                s.donut_ratio,
                fc=s.background,
                linewidth=0,
            )
            ax.add_patch(centre_circle)
            ax.set_aspect("equal")

        # 图例（替代标签，更整洁）
        ax.legend(
            wedges,
            labels,
            loc="center left",
            bbox_to_anchor=(0.85, 0, 0.5, 1),
            frameon=False,
            fontsize=s.legend_fontsize,
            labelcolor=s.label_color,
        )

        ax.axis("equal")
        # 关掉多余轴线
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])

        self._apply_style(ax, title=title, subtitle=subtitle)

        return self.save(fig, output_path, fmt)
