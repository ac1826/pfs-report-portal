# 报表与模型入口

点击报表名称，在新标签页打开原应用。

## 本地运行

在 `streamlit-portal` 目录执行以下命令。

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## 维护工具链接

入口维护于 `tools.json`。每个工具包含名称 `name` 和 HTTPS 地址 `url`。暂时没有地址时，将 `url` 设为 `null`。本地保存后刷新门户。

## 部署到 Streamlit Community Cloud

将此目录的文件放入门户专用 GitHub 仓库的根目录。在 Streamlit Community Cloud 创建应用，选择该仓库、分支和入口文件 `app.py`。先设置适用的门户分享范围，再从同事账号验证可访问的工具。
