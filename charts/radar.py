"""
雷达图（蜘蛛图）
"""
from typing import List
import numpy as np
import matplotlib.pyplot as plt

from .base import BaseChart
from styles.base import StyleConfig
from palettes.presets import Palette


class RadarChart(BaseChart):
    def render(
        self,
        dimensions: List[str],
        series: dict,               # {"系列名": [值, ...], ...}
        title: str = "",
        subtitle: str = "",
        value_range: tuple = (0, 100),
        output_path: str = "output/radar.png",
        fmt: str = "png",
    ) -> str:
        s = self.style
        p = self.palette
        fig = plt.figure(
            figsize=(s.fig_width, s.fig_height),
            facecolor=s.figure_background,
        )
        ax = fig.add_subplot(111, polar=True)
        ax.set_facecolor(s.background)
        fig.subplots_adjust(
            left=s.pad_left, right=s.pad_right,
            top=s.pad_top, bottom=s.pad_bottom,
        )

        N = len(dimensions)
        angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
        angles += angles[:1]  # 闭合

        series_names = list(series.keys())
        n_series = len(series_names)
        colors = p.colors[:n_series] if n_series > 1 else [p.highlight]

        vmin, vmax = value_range

        for i, (name, vals) in enumerate(series.items()):
            vals = list(vals) + [vals[0]]  # 闭合
            color = colors[i % len(colors)]

            ax.plot(
                angles, vals,
                color=color,
                linewidth=s.line_width,
                linestyle="-",
                label=name,
            )
            ax.fill(angles, vals, alpha=0.15, color=color)

        # 轴标签
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(
            dimensions,
            fontsize=s.tick_size,
            color=s.tick_color,
            fontfamily=s.font_family,
        )

        ax.set_ylim(vmin, vmax)
        ax.set_yticks(np.linspace(vmin, vmax, 5))
        ax.set_yticklabels(
            [str(int(v)) for v in np.linspace(vmin, vmax, 5)],
            fontsize=s.tick_size - 1,
            color=s.tick_color,
        )

        # 网格颜色
        ax.grid(
            color=s.grid_color,
            linestyle=s.grid_linestyle,
            linewidth=s.grid_width,
            alpha=s.grid_alpha,
        )
        ax.spines["polar"].set_color(s.grid_color)

        self._apply_style(ax, title=title, subtitle=subtitle)

        if n_series > 1 or series_names[0]:
            self._add_legend(ax, series_names, colors)

        return self.save(fig, output_path, fmt)
