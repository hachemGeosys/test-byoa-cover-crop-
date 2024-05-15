import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel
import datetime as dt
from dotenv import load_dotenv
from geosyspy.geosys import Region,Env
import json
from cover_crop.processor import Cover-crop

app = FastAPI(
    docs_url=None,
    title="cover-crop"+" API",
    description= "this is the cover crop processor"
    )
app.mount("/static", StaticFiles(directory="./api/files"), name="static")

@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="cover-crop"+" API",
        swagger_favicon_url="/static/favicon.svg"
    )
