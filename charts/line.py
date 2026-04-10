"""
折线图 / 面积图
"""
from typing import List
import numpy as np
import matplotlib.pyplot as plt

from .base import BaseChart
from styles.base import StyleConfig
from palettes.presets import Palette


class LineChart(BaseChart):
    def render(
        self,
        categories: List[str],
        series: dict,           # {"系列名": [值, ...], ...}
        title: str = "",
        subtitle: str = "",
        area: bool = False,     # 是否填充面积
        output_path: str = "output/line.png",
        fmt: str = "png",
    ) -> str:
        s = self.style
        p = self.palette
        fig, ax = self._create_figure()

        series_names = list(series.keys())
        n_series = len(series_names)
        colors = p.colors[:n_series] if n_series > 1 else [p.highlight]

        x = np.arange(len(categories))

        for i, (name, vals) in enumerate(series.items()):
            vals = np.array(vals, dtype=float)
            color = colors[i % len(colors)]
            marker = s.line_marker if s.line_marker != "none" else None

            ax.plot(
                x, vals,
                color=color,
                linewidth=s.line_width,
                marker=marker,
                markersize=s.line_marker_size,
                markerfacecolor=color,
                markeredgecolor=s.background,
                markeredgewidth=1.5,
                label=name,
                zorder=3,
            )

            if area:
                ax.fill_between(
                    x, vals,
                    alpha=0.15,
                    color=color,
                    zorder=2,
                )

            if s.show_value_labels:
                for xi, v in zip(x, vals):
                    ax.annotate(
                        s.value_label_fmt.format(v),
                        xy=(xi, v),
                        xytext=(0, 7),
                        textcoords="offset points",
                        ha="center", va="bottom",
                        fontsize=s.annotation_size,
                        fontweight=s.value_label_weight,
                        color=s.value_label_color,
                        fontfamily=s.font_family,
                    )

        ax.set_xticks(x)
        ax.set_xticklabels(categories, fontsize=s.tick_size, color=s.tick_color)
        ax.tick_params(colors=s.tick_color)

        self._apply_style(ax, title=title, subtitle=subtitle)

        if n_series > 1:
            self._add_legend(ax, series_names, colors)

        return self.save(fig, output_path, fmt)
