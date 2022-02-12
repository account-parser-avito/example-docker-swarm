import os
import sys

from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"nodename": os.uname().nodename}

@app.get("/data/")
def update_root():
    return {"data": "data"}

@app.get("/exit/")
def exit_root():
    sys.exit(0)
    # return {"nodename": os.uname().nodename}

@app.get("/break/")
def break_root():
    sys.exit(1)
    # return {"nodename": os.uname().nodename}

