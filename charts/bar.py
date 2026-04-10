"""
柱状图（分组柱 / 堆叠柱）
"""
from typing import List, Optional
import numpy as np
import matplotlib.pyplot as plt

from .base import BaseChart
from styles.base import StyleConfig
from palettes.presets import Palette


class BarChart(BaseChart):
    def render(
        self,
        categories: List[str],
        series: dict,           # {"系列名": [值, ...], ...}
        title: str = "",
        subtitle: str = "",
        stacked: bool = False,
        horizontal: bool = False,
        output_path: str = "output/bar.png",
        fmt: str = "png",
    ) -> str:
        s = self.style
        p = self.palette
        fig, ax = self._create_figure()

        series_names = list(series.keys())
        n_series = len(series_names)
        n_cats = len(categories)
        colors = p.colors[:n_series] if n_series > 1 else [p.highlight]

        x = np.arange(n_cats)
        bar_w = s.bar_width / max(n_series, 1)

        bars_list = []
        bottom_vals = np.zeros(n_cats)

        for i, (name, vals) in enumerate(series.items()):
            vals = np.array(vals, dtype=float)
            color = colors[i % len(colors)]

            if stacked:
                offset = x
                b = bottom_vals.copy()
            else:
                offset = x + (i - (n_series - 1) / 2) * bar_w
                b = None

            plot_fn = ax.barh if horizontal else ax.bar
            if horizontal:
                bars = ax.barh(
                    offset,
                    vals,
                    height=bar_w if not stacked else s.bar_width,
                    left=b if stacked else None,
                    color=color,
                    edgecolor=s.bar_edge_color,
                    linewidth=s.bar_edge_width,
                    label=name,
                )
            else:
                bars = ax.bar(
                    offset,
                    vals,
                    width=bar_w if not stacked else s.bar_width,
                    bottom=b if stacked else None,
                    color=color,
                    edgecolor=s.bar_edge_color,
                    linewidth=s.bar_edge_width,
                    label=name,
                )

            bars_list.append(bars)

            if stacked:
                bottom_vals += vals

            # 圆角（近似：在柱子上叠加圆角矩形遮罩，仅非堆叠时）
            # matplotlib 3.7+ 支持 bar(..., ...暂不依赖)

            # 数据标签
            if s.show_value_labels:
                for rect, v in zip(bars, vals):
                    if horizontal:
                        x_pos = rect.get_x() + rect.get_width()
                        y_pos = rect.get_y() + rect.get_height() / 2
                        ha, va = "left", "center"
                        offset_x, offset_y = 3, 0
                    else:
                        x_pos = rect.get_x() + rect.get_width() / 2
                        y_pos = rect.get_y() + rect.get_height()
                        ha, va = "center", "bottom"
                        offset_x, offset_y = 0, 3

                    ax.annotate(
                        s.value_label_fmt.format(v),
                        xy=(x_pos, y_pos),
                        xytext=(offset_x, offset_y),
                        textcoords="offset points",
                        ha=ha, va=va,
                        fontsize=s.annotation_size,
                        fontweight=s.value_label_weight,
                        color=s.value_label_color,
                        fontfamily=s.font_family,
                    )

        # 坐标轴标签
        if horizontal:
            ax.set_yticks(x)
            ax.set_yticklabels(categories, fontsize=s.tick_size, color=s.tick_color)
            ax.set_xlabel("")
        else:
            ax.set_xticks(x)
            ax.set_xticklabels(categories, fontsize=s.tick_size, color=s.tick_color)
            ax.set_ylabel("")

        ax.tick_params(colors=s.tick_color)

        self._apply_style(ax, title=title, subtitle=subtitle)

        if n_series > 1:
            self._add_legend(ax, series_names, colors)

        return self.save(fig, output_path, fmt)
