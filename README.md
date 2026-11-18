# 报表与模型入口

此 Streamlit 门户集中展示现有工具。点击「打开工具」会在新标签页访问原应用。

## 本地运行

在 `streamlit-portal` 目录执行以下命令。

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## 补充成本工具链接

打开 `tools.json`，找到相应工具，将其 `"url": null` 改为带引号的完整 HTTPS 地址。保存后刷新门户。已有的工具地址也在同一文件维护。

## 部署到 Streamlit Community Cloud

将此目录的文件放入门户专用 GitHub 仓库的根目录。在 Streamlit Community Cloud 创建应用，选择该仓库、分支和入口文件 `app.py`。先设置适用的门户分享范围，再从同事账号验证可访问的工具。
