# 报表与模型入口

此 Streamlit 门户集中展示现有工具。点击「打开工具」会在新标签页访问原应用。

## 本地运行

在 `streamlit-portal` 目录执行以下命令。

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## 维护工具链接

在 `tools.json` 中按分类添加工具或更新现有工具的 HTTPS 地址。暂时没有地址时，将 `url` 设为 `null`，门户会显示「链接待补」。本地保存后刷新门户。

## 部署到 Streamlit Community Cloud

将此目录的文件放入门户专用 GitHub 仓库的根目录。在 Streamlit Community Cloud 创建应用，选择该仓库、分支和入口文件 `app.py`。先设置适用的门户分享范围，再从同事账号验证可访问的工具。
