import json
from html import escape
from pathlib import Path
from urllib.parse import urlsplit

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
TITLE = "报表与模型入口"

st.set_page_config(page_title=TITLE, layout="wide")


def render_tool(tool):
    name = escape(tool["name"])
    description = escape(tool["description"])
    url = tool.get("url")
    if url:
        target = urlsplit(url)
        if target.scheme != "https" or not target.hostname:
            raise ValueError(f"{name} 的链接需为完整的 HTTPS 地址")
        action = (
            f'<a class="portal-action" href="{escape(url, quote=True)}" '
            f'target="_blank" rel="noopener noreferrer" aria-label="打开{name}（新标签页）">'
            '打开工具 <span aria-hidden="true">↗</span></a>'
        )
    else:
        action = '<span class="portal-pending">链接待补</span>'

    return (
        '<li class="portal-tool">'
        f'<div class="portal-tool-copy"><h3>{name}</h3><p>{description}</p></div>'
        f'{action}</li>'
    )


def render_group(group):
    group_name = escape(group["name"])
    tools = "".join(render_tool(tool) for tool in group["tools"])
    return f'<section class="portal-group"><h2>{group_name}</h2><ul>{tools}</ul></section>'


catalog = json.loads((APP_DIR / "tools.json").read_text(encoding="utf-8"))
groups = "".join(render_group(group) for group in catalog)
style = (APP_DIR / "style.css").read_text(encoding="utf-8")

st.html(f"""
<style>{style}</style>
<main class="portal">
  <header class="portal-header">
    <p>经营管理</p>
    <h1>{TITLE}</h1>
    <p>按业务分类查找报表和分析工具。</p>
  </header>
  <div class="portal-groups">{groups}</div>
</main>
""")
