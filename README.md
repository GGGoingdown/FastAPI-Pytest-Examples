# fastapi-pytest-example

## 專案說明
這是一個使用 FastAPI 框架和 Pytest 測試框架的範例專案。專案展示了如何建立一個簡單的 API 服務，並使用 Pytest 進行單元測試和異步測試。

## 專案架構
```bash 
fastapi-pytest-example/
├── src/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── main.py
│   └── utils.py
└── tests/
    ├── __init__.py
    ├── __pycache__/
    ├── conftest.py
    ├── test_main.py
    └── test_utils.py
```

## 主要文件說明
- `src/main.py`：定義了 FastAPI 應用的路由和處理函數。
- `src/utils.py`：包含一些輔助函數，例如長時間運行的任務和生成問候語的函數。
- `tests/conftest.py`：配置 Pytest 的一些全局設置和 fixture。
- `tests/test_main.py`：測試 `src/main.py` 中定義的 API 路由。
- `tests/test_utils.py`：測試 `src/utils.py` 中的輔助函數。

## 安裝與運行
1. 安裝依賴：
    ```sh
    pdm install
    ```

2. 運行 FastAPI 應用：
    ```sh
    pdm run uvicorn src.main:app --reload
    ```

3. 運行測試：
    ```sh
    pdm run pytest
    ```

## API 路由
- `GET /health`：返回服務狀態。
- `GET /greeting`：返回問候語。
- `GET /sync`：運行同步長時間任務。
- `GET /sync-in-thread`：在線程中運行同步長時間任務。
- `GET /async`：運行異步長時間任務。
- `GET /sequential`：順序運行多個異步長時間任務。
- `GET /concurrent`：並發運行多個異步長時間任務。

## 測試
- ：測試 API 路由的響應和行為。
- ：測試輔助函數的行為和輸出。

## 作者
- GGGoingdown (eddiepai0401@gmail.com)