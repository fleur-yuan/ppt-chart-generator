from .bar import BarChart
from .line import LineChart
from .pie import PieChart
from .radar import RadarChart
from .scatter import ScatterChart

CHART_TYPES = {
    "bar":     BarChart,
    "line":    LineChart,
    "pie":     PieChart,
    "radar":   RadarChart,
    "scatter": ScatterChart,
}
