import logging

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import uvicorn

from module.aws import SQS

app = FastAPI()
logger = logging.getLogger('root')


class Item(BaseModel):
    operation: str
    key: str
    mode: Optional[str] = None


@app.get("/")
def hello_world():
    logger.info('Welcome to FastAPI')
    return "Hello World!!!"


@app.post("/scrap/place")
def scrap_place(item: Item):
    logger.info('Request >>> Scrap Place : {}'.format(item))
    SQS().produce(dict(item))
    return 'Accepted Request'


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, log_config='./config/log.ini')
