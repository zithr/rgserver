import os
import uvicorn

from io import BytesIO
from pathlib import Path
from typing import Annotated
from loguru import logger

from litestar import Litestar, get, Response, Request
from litestar.exceptions import NotAuthorizedException, ValidationException
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.static_files import create_static_files_router
from litestar.template.config import TemplateConfig
from litestar.datastructures import UploadFile
from litestar.enums import RequestEncodingType
from litestar.params import Body
from litestar.response import File, Template
from litestar.contrib.htmx.response import ClientRedirect
from litestar.background_tasks import BackgroundTask

BACKEND_SERVER_URL = os.getenv("BACKEND_SERVER_URL", "http://0.0.0.0:8000")


@get(path="/")
async def hello() -> Template:
    return Template(template_name="index.html")


app = Litestar(
    route_handlers=[
        hello,
        create_static_files_router(path="/static", directories=["src/assets"]),
    ],
    template_config=TemplateConfig(
        directory=Path("src/templates"),
        engine=JinjaTemplateEngine,
    ),
    debug=True,
)

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="0.0.0.0",
        port=8000,
        reload_delay=5,
        reload=BACKEND_SERVER_URL == "http://0.0.0.0:8000",
    )
