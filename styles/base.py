from dataclasses import dataclass, field
from typing import Optional


@dataclass
class StyleConfig:
    name: str

    # 背景
    background: str = "#FFFFFF"
    figure_background: str = "#FFFFFF"

    # 边框与阴影
    show_border: bool = False
    shadow: bool = False

    # 顶部强调线（麦肯锡特色）
    emphasis_line: bool = False
    emphasis_line_color: str = "#000000"
    emphasis_line_width: float = 2.5

    # 字体
    font_family: str = "DejaVu Sans"
    title_size: float = 14
    title_weight: str = "bold"
    subtitle_size: float = 10
    label_size: float = 10
    tick_size: float = 9
    annotation_size: float = 9
    title_color: str = "#000000"
    label_color: str = "#333333"
    tick_color: str = "#555555"

    # 轴线
    spine_top: bool = False
    spine_right: bool = False
    spine_left: bool = True
    spine_bottom: bool = True
    spine_color: str = "#CCCCCC"
    spine_width: float = 1.0

    # 网格
    grid: bool = False
    grid_axis: str = "y"          # "x", "y", "both"
    grid_color: str = "#E5E5E5"
    grid_linestyle: str = "--"
    grid_alpha: float = 0.7
    grid_width: float = 0.5

    # 刻度
    tick_length: float = 0
    tick_width: float = 0

    # 柱状图
    bar_width: float = 0.6
    bar_radius: float = 0         # 圆角半径（0=直角）
    bar_edge_color: str = "none"
    bar_edge_width: float = 0

    # 折线图
    line_width: float = 2.5
    line_marker: str = "o"
    line_marker_size: float = 6
    line_smooth: bool = False

    # 饼图
    pie_startangle: float = 90
    pie_wedge_edge: str = "white"
    pie_wedge_edge_width: float = 2
    donut: bool = False
    donut_ratio: float = 0.6

    # 数据标签
    show_value_labels: bool = True
    value_label_position: str = "outside_end"  # "inside", "outside_end", "center"
    value_label_weight: str = "normal"
    value_label_color: str = "#333333"
    value_label_fmt: str = "{:.0f}"

    # 图例
    legend: bool = True
    legend_position: str = "upper right"
    legend_frame: bool = False
    legend_fontsize: float = 9

    # 图表尺寸（PPT 16:9）
    fig_width: float = 12
    fig_height: float = 6.75
    dpi: int = 150

    # 内边距
    pad_left: float = 0.10
    pad_right: float = 0.95
    pad_top: float = 0.88
    pad_bottom: float = 0.15
