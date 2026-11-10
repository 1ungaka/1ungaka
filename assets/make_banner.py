"""Generate the profile banner in dark and light themes.

Run: python assets/make_banner.py
The terminal lines are real alerts from github.com/1ungaka/soc-log-triage run on its sample data.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent

THEMES = {
    "dark": dict(bg="#0d1117", panel="#161b22", bar="#1c2128", border="#30363d", text="#e6edf3",
                 muted="#8b949e", accent="#58a6ff", chip="#1f6feb26", chipText="#79c0ff",
                 crit="#ff7b72", high="#ffa657", ok="#3fb950", grid="#21262d"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", bar="#eaeef2", border="#d0d7de", text="#1f2328",
                  muted="#59636e", accent="#0969da", chip="#0969da14", chipText="#0550ae",
                  crit="#cf222e", high="#bc4c00", ok="#1a7f37", grid="#eaeef2"),
}

ALERTS = [
    ("CRITICAL", "AUTH-003 ", "root login after 24 failures", "T1110"),
    ("CRITICAL", "ACCT-003 ", "new account added to sudo", "T1098"),
    ("HIGH", "KERB-001 ", "kerberoasting, 4 RC4 tickets", "T1558.003"),
    ("HIGH", "EXEC-002 ", "winword.exe -> powershell", "T1204.002"),
    ("HIGH", "EVADE-001", "security log cleared", "T1685.005"),
]

CHIPS = ["Detection engineering", "Log analysis", "Incident triage", "MITRE ATT&CK"]


def banner(c: dict) -> str:
    W, H = 1200, 330
    mono = "ui-monospace,SFMono-Regular,Consolas,'Liberation Mono',Menlo,monospace"
    sans = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Lunga Ngaka, aspiring SOC analyst</title>
<desc id="d">Banner with a terminal showing ATT&amp;CK-mapped alerts from the soc-log-triage tool.</desc>
<style>
  .sans {{ font-family: {sans}; }}
  .mono {{ font-family: {mono}; }}
  .line {{ animation: show .45s ease-out backwards; }}
  .cursor {{ animation: blink 1.1s steps(1) infinite; }}
  @keyframes show {{ from {{ opacity: 0; transform: translateX(-6px); }} }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  @media (prefers-reduced-motion: reduce) {{ .line, .cursor {{ animation: none; }} }}
</style>
<defs>
  <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
    <path d="M24 0H0V24" fill="none" stroke="{c['grid']}" stroke-width="1"/>
  </pattern>
  <linearGradient id="fade" x1="0" x2="1">
    <stop offset="0" stop-color="{c['bg']}" stop-opacity="1"/>
    <stop offset=".55" stop-color="{c['bg']}" stop-opacity=".2"/>
    <stop offset="1" stop-color="{c['bg']}" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect width="{W}" height="{H}" rx="14" fill="{c['bg']}"/>
<rect width="{W}" height="{H}" rx="14" fill="url(#grid)"/>
<rect width="{W}" height="{H}" rx="14" fill="url(#fade)"/>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{c['border']}"/>

<g class="sans">
  <text x="56" y="86" font-size="14" font-weight="600" letter-spacing="2.5" fill="{c['accent']}">BLUE TEAM  ·  SECURITY OPERATIONS</text>
  <text x="54" y="146" font-size="54" font-weight="700" fill="{c['text']}">Lunga Ngaka</text>
  <text x="56" y="186" font-size="19" fill="{c['muted']}">Aspiring SOC Analyst. I build detections and triage</text>
  <text x="56" y="212" font-size="19" fill="{c['muted']}">tools, and test them against realistic attack data.</text>
</g>''']
    # chips
    x = 56
    for chip in CHIPS:
        w = 18 + len(chip) * 7.6
        parts.append(f'<g class="sans"><rect x="{x}" y="240" width="{w:.0f}" height="30" rx="15" fill="{c["chip"]}" stroke="{c["accent"]}" stroke-opacity=".35"/>'
                     f'<text x="{x + w/2:.0f}" y="260" font-size="13" font-weight="600" text-anchor="middle" fill="{c["chipText"]}">{escape(chip)}</text></g>')
        x += w + 10

    # terminal
    tx, ty, tw, th = 640, 40, 516, 250
    parts.append(f'''<g>
  <rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="10" fill="{c['panel']}" stroke="{c['border']}"/>
  <path d="M{tx} {ty+10}a10 10 0 0 1 10-10h{tw-20}a10 10 0 0 1 10 10v22H{tx}z" fill="{c['bar']}"/>
  <circle cx="{tx+20}" cy="{ty+16}" r="5.5" fill="#ff5f57"/><circle cx="{tx+38}" cy="{ty+16}" r="5.5" fill="#febc2e"/><circle cx="{tx+56}" cy="{ty+16}" r="5.5" fill="#28c840"/>
  <text x="{tx + tw/2}" y="{ty+21}" class="mono" font-size="12" text-anchor="middle" fill="{c['muted']}">soc-log-triage</text>
</g>''')
    y = ty + 62
    parts.append(f'<text x="{tx+18}" y="{y}" class="mono line" font-size="13.5" xml:space="preserve" style="animation-delay:.2s">'
                 f'<tspan fill="{c["ok"]}">$</tspan><tspan fill="{c["text"]}"> soc-triage scan logs/* --min-severity high</tspan></text>')
    for i, (sev, rid, what, tid) in enumerate(ALERTS):
        y += 26
        col = c["crit"] if sev == "CRITICAL" else c["high"]
        label = f"[{sev}]".ljust(11)
        parts.append(
            f'<text x="{tx+18}" y="{y}" class="mono line" font-size="13.5" xml:space="preserve" style="animation-delay:{.7 + i*.45:.2f}s">'
            f'<tspan fill="{col}" font-weight="700">{label}</tspan>'
            f'<tspan fill="{c["text"]}">{escape(rid)} </tspan>'
            f'<tspan fill="{c["muted"]}">{escape(what.ljust(29))}</tspan>'
            f'<tspan fill="{c["accent"]}">{tid}</tspan></text>')
    y += 30
    parts.append(f'<text x="{tx+18}" y="{y}" class="mono line" font-size="13.5" style="animation-delay:{.7 + len(ALERTS)*.45:.2f}s">'
                 f'<tspan fill="{c["ok"]}">$</tspan></text>'
                 f'<rect class="cursor" x="{tx+32}" y="{y-12}" width="8" height="15" fill="{c["text"]}"/>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    for name, colours in THEMES.items():
        (OUT / f"banner-{name}.svg").write_text(banner(colours), encoding="utf-8")
    print("wrote", ", ".join(f"banner-{n}.svg" for n in THEMES))
