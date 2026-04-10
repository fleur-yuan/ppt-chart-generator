"""
万能 PPT 图表生成器
用法示例：
  python main.py --chart bar --style mckinsey --palette business_blue
  python main.py --chart line --style apple --palette warm_orange --area
  python main.py --chart pie --style notion --palette forest_green --donut
  python main.py --chart radar --style tech_dark --palette neon_tech
  python main.py --chart scatter --style academic --palette purple_fade
  python main.py --demo   # 一次性生成所有风格×颜色方案的演示图
"""
import argparse
import os
import sys

# 让子模块可以被直接导入
sys.path.insert(0, os.path.dirname(__file__))

from styles.presets import get_style, STYLES
from palettes.presets import get_palette, PALETTES
from charts import CHART_TYPES

# ── 演示数据 ──────────────────────────────────────────────────
DEMO_DATA = {
    "bar": {
        "categories": ["Q1", "Q2", "Q3", "Q4"],
        "series": {
            "产品A": [42, 58, 71, 89],
            "产品B": [35, 47, 63, 74],
        },
        "title": "季度销售对比",
        "subtitle": "单位：百万元  |  数据来源：销售部",
    },
    "line": {
        "categories": ["1月", "2月", "3月", "4月", "5月", "6月"],
        "series": {
            "收入": [120, 135, 148, 162, 178, 195],
            "成本": [80, 85, 90, 92, 95, 98],
        },
        "title": "收入与成本趋势",
        "subtitle": "单位：万元",
    },
    "pie": {
        "labels": ["华东", "华南", "华北", "华西", "其他"],
        "values": [35, 25, 20, 12, 8],
        "title": "区域销售占比",
        "subtitle": "2025 全年",
    },
    "radar": {
        "dimensions": ["创新能力", "市场份额", "客户满意度", "成本控制", "团队效率", "品牌影响力"],
        "series": {
            "本公司": [80, 65, 88, 72, 78, 70],
            "竞争对手": [70, 80, 75, 68, 65, 85],
        },
        "title": "竞争力雷达分析",
        "subtitle": "评分满分 100",
    },
    "scatter": {
        "series": {
            "高端市场": {"x": [8.2, 9.1, 7.8, 9.5, 8.7], "y": [85, 92, 78, 95, 88], "size": [120, 200, 90, 250, 160]},
            "大众市场": {"x": [5.1, 6.3, 4.8, 7.0, 5.9], "y": [55, 68, 48, 72, 61], "size": [80, 150, 60, 180, 100]},
        },
        "title": "价格与满意度关系",
        "subtitle": "气泡大小表示销量",
        "x_label": "价格指数",
        "y_label": "满意度评分",
    },
}


def generate_chart(chart_type, style_name, palette_name, output_dir, **kwargs):
    style = get_style(style_name)
    palette = get_palette(palette_name)
    ChartClass = CHART_TYPES[chart_type]
    chart = ChartClass(style=style, palette=palette)

    fname = f"{chart_type}_{style_name}_{palette_name}.png"
    output_path = os.path.join(output_dir, fname)

    data = DEMO_DATA[chart_type]

    if chart_type == "bar":
        path = chart.render(
            categories=data["categories"],
            series=data["series"],
            title=data["title"],
            subtitle=data["subtitle"],
            stacked=kwargs.get("stacked", False),
            horizontal=kwargs.get("horizontal", False),
            output_path=output_path,
        )
    elif chart_type == "line":
        path = chart.render(
            categories=data["categories"],
            series=data["series"],
            title=data["title"],
            subtitle=data["subtitle"],
            area=kwargs.get("area", False),
            output_path=output_path,
        )
    elif chart_type == "pie":
        path = chart.render(
            labels=data["labels"],
            values=data["values"],
            title=data["title"],
            subtitle=data["subtitle"],
            donut=kwargs.get("donut", False),
            output_path=output_path,
        )
    elif chart_type == "radar":
        path = chart.render(
            dimensions=data["dimensions"],
            series=data["series"],
            title=data["title"],
            subtitle=data["subtitle"],
            output_path=output_path,
        )
    elif chart_type == "scatter":
        path = chart.render(
            series=data["series"],
            title=data["title"],
            subtitle=data["subtitle"],
            x_label=data["x_label"],
            y_label=data["y_label"],
            output_path=output_path,
        )

    print(f"  ✓  {path}")
    return path


def run_demo(output_dir):
    """生成所有图表类型 × 所有风格 的演示图（使用默认颜色方案）"""
    style_palette_pairs = [
        ("mckinsey",   "business_blue"),
        ("apple",      "warm_orange"),
        ("tech_dark",  "neon_tech"),
        ("notion",     "forest_green"),
        ("academic",   "mono"),
        ("government", "china_red"),
    ]
    print(f"\n生成演示图集到 {output_dir}/\n")
    for chart_type in CHART_TYPES:
        print(f"[{chart_type}]")
        for style_name, palette_name in style_palette_pairs:
            generate_chart(chart_type, style_name, palette_name, output_dir)
    print(f"\n完成！共生成 {len(CHART_TYPES) * len(style_palette_pairs)} 张图表。")


def main():
    parser = argparse.ArgumentParser(
        description="万能 PPT 图表生成器",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--chart", "-c",
        choices=list(CHART_TYPES.keys()),
        default="bar",
        help=f"图表类型：{', '.join(CHART_TYPES.keys())}",
    )
    parser.add_argument(
        "--style", "-s",
        choices=list(STYLES.keys()),
        default="mckinsey",
        help=f"视觉风格：{', '.join(STYLES.keys())}",
    )
    parser.add_argument(
        "--palette", "-p",
        choices=list(PALETTES.keys()),
        default="business_blue",
        help=f"颜色方案：{', '.join(PALETTES.keys())}",
    )
    parser.add_argument(
        "--output", "-o",
        default="output",
        help="输出目录（默认：output/）",
    )
    parser.add_argument("--stacked",    action="store_true", help="柱状图：堆叠模式")
    parser.add_argument("--horizontal", action="store_true", help="柱状图：横向模式")
    parser.add_argument("--area",       action="store_true", help="折线图：面积填充")
    parser.add_argument("--donut",      action="store_true", help="饼图：环形模式")
    parser.add_argument("--demo",       action="store_true", help="生成全量演示图集")
    parser.add_argument(
        "--list", action="store_true",
        help="列出所有可用风格和颜色方案",
    )

    args = parser.parse_args()

    if args.list:
        print("\n可用风格：")
        for k, v in __import__("styles.presets", fromlist=["STYLES"]).STYLES.items():
            print(f"  {k:<15} {v.name}")
        print("\n可用颜色方案：")
        for k, v in __import__("palettes.presets", fromlist=["PALETTES"]).PALETTES.items():
            print(f"  {k:<15} {v.name}  {' '.join(v.colors[:4])}")
        return

    os.makedirs(args.output, exist_ok=True)

    if args.demo:
        run_demo(args.output)
        return

    print(f"\n图表：{args.chart}  风格：{args.style}  颜色：{args.palette}\n")
    generate_chart(
        args.chart, args.style, args.palette, args.output,
        stacked=args.stacked,
        horizontal=args.horizontal,
        area=args.area,
        donut=args.donut,
    )


if __name__ == "__main__":
    main()
