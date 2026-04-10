import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from web.models import ChartRequest, GenerateResponse, OptionsResponse, StyleMeta, PaletteMeta, ChartTypeMeta
from web.renderer import render_to_base64
from styles.presets import STYLES
from palettes.presets import PALETTES

app = FastAPI(title="PPT Chart Generator")

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# 深色风格判断阈值
def _is_dark(hex_color: str) -> bool:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    return luminance < 128


@app.get("/")
def index():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


@app.post("/api/generate", response_model=GenerateResponse)
def generate(req: ChartRequest):
    try:
        image_b64 = render_to_base64(req)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"渲染失败：{e}")
    return GenerateResponse(image=image_b64, chart_type=req.chart_type)


@app.get("/api/options", response_model=OptionsResponse)
def options():
    styles = []
    for key, s in STYLES.items():
        styles.append(StyleMeta(
            key=key,
            name=s.name,
            background=s.background,
            is_dark=_is_dark(s.background),
            emphasis_color=s.emphasis_line_color if s.emphasis_line else s.spine_color,
        ))

    palettes = []
    for key, p in PALETTES.items():
        palettes.append(PaletteMeta(
            key=key,
            name=p.name,
            colors=p.colors,
            highlight=p.highlight,
        ))

    chart_types = [
        ChartTypeMeta(key="bar",     label="柱状图", options=["stacked", "horizontal"]),
        ChartTypeMeta(key="line",    label="折线图", options=["area"]),
        ChartTypeMeta(key="pie",     label="饼图",   options=["donut"]),
        ChartTypeMeta(key="radar",   label="雷达图", options=[]),
        ChartTypeMeta(key="scatter", label="散点图", options=[]),
    ]

    return OptionsResponse(styles=styles, palettes=palettes, chart_types=chart_types)
