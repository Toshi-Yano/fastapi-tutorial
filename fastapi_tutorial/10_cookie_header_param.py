from typing import Annotated

from fastapi import Cookie, FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}


@app.get("/items/")
async def read_items2(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}


@app.get("/items/")
async def read_items3(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None
):
    return {"strange_header": strange_header}


@app.get("/items/")
async def read_items4(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}
