#  py -m pip install fastapi uvicorn
#  py -m uvicorn main:app --reload --port 8080
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from router import accounty, helloy, imgconverty, qrcodey, ipy
from sqly import models
from sqly.database import Base
from sqly.database import engine

app = FastAPI()
app.include_router(accounty.router)
app.include_router(helloy.router)
app.include_router(imgconverty.router)
app.include_router(qrcodey.router)
app.include_router(ipy.router)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return RedirectResponse(url="/docs", status_code=301)







