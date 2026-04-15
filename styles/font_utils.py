"""
自动检测系统中可用的中文字体，按优先级返回最佳选择
"""
import matplotlib.font_manager as fm

_PREFERRED_FONTS = [
    # Linux (Railway/server)
    "Noto Sans CJK SC", "Noto Sans CJK TC", "Source Han Sans SC",
    "WenQuanYi Micro Hei",
    # macOS
    "PingFang SC", "PingFang HK", "PingFang TC",
    "STHeiti", "Heiti TC", "Heiti SC",
    # Windows
    "Microsoft YaHei", "SimHei", "SimSun",
    # 通用衬线（学术用）
    "Songti SC", "STSong", "SimSun",
    # 最终兜底
    "Arial Unicode MS",
]

_PREFERRED_SERIF = [
    "Songti SC", "STSong", "SimSun",
    "AR PL UMing CN", "Noto Serif CJK SC",
]

_cache: dict = {}


def _available_fonts() -> set:
    if "all" not in _cache:
        _cache["all"] = {f.name for f in fm.fontManager.ttflist}
    return _cache["all"]


def best_cjk_font(serif: bool = False) -> str:
    preferred = _PREFERRED_SERIF if serif else _PREFERRED_FONTS
    available = _available_fonts()
    for font in preferred:
        if font in available:
            return font
    return "DejaVu Sans"  # 兜底（不显示中文但不报错）


# 在各风格中使用的默认字体
DEFAULT_SANS  = best_cjk_font(serif=False)
DEFAULT_SERIF = best_cjk_font(serif=True)
