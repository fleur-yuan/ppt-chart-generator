"""
散点图
"""
from typing import List, Optional
import numpy as np
import matplotlib.pyplot as plt

from .base import BaseChart
from styles.base import StyleConfig
from palettes.presets import Palette


class ScatterChart(BaseChart):
    def render(
        self,
        series: dict,   # {"系列名": {"x": [...], "y": [...], "size": [...] (可选)}, ...}
        title: str = "",
        subtitle: str = "",
        x_label: str = "",
        y_label: str = "",
        output_path: str = "output/scatter.png",
        fmt: str = "png",
    ) -> str:
        s = self.style
        p = self.palette
        fig, ax = self._create_figure()

        series_names = list(series.keys())
        n_series = len(series_names)
        colors = p.colors[:n_series] if n_series > 1 else [p.highlight]

        for i, (name, data) in enumerate(series.items()):
            x = np.array(data["x"], dtype=float)
            y = np.array(data["y"], dtype=float)
            sizes = data.get("size", None)
            if sizes is not None:
                # 归一化 size 到 20-200
                sz = np.array(sizes, dtype=float)
                sz = 20 + 180 * (sz - sz.min()) / (sz.max() - sz.min() + 1e-9)
            else:
                sz = 60

            color = colors[i % len(colors)]
            ax.scatter(
                x, y,
                s=sz,
                c=color,
                alpha=0.8,
                edgecolors=s.background,
                linewidths=0.8,
                label=name,
                zorder=3,
            )

        if x_label:
            ax.set_xlabel(
                x_label,
                fontsize=s.label_size,
                color=s.label_color,
                fontfamily=s.font_family,
            )
        if y_label:
            ax.set_ylabel(
                y_label,
                fontsize=s.label_size,
                color=s.label_color,
                fontfamily=s.font_family,
            )

        ax.tick_params(colors=s.tick_color)

        self._apply_style(ax, title=title, subtitle=subtitle)

        if n_series > 1:
            self._add_legend(ax, series_names, colors)

        return self.save(fig, output_path, fmt)
