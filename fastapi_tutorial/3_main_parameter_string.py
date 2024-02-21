from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: str | None = Query(
#         default=None, min_length=3, max_length=50, pattern="^fixedquery$"
#     ),
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# 1. read_items(q: Annotated[str | None, Query(max_length=50)] = None):
# 2. read_items(q: str | None = Query(default=None, max_length=50)):
# 上記2つは等価だが、Annotatedを使用した1が推奨されている
@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 明示的に必須パラメータであることを表すには`...`をデフォルト値にセットする
@app.get("/items/")
async def read_items2(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 必須パラメータかつNoneを許可する（= 何かしらの値をパラメータとして受け取る必要がある）場合はtypeとEllipsisを併用する
@app.get("/items/")
async def read_items3(q: Annotated[str | None, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# リスト形式のパラメータ
# ex. http://localhost:8000/items/?q=foo&q=bar
@app.get("/itemsss/")
async def read_items4(q: Annotated[list[str] | None, Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items
