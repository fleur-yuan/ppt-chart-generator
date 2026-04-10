import base64
import os
import sys
import tempfile

# 引用上级目录的模块
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from charts import CHART_TYPES
from styles.presets import get_style
from palettes.presets import get_palette
from web.models import (
    BarRequest, LineRequest, PieRequest, RadarRequest, ScatterRequest,
)


def render_to_base64(req) -> str:
    style = get_style(req.style)
    palette = get_palette(req.palette)
    chart = CHART_TYPES[req.chart_type](style=style, palette=palette)

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        tmp_path = f.name

    try:
        _dispatch(chart, req, tmp_path)
        with open(tmp_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


def _dispatch(chart, req, path: str):
    t = req.chart_type

    if t == "bar":
        chart.render(
            categories=req.categories,
            series=req.series,
            title=req.title,
            subtitle=req.subtitle,
            stacked=req.stacked,
            horizontal=req.horizontal,
            output_path=path,
        )
    elif t == "line":
        chart.render(
            categories=req.categories,
            series=req.series,
            title=req.title,
            subtitle=req.subtitle,
            area=req.area,
            output_path=path,
        )
    elif t == "pie":
        chart.render(
            labels=req.labels,
            values=req.values,
            title=req.title,
            subtitle=req.subtitle,
            donut=req.donut,
            output_path=path,
        )
    elif t == "radar":
        chart.render(
            dimensions=req.dimensions,
            series=req.series,
            title=req.title,
            subtitle=req.subtitle,
            value_range=tuple(req.value_range),
            output_path=path,
        )
    elif t == "scatter":
        chart.render(
            series=req.series,
            title=req.title,
            subtitle=req.subtitle,
            x_label=req.x_label,
            y_label=req.y_label,
            output_path=path,
        )
