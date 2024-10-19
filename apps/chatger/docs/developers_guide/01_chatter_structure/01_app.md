# `App/`

```shell
App/
├── __init__.py
└── App.py
```

### `App.py`
主要用來啟動 `FastAPI` 的 `app`，並且設定 `app` 的 `Router`，另外設定 `app` 的 static files 路徑、`build_and_mount_playground` 的方法。

```py
app = FastAPI(
    title="Chatter Judge",
    description="Judge with ChatGPT",
    version="Chatter-v0.0.1-beta",
    docs_url="/docs",
)
```

```py
templates = Jinja2Templates(
    directory="templates",
)
```

```py
os.makedirs("static", exist_ok=True)
app.mount(
    "/static", 
    StaticFiles(directory="static"), 
    name="static",
)
```

```py
@app.get('/favicon.ico', include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse(
        './static/favicon.ico',
    )
```
