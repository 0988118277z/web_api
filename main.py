#  py -m pip install fastapi uvicorn
#  py -m uvicorn main:app --reload --port 8080
from pydantic import ValidationError
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from router import accounty, helloy, imgconverty, qrcodey, ipy, dnsy
from sqly import models
from fastapi.responses import JSONResponse
from sqly.database import engine

app = FastAPI()
app.include_router(accounty.router)
app.include_router(helloy.router)
app.include_router(imgconverty.router)
app.include_router(qrcodey.router)
app.include_router(ipy.router)
app.include_router(dnsy.router)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return RedirectResponse(url="/docs", status_code=301)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()}
    )




