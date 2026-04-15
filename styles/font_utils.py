"""
自动检测系统中可用的中文字体，按优先级返回最佳选择
优先使用项目内置字体，确保服务器环境也能正常显示中文
"""
import os
import matplotlib.font_manager as fm

# 项目内置字体路径
_BUILTIN_FONT = os.path.join(os.path.dirname(__file__), "NotoSansCJKsc-Regular.otf")

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
    "Songti SC", "STSong",
    # 最终兜底
    "Arial Unicode MS",
]

_PREFERRED_SERIF = [
    "Songti SC", "STSong", "SimSun",
    "AR PL UMing CN", "Noto Serif CJK SC",
]

_cache: dict = {}


def _register_builtin_font():
    """注册项目内置字体"""
    if os.path.exists(_BUILTIN_FONT) and "builtin" not in _cache:
        fm.fontManager.addfont(_BUILTIN_FONT)
        _cache["builtin"] = True


def _available_fonts() -> set:
    if "all" not in _cache:
        _register_builtin_font()
        _cache["all"] = {f.name for f in fm.fontManager.ttflist}
    return _cache["all"]


def best_cjk_font(serif: bool = False) -> str:
    _register_builtin_font()
    preferred = _PREFERRED_SERIF if serif else _PREFERRED_FONTS
    available = _available_fonts()
    for font in preferred:
        if font in available:
            return font
    # 如果内置字体存在，直接用文件路径
    if os.path.exists(_BUILTIN_FONT):
        prop = fm.FontProperties(fname=_BUILTIN_FONT)
        return prop.get_name()
    return "DejaVu Sans"  # 兜底（不显示中文但不报错）


# 在各风格中使用的默认字体
DEFAULT_SANS  = best_cjk_font(serif=False)
DEFAULT_SERIF = best_cjk_font(serif=True)
