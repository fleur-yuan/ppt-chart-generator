from __future__ import annotations
from typing import Annotated, Dict, List, Literal, Union
from pydantic import BaseModel, Field


# ── 请求模型 ──────────────────────────────────────────────────

class BarRequest(BaseModel):
    chart_type: Literal["bar"]
    style: str = "mckinsey"
    palette: str = "business_blue"
    title: str = ""
    subtitle: str = ""
    categories: List[str]
    series: Dict[str, List[float]]
    stacked: bool = False
    horizontal: bool = False


class LineRequest(BaseModel):
    chart_type: Literal["line"]
    style: str = "mckinsey"
    palette: str = "business_blue"
    title: str = ""
    subtitle: str = ""
    categories: List[str]
    series: Dict[str, List[float]]
    area: bool = False


class PieRequest(BaseModel):
    chart_type: Literal["pie"]
    style: str = "mckinsey"
    palette: str = "business_blue"
    title: str = ""
    subtitle: str = ""
    labels: List[str]
    values: List[float]
    donut: bool = False


class RadarRequest(BaseModel):
    chart_type: Literal["radar"]
    style: str = "mckinsey"
    palette: str = "business_blue"
    title: str = ""
    subtitle: str = ""
    dimensions: List[str]
    series: Dict[str, List[float]]
    value_range: List[float] = [0, 100]


class ScatterRequest(BaseModel):
    chart_type: Literal["scatter"]
    style: str = "mckinsey"
    palette: str = "business_blue"
    title: str = ""
    subtitle: str = ""
    series: Dict[str, Dict[str, List[float]]]
    x_label: str = ""
    y_label: str = ""


ChartRequest = Annotated[
    Union[BarRequest, LineRequest, PieRequest, RadarRequest, ScatterRequest],
    Field(discriminator="chart_type"),
]


# ── 响应模型 ──────────────────────────────────────────────────

class GenerateResponse(BaseModel):
    image: str        # base64 编码的 PNG
    chart_type: str


class StyleMeta(BaseModel):
    key: str
    name: str
    background: str
    is_dark: bool
    emphasis_color: str


class PaletteMeta(BaseModel):
    key: str
    name: str
    colors: List[str]
    highlight: str


class ChartTypeMeta(BaseModel):
    key: str
    label: str
    options: List[str]


class OptionsResponse(BaseModel):
    styles: List[StyleMeta]
    palettes: List[PaletteMeta]
    chart_types: List[ChartTypeMeta]
