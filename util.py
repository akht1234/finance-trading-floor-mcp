from enum import Enum

# ======== COLORS =========
class Color(Enum):
    RED = "#ff4040"
    GREEN = "#48ff78"
    YELLOW = "#ffd85c"
    BLUE = "#5ca9ff"
    MAGENTA = "#da66ff"
    CYAN = "#41f8ff"
    WHITE = "#d5e8f6"
    DARK_CARD = "#101416"
    DARK_SURFACE = "#0b0f11"
    BORDER_NEON = "#00ffa8"


css = f"""
footer{{display:none !important}}
* {{
  scroll-behavior:smooth;
}}
*::-webkit-scrollbar {{
  width: 6px;
  height: 6px;
}}
*::-webkit-scrollbar-thumb {{
  background: #00ffa855;
  border-radius: 6px;
}}

body, .gradio-container {{
    background: radial-gradient(circle at 30% 20%, #0e1316, #050708 80%) !important;
    color: #cfd6dd !important;
    font-family: Inter, -apple-system, BlinkMacSystemFont, sans-serif !important;
    animation: fadeIn 0.7s ease-out forwards;
    opacity:0;
}}
@keyframes fadeIn {{
  0% {{ opacity:0; transform:translateY(6px) }}
  100% {{ opacity:1; transform:translateY(0) }}
}}

.gr-box {{
    backdrop-filter: blur(14px);
    background: linear-gradient(180deg, rgba(16,20,22,0.55) 0%, rgba(10,14,16,0.7) 100%) !important;
    border: 1px solid rgba(0,255,168,0.08) !important;
    border-radius: 14px !important;
    padding: 8px !important;
    transition: all .25s ease-in-out;
}}
.gr-box:hover {{
    border: 1px solid {Color.BORDER_NEON.value} !important;
    box-shadow:0 0 12px {Color.BORDER_NEON.value}55;
}}

@keyframes pulse {{
  0% {{ box-shadow: 0 0 0px {Color.BORDER_NEON.value}; }}
  50%{{ box-shadow: 0 0 14px {Color.BORDER_NEON.value}; }}
  100%{{ box-shadow: 0 0 0px {Color.BORDER_NEON.value}; }}
}}
.neon {{
    border-color: {Color.BORDER_NEON.value} !important;
    animation: pulse 3s infinite !important;
}}

.positive-pnl {{
    color: {Color.GREEN.value} !important;
    font-weight: 700;
}}
.negative-pnl {{
    color: {Color.RED.value} !important;
    font-weight: 700;
}}

.dataframe-fix-small .table-wrap {{
  min-height: 160px;
  max-height: 160px;
}}
.dataframe-fix .table-wrap {{
  min-height: 220px;
  max-height: 220px;
}}
"""

# ========== JS ==============
js = """
let last = 0;
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
function throttleRAF(cb){
  const now = performance.now();
  if(now - last > 400){
    last = now; cb();
  }
}
"""

def make_sparkline_values(time_series: list):
    if not time_series: return []
    return [float(v) for _, v in time_series]
