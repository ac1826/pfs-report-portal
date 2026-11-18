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
    url = tool.get("url")
    if not url:
        return f'<li class="report-row pending">{name}<span>链接待补</span></li>'

    target = urlsplit(url)
    if target.scheme != "https" or not target.hostname:
        raise ValueError(f"{tool['name']} 的链接需为完整的 HTTPS 地址")
    return (
        f'<li><a class="report-row" href="{escape(url, quote=True)}" '
        'target="_blank" rel="noopener noreferrer" aria-description="在新标签页打开">'
        f'{name}<span aria-hidden="true">↗</span></a></li>'
    )


def render_group(group):
    group_name = escape(group["name"])
    tools = "".join(render_tool(tool) for tool in group["tools"])
    return f'<section><h2>{group_name}</h2><ul class="reports">{tools}</ul></section>'


def render_rules(tool):
    rules = "".join(f"<li>{escape(rule)}</li>" for rule in tool["rules"])
    return (
        f'<details><summary>{escape(tool["name"])}</summary>'
        f"<ul>{rules}</ul></details>"
    )


catalog = json.loads((APP_DIR / "tools.json").read_text(encoding="utf-8"))
groups = "".join(render_group(group) for group in catalog)
rule_documents = "".join(render_rules(tool) for group in catalog for tool in group["tools"])
style = (APP_DIR / "style.css").read_text(encoding="utf-8")

st.html(f"""
<style>{style}</style>
<div class="portal">
  <h1>{TITLE}</h1>
  <nav aria-label="报表入口">{groups}</nav>
  <section class="rules" aria-labelledby="portal-rules-title">
    <h2 id="portal-rules-title">报表规则</h2>
    {rule_documents}
  </section>
</div>
""")
